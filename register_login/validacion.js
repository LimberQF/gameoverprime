(() => {
  const form = document.getElementById("formRegistro");
  if (!form) return;
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    const nombre = (document.getElementById("nombreCompleto").value || "").trim();
    const usuario = (document.getElementById("usuario").value || "").trim();
    const email = (document.getElementById("email").value || "").trim();
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirmPassword").value;
    const fechaNacimiento = document.getElementById("fechaNacimiento").value;
    const direccion = (document.getElementById("direccion")?.value || "").trim();
    if (!nombre || !usuario || !email || !password || !confirmPassword || !fechaNacimiento) {
      alert("Todos los campos son obligatorios, excepto la dirección.");
      return;
    }
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      alert("El correo electrónico no tiene un formato válido.");
      return;
    }
    if (password !== confirmPassword) {
      alert("Las contraseñas no coinciden.");
      return;
    }
    const passwordRegex = /^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,18}$/;
    if (!passwordRegex.test(password)) {
      alert("La contraseña debe tener entre 6 y 18 caracteres, al menos una mayúscula y un número.");
      return;
    }
    const hoy = new Date();
    const nacimiento = new Date(fechaNacimiento);
    let edad = hoy.getFullYear() - nacimiento.getFullYear();
    const mes = hoy.getMonth() - nacimiento.getMonth();
    if (mes < 0 || (mes === 0 && hoy.getDate() < nacimiento.getDate())) {
      edad--;
    }
    if (edad < 13) {
      alert("Debes tener al menos 13 años para registrarte.");
      return;
    }
    const key = "users";
    const users = JSON.parse(localStorage.getItem(key) || "[]");
    const exists = users.some(u =>
      (u.usuario?.toLowerCase() === usuario.toLowerCase()) ||
      (u.email?.toLowerCase() === email.toLowerCase())
    );
    if (exists) {
      alert("El nombre de usuario o correo ya está registrado.");
      return;
    }
    const nuevo = {
      nombreCompleto: nombre,
      usuario,
      email,
      fechaNacimiento,
      direccion,
      password,              
      createdAt: new Date().toISOString()
    };
    users.push(nuevo);
    localStorage.setItem(key, JSON.stringify(users));
    alert("¡Registro exitoso! Ahora puedes iniciar sesión.");
    window.location.href = "./login.html";
  });
})();