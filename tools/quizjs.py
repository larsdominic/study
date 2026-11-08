# Shared quiz JavaScript.
# quiz_js(key): the whole quiz for generated pages (review.py and friends).
# ENGINE + ibQuizEnhance({key, own:false}) is what tools/enhance.py adds to hand-written guides,
# where the page's own quiz script already scores the first round.
#
# What the engine adds (the saved key keeps its old format {right,total,date,best}):
#  - "Sure / Guessing" toggle on every multiple-choice question; at the end the sure-but-wrong ones are listed first
#  - every finished round is kept as <key>-attempts = [{date,right,total}] (local date); timed pages ({score,max})
#    keep one entry per day
#  - "Try again (shuffled)": new question order and new option order, data-a moved with the right option
#  - .written[data-max] items get a self-mark menu 0..max saved as <key>-written = {id: mark}
import json

# storageOK(): shared check; shows the notice when this browser will not save (private mode and similar).
STORAGE_JS = r'''
function storageOK(){ try{ var k='__ib_t'; localStorage.setItem(k,'1'); localStorage.removeItem(k); return true; }catch(e){ return false; } }
function storageNotice(){ if(storageOK() || document.querySelector('.notice.storage')) return;
  var n=document.createElement('div'); n.className='notice storage'; n.setAttribute('role','status');
  n.textContent='Progress cannot be saved in this browser (private mode?). Use normal Safari or Chrome.';
  var sb=document.querySelector('.sitebar');   // under the shared top bar when the page has one
  if(sb && sb.parentNode){ sb.parentNode.insertBefore(n,sb.nextSibling); return; }
  var m=document.querySelector('main')||document.body; m.insertBefore(n,m.firstChild); }
'''

