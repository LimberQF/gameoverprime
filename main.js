const toggle=document.getElementById('themeToggle');
const saved=localStorage.getItem('theme');
if(saved==='dark'){document.documentElement.classList.add('dark');toggle.checked=true}
toggle.addEventListener('change',()=>{document.documentElement.classList.toggle('dark');const mode=document.documentElement.classList.contains('dark')?'dark':'light';localStorage.setItem('theme',mode)});

const input=document.getElementById('search');
const cards=Array.from(document.querySelectorAll('.card'));
input.addEventListener('input',()=>{const q=input.value.trim().toLowerCase();cards.forEach(c=>{const ok=c.dataset.title.includes(q);c.style.display=ok?'':'none'})});

document.getElementById('searchBtn').addEventListener('click',()=>{const first=cards.find(c=>c.style.display!=='none');first&&first.focus&&first.focus()});





