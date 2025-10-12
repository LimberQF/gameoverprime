(() => {
  const form = document.getElementById('formLogin');
  const see  = document.getElementById('verPw');
  const pw   = document.getElementById('password');
  const ue   = document.getElementById('usuarioEmail');

  if (see && pw) {
    see.addEventListener('click', () => {
      pw.type = pw.type === 'password' ? 'text' : 'password';
      pw.focus();
    });
  }

  if (form) {
    form.addEventListener('submit', (e) => {
      if (!ue.value.trim() || !pw.value) {
        e.preventDefault();
        alert('Completa usuario/correo y contraseña.');
      }
    });
  }
})();