ENGINE = r'''
function ibQuizEnhance(cfg){
  if(window.__ibQuizEnh) return; window.__ibQuizEnh=1;
  if(typeof storageNotice==='function') storageNotice();
  var KEY=cfg&&cfg.key; if(!KEY) return;
  var AK=KEY+'-attempts', WK=KEY+'-written';
  function get(k){ try{ return JSON.parse(localStorage.getItem(k)||'null'); }catch(e){ return null; } }
  function put(k,v){ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(e){} }
  function pad(n){ return (n<10?'0':'')+n; }
  function today(){ var d=new Date(); return d.getFullYear()+'-'+pad(d.getMonth()+1)+'-'+pad(d.getDate()); }
  function attempts(){ var a=get(AK); return Array.isArray(a)?a:[]; }
  function addAttempt(r,t,sameDay){ var a=attempts(), d=today(), rec={date:d,right:r,total:t};
    if(sameDay && a.length && a[a.length-1].date===d) a[a.length-1]=rec; else a.push(rec); put(AK,a); return a; }
  // keep the score saved before this history existed as the first attempt
  (function(){ if(get(AK)) return; var r=get(KEY); if(!r||typeof r!=='object') return;
    var rr=(typeof r.right==='number')?r.right:r.score, tt=(typeof r.total==='number')?r.total:r.max;
    if(typeof rr==='number' && tt) put(AK,[{date:r.date||today(),right:rr,total:tt}]); })();

  // written answers: self-mark 0..max
  var W=get(WK); if(!W||typeof W!=='object') W={};
  [].forEach.call(document.querySelectorAll('.written[data-max]'),function(el,i){
    var max=parseInt(el.getAttribute('data-max'),10); if(!(max>=0) || el.querySelector('.wm')) return;
    var id=el.id||el.getAttribute('data-id')||('w'+(i+1));
    var box=document.createElement('div'); box.className='wm';
    var lab=document.createElement('label'); lab.appendChild(document.createTextNode('My mark: '));
    var sel=document.createElement('select'); sel.setAttribute('aria-label','Your mark out of '+max);
    var o=document.createElement('option'); o.value=''; o.textContent='not marked yet'; sel.appendChild(o);
    for(var m=0;m<=max;m++){ o=document.createElement('option'); o.value=String(m); o.textContent=m+' out of '+max; sel.appendChild(o); }
    if(W[id]!=null) sel.value=String(W[id]);
    sel.addEventListener('change',function(){ var w=get(WK); if(!w||typeof w!=='object') w={};
      if(sel.value==='') delete w[id]; else w[id]=parseInt(sel.value,10); put(WK,w); });
    lab.appendChild(sel); box.appendChild(lab); el.appendChild(box);
  });

  // timed pages save {score,max,date} themselves; keep one history entry per day
  if(/^ib-timed-/.test(KEY)){
    var rec=function(){ var r=get(KEY); if(r && typeof r.score==='number' && r.max) addAttempt(r.score,r.max,true); };
    var sb=document.getElementById('savebtn'); if(sb) sb.addEventListener('click',function(){ setTimeout(rec,0); });
    [].forEach.call(document.querySelectorAll('.score-t input'),function(i){ i.addEventListener('change',function(){ setTimeout(rec,0); }); });
  }

  // multiple-choice quiz
  var q0=document.querySelector('.quiz .q[data-a]'); if(!q0) return;
  var quiz=q0.closest('.quiz');
  var own=!!cfg.own, total=0, count=0, right=0, recs=[];
  function qsAll(){ return [].filter.call(quiz.querySelectorAll('.q[data-a]'),function(q){ return !q.classList.contains('written'); }); }
  function opts(q){ return [].filter.call(q.children,function(c){ return c.tagName==='BUTTON'; }); }
  var score=document.getElementById('score');
  if(!score){ score=document.createElement('div'); score.className='score'; score.id='score'; var l=qsAll(); l[l.length-1].parentNode.insertBefore(score,l[l.length-1].nextSibling); }
  var rep=document.createElement('div'); rep.className='cfr'; rep.setAttribute('aria-live','polite'); score.parentNode.insertBefore(rep,score.nextSibling);
  var hint=document.createElement('p'); hint.className='cfh';
  hint.textContent='Before each answer, say how sure you are. At the end, the ones you were sure about but got wrong are listed first: they matter most.';
  q0.parentNode.insertBefore(hint,qsAll()[0]);
  function addConf(q){ var p=q.querySelector('.cf'); if(p) p.parentNode.removeChild(p);
    var d=document.createElement('div'); d.className='cf'; d.setAttribute('role','group'); d.setAttribute('aria-label','How sure are you?');
    d.innerHTML='<div class="cfl-h">How sure are you?</div><div class="cfb"><button type="button" data-c="guess" aria-pressed="false">Guessed</button><button type="button" data-c="unsure" aria-pressed="false">Unsure</button><button type="button" data-c="sure" aria-pressed="false">Sure</button></div>';
    var first=opts(q)[0]; q.insertBefore(d,first||null); q.removeAttribute('data-conf'); }
  function counters(qs){ qs.forEach(function(q,i){ var c=q.querySelector('.qn'); if(!c){ c=document.createElement('div'); c.className='qn'; q.insertBefore(c,q.firstChild); } c.textContent=(i+1)+' of '+qs.length; }); }
  function start(){ var qs=qsAll(); total=qs.length; count=0; right=0; recs=[]; qs.forEach(addConf); counters(qs); rep.innerHTML=''; }
  function msg(){ return 'Score: '+right+' / '+total+' answered '+count+(count===total?(right>=0.8*total?'. Good. Log the ones you missed.':'. Re-read the sections for the ones you missed, then log them.'):''); }
  function qtext(q){ var p=q.querySelector('p'); var t=p?p.textContent:''; t=t.replace(/\s+/g,' ').trim();
    var s=p&&p.querySelector('.subj'); if(s) t=t.slice(s.textContent.trim().length).trim();
    t=t.replace(/^\d+\.\s*/,''); return t.length>110?t.slice(0,107)+'...':t; }
  function esc(s){ var d=document.createElement('div'); d.textContent=s; return d.innerHTML; }
  quiz.addEventListener('click',function(e){
    var b=e.target.closest?e.target.closest('button'):null; if(!b) return;
    var q=b.closest('.q'); if(!q || !quiz.contains(q) || !q.hasAttribute('data-a') || q.classList.contains('written')) return;
    var cf=b.closest('.cf');
    if(cf){ if(q.__ibRec) return; var c=b.getAttribute('data-c'); q.setAttribute('data-conf',c);
      [].forEach.call(cf.querySelectorAll('button'),function(x){ var on=x===b; x.classList.toggle('on',on); x.setAttribute('aria-pressed',on?'true':'false'); }); return; }
    if(b.parentNode!==q || q.__ibRec) return;
    if(own){
      if(q.classList.contains('done')) return;
      var bs=opts(q), a=parseInt(q.getAttribute('data-a'),10), i=bs.indexOf(b);
      q.classList.add('done');
      if(i===a) b.classList.add('right'); else { b.classList.add('wrong'); if(bs[a]) bs[a].classList.add('right'); }
    } else if(!q.classList.contains('done')) return;
    q.__ibRec=true; var ok=b.classList.contains('right'); if(ok) right++; count++;
    recs.push({q:q,ok:ok,conf:q.getAttribute('data-conf')||''});
    [].forEach.call(q.querySelectorAll('.cf button'),function(x){ x.disabled=true; });
    if(own) score.textContent=msg();
    if(count===total) finish();
  });
  function finish(){
    var r=right, t=total;
    if(own){ try{ var prev=get(KEY); localStorage.setItem(KEY,JSON.stringify({right:r,total:t,date:new Date().toISOString().slice(0,10),best:Math.max(r,prev&&prev.best||0)})); }catch(e){} }
    else { var s=get(KEY); if(s && typeof s.right==='number' && s.total) { r=s.right; t=s.total; } }
    var a=addAttempt(r,t,false);
    var order=qsAll(), num=function(q){ return order.indexOf(q)+1; };
    var wrong=recs.filter(function(x){ return !x.ok; });
    wrong.sort(function(x,y){ return (y.conf==='sure')-(x.conf==='sure') || num(x.q)-num(y.q); });
    var lucky=recs.filter(function(x){ return x.ok && (x.conf==='guess'||x.conf==='unsure'); }).sort(function(x,y){ return num(x.q)-num(y.q); });
    var lab={sure:'you were sure',unsure:'you were unsure',guess:'you guessed','':'not marked'};
    var h='';
    if(wrong.length){ h+='<b>Log these first</b><ol class="cfl">'+wrong.map(function(x){ return '<li'+(x.conf==='sure'?' class="sure"':'')+'>Question '+num(x.q)+' ('+lab[x.conf]+'): '+esc(qtext(x.q))+'</li>'; }).join('')+'</ol>'; }
    if(lucky.length){ h+='<b>Right, but not sure</b>: read the explanation again for '+lucky.map(function(x){ return 'question '+num(x.q); }).join(', ')+'.'; }
    if(!wrong.length && !lucky.length) h+='<b>All right.</b> Come back in a few days and try again: a score that lasts is what counts.';
    var past=a.slice(0,-1).slice(-3).map(function(x){ return x.right+'/'+x.total+' on '+x.date; });
    h+='<p class="cfa">Try number '+a.length+(past.length?'. Before: '+past.join(', ')+'.':'.')+'</p>';
    h+='<button type="button" class="retry">Try again (shuffled)</button>';
    rep.innerHTML=h;
    rep.querySelector('.retry').addEventListener('click',retry);
  }
  function shuffled(arr){ var best=arr.slice();
    for(var k=0;k<12;k++){ var x=arr.slice(); for(var i=x.length-1;i>0;i--){ var j=Math.floor(Math.random()*(i+1)); var t=x[i]; x[i]=x[j]; x[j]=t; }
      best=x; if(arr.length<2 || x.some(function(v,i){ return v!==arr[i]; })) break; }
    return best; }
  function renumber(q,n){ var p=q.querySelector('p'); if(!p) return;
    var w=document.createTreeWalker(p,4,null), tn;
    while((tn=w.nextNode())){ if(tn.parentNode.closest && tn.parentNode.closest('.subj')) continue; if(!/\S/.test(tn.data)) continue;
      if(/^\s*\d+\.\s/.test(tn.data)) tn.data=tn.data.replace(/^(\s*)\d+\./,'$1'+n+'.'); break; } }
  function retry(){
    var qs=qsAll(), marks=[], clones=[];
    qs.forEach(function(q){
      var m=document.createComment('q'); q.parentNode.insertBefore(m,q); marks.push(m);
      var c=q.cloneNode(true); c.classList.remove('done'); c.removeAttribute('data-conf');
      var p=c.querySelector('.cf'); if(p) p.parentNode.removeChild(p); p=c.querySelector('.qn'); if(p) p.parentNode.removeChild(p);
      var bs=opts(c), a=parseInt(c.getAttribute('data-a'),10), good=bs[a];
      bs.forEach(function(x){ x.classList.remove('right','wrong'); x.disabled=false; });
      if(bs.length){ var after=bs[bs.length-1].nextSibling, nb=shuffled(bs);
        bs.forEach(function(x){ c.removeChild(x); }); nb.forEach(function(x){ c.insertBefore(x,after); });
        c.setAttribute('data-a',String(nb.indexOf(good))); }
      q.parentNode.removeChild(q); clones.push(c);
    });
    var nq=shuffled(clones);
    marks.forEach(function(m,i){ m.parentNode.insertBefore(nq[i],m); m.parentNode.removeChild(m); renumber(nq[i],i+1); });
    own=true; start(); score.textContent='Score: 0 / '+total+' answered 0';
    var top=quiz.getBoundingClientRect().top+window.pageYOffset-60; try{ window.scrollTo(0,Math.max(0,top)); }catch(e){}
  }
  start();
}
'''

