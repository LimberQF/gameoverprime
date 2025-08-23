(() => {
  const form = document.getElementById('formLogin');
  const see = document.getElementById('verPw');
  const pw  = document.getElementById('password');
  if (see && pw) see.addEventListener('click', () => {
    pw.type = pw.type === 'password' ? 'text' : 'password';
  });
  if (!form) return;
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const ue = (document.getElementById('usuarioEmail').value || '').trim().toLowerCase();
    const pass = pw.value;
    const users = JSON.parse(localStorage.getItem('users') || '[]');
    const u = users.find(x =>
      (x.usuario?.toLowerCase() === ue || x.email?.toLowerCase() === ue) && x.password === pass
    );
    if (!u) { alert('Usuario o contraseña incorrectos.'); return; }
    localStorage.setItem('currentUser', JSON.stringify({
      usuario: u.usuario, nombre: u.nombreCompleto || u.nombre || '', email: u.email
    }));
    alert('¡Bienvenido, ' + (u.nombreCompleto || u.nombre || u.usuario) + '!');
    window.location.href = '../home_page.html';
  });
})();

