def quiz_js(key):
    return '''(function(){
  var KEY='%s';
  var qs=document.querySelectorAll('.quiz .q'); var right=0, done=0, total=qs.length;
  qs.forEach(function(q){
    var a=parseInt(q.dataset.a,10); var btns=q.querySelectorAll('button');
    btns.forEach(function(b,i){ b.addEventListener('click',function(){
      if(q.classList.contains('done')) return;
      q.classList.add('done'); done++;
      if(i===a){ b.classList.add('right'); right++; } else { b.classList.add('wrong'); btns[a].classList.add('right'); }
      document.getElementById('score').textContent='Score: '+right+' / '+total+' answered '+done+(done===total?(right>=0.8*total?'. Good. Log the ones you missed.':'. Re-read the sections for the ones you missed, then log them.'):'');
      if(done===total){ try{ var prev=JSON.parse(localStorage.getItem(KEY)||'null'); var rec={right:right,total:total,date:new Date().toISOString().slice(0,10),best:Math.max(right,prev&&prev.best||0)}; localStorage.setItem(KEY,JSON.stringify(rec)); }catch(e){} }
    }); });
  });
})();''' % key
