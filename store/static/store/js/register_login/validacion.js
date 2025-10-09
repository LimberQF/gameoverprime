(() => {
  const form = document.getElementById("formRegistro");
  if (!form) return;

  const q = id => document.getElementById(id);

  form.addEventListener("submit", (e) => {
    const nombre = (q("nombreCompleto").value || "").trim();
    const usuario = (q("usuario").value || "").trim();
    const email = (q("email").value || "").trim();
    const pw1 = q("password").value;
    const pw2 = q("confirmPassword").value;
    const fnac = q("fechaNacimiento").value;

    if (!nombre || !usuario || !email || !pw1 || !pw2 || !fnac) {
      e.preventDefault();
      alert("Todos los campos son obligatorios, excepto la dirección.");
      return;
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      e.preventDefault();
      alert("El correo electrónico no tiene un formato válido.");
      return;
    }

    if (pw1 !== pw2) {
      e.preventDefault();
      alert("Las contraseñas no coinciden.");
      return;
    }

    const softPw = /^(?=.*[A-Z])(?=.*\d).{8,}$/;
    if (!softPw.test(pw1)) {
      e.preventDefault();
      alert("La contraseña debe tener mínimo 8 caracteres, incluir 1 mayúscula y 1 número.");
      return;
    }

    const hoy = new Date();
    const nacimiento = new Date(fnac);
    let edad = hoy.getFullYear() - nacimiento.getFullYear();
    const mes = hoy.getMonth() - nacimiento.getMonth();
    if (mes < 0 || (mes === 0 && hoy.getDate() < nacimiento.getDate())) edad--;
    if (edad < 13) {
      e.preventDefault();
      alert("Debes tener al menos 13 años para registrarte.");
      return;
    }

  });
})();
