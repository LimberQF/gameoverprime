// Script de buscador juegos
const toggle=document.getElementById('themeToggle');
const saved=localStorage.getItem('theme');
if(saved==='dark'){document.documentElement.classList.add('dark');toggle.checked=true}
toggle.addEventListener('change',()=>{document.documentElement.classList.toggle('dark');const mode=document.documentElement.classList.contains('dark')?'dark':'light';localStorage.setItem('theme',mode)});
const input=document.getElementById('search');
const cards=Array.from(document.querySelectorAll('.card'));
input.addEventListener('input',()=>{const q=input.value.trim().toLowerCase();cards.forEach(c=>{const ok=c.dataset.title.includes(q);c.style.display=ok?'':'none'})});
document.getElementById('searchBtn').addEventListener('click',()=>{const first=cards.find(c=>c.style.display!=='none');first&&first.focus&&first.focus()});

// Tema claro/oscuro compartido y sincronizado
(() => {
  const STORAGE_KEY = 'theme';
  const root = document.documentElement;
  const applyTheme = (mode) => {
    root.classList.toggle('dark', mode === 'dark');
    document.querySelectorAll('#themeToggle, [data-theme-toggle]').forEach(el => {
      if ('checked' in el) el.checked = (mode === 'dark');
    });
  };
  const saved = localStorage.getItem(STORAGE_KEY) || 'light';
  applyTheme(saved);
  document.querySelectorAll('#themeToggle, [data-theme-toggle]').forEach(el => {
    el.addEventListener('change', () => {
      const mode = el.checked ? 'dark' : 'light';
      localStorage.setItem(STORAGE_KEY, mode);
      applyTheme(mode);
    });
  });
  window.addEventListener('storage', (e) => {
    if (e.key === STORAGE_KEY) {
      applyTheme(e.newValue === 'dark' ? 'dark' : 'light');
    }
  });
})();


// Script para las ofertas
(function ofertasAleatorias(){
  const grid = document.getElementById('grid');         
  const row  = document.getElementById('offersRow');    
  if (!grid || !row) return;
  const pool = Array.from(grid.querySelectorAll('.card'));
  if (!pool.length) return;
  const cuantos = Math.min(6, pool.length); 
  const usados = new Set();
  while (usados.size < cuantos) {
    usados.add(Math.floor(Math.random() * pool.length));
  }
  usados.forEach(i => {
    const clone = pool[i].cloneNode(true);
    const priceEl = clone.querySelector('.price');
    if (priceEl && !/free/i.test(priceEl.textContent)) {
      const digits = priceEl.textContent.replace(/[^\d]/g, '');
      const precio = parseInt(digits || '0', 10);
      const pct = 10 + Math.floor(Math.random() * 41); 
      const nuevo = Math.max(100, Math.round(precio * (1 - pct / 100)));
      priceEl.innerHTML =
        `CLP$ ${nuevo.toLocaleString('es-CL')} ` +
        `<s>CLP$ ${precio.toLocaleString('es-CL')}</s> ` +
        `<span class="discount">-${pct}%</span>`;
    }
    const th = clone.querySelector('.thumb');
    if (th) {
      th.style.position = 'relative';
      const b = document.createElement('div');
      b.className = 'badge-offer';
      b.textContent = 'OFERTA';
      Object.assign(b.style, { position:'absolute', top:'6px', left:'6px' });
      th.appendChild(b);
    }
    row.appendChild(clone);
  });
})();





