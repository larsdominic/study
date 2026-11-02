# shared head/CSS for the study-site extra pages (each output file stays self-contained)
CSS = r'''
  :root{--paper:#F5F7F4;--ink:#1E2A33;--ink-soft:#4A5862;--rule:#D6DCD8;--indigo:#2F47A6;--indigo-soft:#E6EAF7;--amber:#B8761A;--amber-soft:#FBF1DF;--green:#2E7D4F;--green-soft:#E3F2E8;--red:#B23A3A;--red-soft:#F8E4E4;--grey:#8A949B;--card:#FFFFFF}
  *{box-sizing:border-box}
  body{margin:0;background:var(--paper);color:var(--ink);font:17px/1.6 "Segoe UI","Helvetica Neue",Helvetica,Arial,sans-serif;overflow-wrap:break-word}
  h1,h2,h3{font-family:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;line-height:1.2;margin:0 0 .4em;font-weight:600}
  h1{font-size:2.1rem} h2{font-size:1.5rem;margin-top:1.6em} h3{font-size:1.15rem;margin-top:1.4em}
  p{margin:0 0 1em} a{color:var(--indigo)}
  sup,sub{line-height:0}
  .wrap{max-width:820px;margin:0 auto;padding:0 20px 80px}
  .top{background:#0B0F1A;color:#fff;padding:26px 0 22px}
  .top h1{color:#fff} .top p{color:#C9D1E6;max-width:660px;margin-bottom:0}
  .top .crumb{font-size:.9rem;margin-bottom:8px} .top .crumb a{color:#F2C46D}
  table{border-collapse:collapse;width:100%;margin:12px 0 20px;font-size:.95rem;background:var(--card)}
  th,td{border:1px solid var(--rule);padding:8px 10px;text-align:left;vertical-align:top}
  th{background:#EDF0EC}
  .tablewrap{overflow-x:auto;-webkit-overflow-scrolling:touch}
  .card{background:var(--card);border:1px solid var(--rule);padding:14px 16px;margin:12px 0}
  .tip{background:var(--amber-soft);border-left:5px solid var(--amber);padding:12px 16px;margin:18px 0}
  .tip b:first-child{color:var(--amber)}
  .step{background:var(--card);border:1px solid var(--rule);border-left:5px solid var(--indigo);padding:12px 16px;margin:12px 0}
  .step .bh{display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 12px;margin-bottom:4px}
  .step .bh b{font-size:1.15rem;font-family:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif}
  .step .bh span{font-weight:700;color:var(--indigo)}
  .step ol{margin:6px 0 0;padding-left:22px} .step li{margin:4px 0}
  .t{color:var(--ink-soft);font-size:.88rem;white-space:nowrap}
  .tag{display:inline-block;font-size:.72rem;font-weight:700;padding:1px 7px;border-radius:3px;color:#fff;vertical-align:middle;white-space:nowrap}
  .quiz .q{background:var(--card);border:1px solid var(--rule);padding:14px 16px;margin:12px 0}
  .quiz .q > p{font-weight:600;margin-bottom:8px}
  .quiz .subj{display:inline-block;font-size:.75rem;font-weight:700;color:var(--indigo);background:var(--indigo-soft);padding:1px 7px;border-radius:3px;margin-right:6px;vertical-align:middle}
  .quiz button{display:block;width:100%;text-align:left;background:#F3F5F2;border:1px solid var(--rule);padding:8px 12px;margin:6px 0;border-radius:6px;font:inherit;cursor:pointer;color:var(--ink)}
  .quiz button:hover,.quiz button:focus-visible{border-color:var(--indigo);outline:none}
  .quiz button.right{background:var(--green-soft);border-color:var(--green)}
  .quiz button.wrong{background:var(--red-soft);border-color:var(--red)}
  .quiz .why{display:none;margin-top:8px;font-size:.95rem;color:var(--ink-soft)}
  .quiz .q.done .why{display:block}
  .score{font-weight:700;margin-top:14px}
  .frac{display:inline-flex;flex-direction:column;vertical-align:middle;text-align:center;font-size:.92em;line-height:1.15;margin:0 2px}
  .frac>span:first-child{border-bottom:1px solid currentColor;padding:0 3px}
  .frac>span:last-child{padding:0 3px}
  .nw{white-space:nowrap}
  @media (max-width:600px){h1{font-size:1.7rem}body{font-size:16px}th,td{padding:6px}}
'''
def page(title, crumb, h1, intro, body, script="", crumb_label="All study pages"):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>{CSS}</style>
</head>
<body>
<header class="top"><div class="wrap" style="padding-bottom:0">
  <div class="crumb"><a href="{crumb}">{crumb_label}</a></div>
  <h1>{h1}</h1>
  <p>{intro}</p>
</div></header>
<main class="wrap">
{body}
</main>
{('<script>'+script+'</script>') if script else ''}
</body>
</html>
'''
DRIVE=lambda i:f'https://drive.google.com/file/d/{i}/view'
SHEET='https://docs.google.com/spreadsheets/d/14eB8zIWZMuldcvLXTYNA4Q77jad3siDgHOK3mMrUCX8/edit'
