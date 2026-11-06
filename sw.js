const C='workout-v6';
// The page itself (index.html) is fetched network-first so a new version shows up on the next
// launch; if the network is slow or missing (gym), the cached copy is used after 3 s.
// Everything else (icons, exercise sprites) is cache-first and refreshed in the background.
const SHELL=['./','index.html','manifest.webmanifest','icon-180.png','icon-192.png'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(C).then(c=>c.addAll(SHELL.map(u=>new Request(u,{cache:'reload'})))));self.skipWaiting();});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==C).map(x=>caches.delete(x)))).then(()=>self.clients.claim()));});
self.addEventListener('fetch',e=>{
  const q=e.request; if(q.method!=='GET')return;
  const u=new URL(q.url); if(u.origin!==location.origin)return;
  const page=q.mode==='navigate'||u.pathname.endsWith('/index.html');
  e.respondWith(caches.open(C).then(async c=>{
    const key=page?'index.html':q;
    const hit=await c.match(key,{ignoreSearch:page});
    const net=fetch(q,{cache:'no-cache'}).then(r=>{if(r.ok)c.put(key,r.clone());return r;});
    if(!page)return hit||net.catch(()=>hit);
    if(!hit)return net;
    // network-first with a 3 s fallback to the cached page
    return Promise.race([net.catch(()=>hit),new Promise(r=>setTimeout(()=>r(hit),3000))]);
  }));
});
