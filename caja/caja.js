document.addEventListener('DOMContentLoaded', () => {
  const listaItems = document.getElementById('listaItems');
  const netoTxt = document.getElementById('netoTxt');
  const ivaTxt = document.getElementById('ivaTxt');
  const totalTxt = document.getElementById('totalTxt');
  const formPago = document.getElementById('formPago');
  const formato = new Intl.NumberFormat('es-CL', { style:'currency', currency:'CLP' });

  const leerCarrito = () => JSON.parse(localStorage.getItem('carrito') || '[]');
  const escribirCarrito = datos => localStorage.setItem('carrito', JSON.stringify(datos));

  const carrito = leerCarrito();

  if (!carrito.length) {
    listaItems.innerHTML = `<div class="muted">No hay productos en el carrito.</div>`;
    netoTxt.textContent = '—';
    ivaTxt.textContent = '—';
    totalTxt.textContent = '—';
  } else {
    let total = 0;
    listaItems.innerHTML = '';
    carrito.forEach(it => {
      const subtotal = it.precio * it.cantidad;
      total += subtotal;
      const fila = document.createElement('a');
      fila.className = 'cat-btn';
      fila.href = 'javascript:void(0)';
      fila.textContent = `${it.nombre} × ${it.cantidad} — ${formato.format(subtotal)}`;
      listaItems.appendChild(fila);
    });
    const neto = Math.round(total / 1.19);
    const iva = total - neto;
    netoTxt.textContent = formato.format(neto);
    ivaTxt.textContent = formato.format(iva);
    totalTxt.textContent = formato.format(total);
  }

  formPago.addEventListener('submit', e => {
    e.preventDefault();

    const nombre = document.getElementById('nombre').value.trim();
    const correo = document.getElementById('correo').value.trim();
    const rut = document.getElementById('rut').value.trim();
    const metodo = document.getElementById('metodo').value;
    const notas = document.getElementById('notas').value.trim();

    if (!carrito.length) { alert('Tu carrito está vacío.'); return; }
    if (!nombre || !correo || !rut || !metodo) { alert('Completa los campos requeridos.'); return; }

    const total = carrito.reduce((acc, it) => acc + it.precio * it.cantidad, 0);

    const orden = {
      id: 'ORD-' + Date.now(),
      fecha: new Date().toISOString(),
      cliente: { nombre, correo, rut },
      metodo,
      notas,
      items: carrito,
      total
    };

    const historial = JSON.parse(localStorage.getItem('ordenes') || '[]');
    historial.push(orden);
    localStorage.setItem('ordenes', JSON.stringify(historial));

    escribirCarrito([]); // vacía el carrito

    alert(`✅ Pago exitoso\nOrden: ${orden.id}\nTotal: ${new Intl.NumberFormat('es-CL',{style:'currency',currency:'CLP'}).format(total)}`);
    window.location.href = '../index.html'; // ajusta si tu inicio está en otra ruta
  });
});