CSS = '''
:root{--amber-ink:#8A6416}
:focus-visible{outline:3px solid var(--indigo);outline-offset:2px}
.quiz button:focus-visible,.quiz .q .cf button:focus-visible{outline:3px solid var(--indigo);outline-offset:2px}
@media (hover:none){.quiz button:not(.right):not(.wrong):hover{border-color:var(--rule)}}
.quiz button.right::before{content:"✓ Correct: ";font-weight:700;color:var(--green)}
.quiz button.wrong::before{content:"✗ Your answer: ";font-weight:700;color:var(--red)}
.quiz .q .qn{font-size:.8rem;font-weight:700;color:var(--ink-soft);margin-bottom:2px}
.quiz .q .cf{margin:4px 0 10px}
.quiz .q .cf .cfl-h{font-size:.88rem;font-weight:600;color:var(--ink-soft);margin-bottom:4px}
.quiz .q .cf .cfb{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:6px;max-width:420px}
.quiz .q .cf button{display:block;width:100%;min-height:44px;margin:0;padding:6px 8px;text-align:center;font-size:.92rem;border:1px solid var(--rule);border-radius:8px;background:var(--card);color:var(--ink)}
.quiz .q .cf button.on{background:var(--indigo-soft);border:2px solid var(--indigo);font-weight:700}
.quiz .q .cf button:disabled{cursor:default;opacity:1;color:var(--ink-soft)}
.quiz .q .cf button.on:disabled{color:var(--ink)}
.quiz .cfh{font-size:.92rem;color:var(--ink-soft)}
.quiz .cfr{margin-top:10px}
.quiz .cfr ol{margin:6px 0 10px;padding-left:22px}
.quiz .cfr li{margin:4px 0}
.quiz .cfr li.sure{font-weight:600}
.quiz .cfr .cfa{font-size:.9rem;color:var(--ink-soft);margin:8px 0}
.quiz .cfr button.retry{display:inline-block;width:auto;min-height:44px;text-align:center;background:var(--indigo);color:#fff;border-color:var(--indigo);font-weight:700;padding:8px 16px}
.wm{margin-top:8px;font-size:.92rem}
.wm select{font:inherit;min-height:44px;padding:4px 6px;border:1px solid var(--rule);border-radius:8px;background:var(--card);color:var(--ink);max-width:100%}
.notice{background:var(--amber-soft);border:1px solid var(--amber);color:var(--ink);padding:10px 14px;margin:12px 0;border-radius:8px;font-weight:600}
'''


def quiz_js(key):
    """The full quiz script for generated pages (same scoring and saved format as before)."""
    return (STORAGE_JS + ENGINE + "\n(function(){ var s=document.createElement('style'); s.textContent=" + json.dumps(CSS)
            + "; document.head.appendChild(s); })();\nibQuizEnhance({key:" + json.dumps(key) + ", own:true});")
