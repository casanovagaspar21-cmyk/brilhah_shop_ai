function addMsg(text, who){ 
  const div = document.createElement('div');
  div.className = 'chat-msg';
  div.textContent = (who==='me'?'🧑‍💼 ':'🤖 ') + text;
  document.getElementById('chat-list').appendChild(div);
  div.scrollIntoView({behavior:'smooth',block:'end'});
}
function fakeReply(){
  const i = document.getElementById('chat-text');
  const v = i.value.trim(); if(!v) return;
  addMsg(v,'me'); i.value='';
  setTimeout(()=>addMsg('Resposta simulada. Na próxima versão ligo IA real gratuita.','bot'),500);
}
function demoSearch(){
  const q = document.getElementById('q').value.trim();
  const box = document.getElementById('results'); box.innerHTML='';
  const demo = [
    {name:'Fones Bluetooth', price:19.9, url:'#'},
    {name:'Powerbank 20.000mAh', price:16.9, url:'#'},
    {name:'Suporte Telemóvel', price:11.9, url:'#'},
  ].filter(x=>!q || x.name.toLowerCase().includes(q.toLowerCase()));
  demo.forEach(p=>{
    const c = document.createElement('div'); c.className='card';
    c.innerHTML = `<strong>${p.name}</strong><br>€ ${p.price.toFixed(2)}<br><a class="btn" href="${p.url}" target="_blank">Abrir</a>`;
    box.appendChild(c);
  });
}
