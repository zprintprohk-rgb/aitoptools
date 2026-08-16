const fs=require('fs');
const path=require('path');
const ROOT='F:/aitoptools';
const KEY_FILE=path.join(ROOT,'.hermes/secrets/indexnow-key.txt');
const LOG_DIR=path.join(ROOT,'.hermes/logs');
const URLS=[
 'https://aitoptools.net/resources/',
 'https://aitoptools.net/blog/kittl-halloween-template-test-2026/',
 'https://aitoptools.net/copy-ai-review/'
];
(async()=>{
 const key=fs.readFileSync(KEY_FILE,'utf-8').trim();
 if(!key||key.startsWith('#')){console.log('ERROR: key missing');process.exit(1)}
 const payload={host:'aitoptools.net',key:key,keyLocation:'https://aitoptools.net/'+key+'.txt',urlList:URLS};
 try{
  const resp=await fetch('https://api.indexnow.org/indexnow',{method:'POST',headers:{'Content-Type':'application/json; charset=utf-8'},body:JSON.stringify(payload)});
  const txt=await resp.text();
  const result={date:'2026-08-16',action:'INCREMENTAL-0816',status:resp.status,url_count:URLS.length,urls:URLS,body:txt.slice(0,200)};
  fs.writeFileSync(path.join(LOG_DIR,'indexnow-2026-08-16.log'),JSON.stringify(result,null,2),'utf-8');
  console.log(JSON.stringify(result,null,2));
  process.exit(resp.status===200?0:1);
 }catch(e){
  const result={date:'2026-08-16',action:'INCREMENTAL-0816',status:'NETWORK_ERROR',error:e.message,urls:URLS};
  fs.writeFileSync(path.join(LOG_DIR,'indexnow-2026-08-16.log'),JSON.stringify(result,null,2),'utf-8');
  console.log(JSON.stringify(result,null,2));
  process.exit(1);
 }
})();