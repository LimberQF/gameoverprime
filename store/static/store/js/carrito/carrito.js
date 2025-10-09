document.addEventListener('DOMContentLoaded', () => {
  const listaCarrito = document.getElementById('listaCarrito');
  const vacioMsg = document.getElementById('vacioMsg');
  const bloqueTotales = document.getElementById('bloqueTotales');
  const netoTxt = document.getElementById('netoTxt');
  const ivaTxt = document.getElementById('ivaTxt');
  const totalTxt = document.getElementById('totalTxt');
  const vaciarBtn = document.getElementById('vaciarBtn');
  const formato = new Intl.NumberFormat('es-CL', { style:'currency', currency:'CLP' });

  const leer = () => JSON.parse(localStorage.getItem('carrito') || '[]');
  const escribir = datos => localStorage.setItem('carrito', JSON.stringify(datos));

  const pintar = () => {
    const carrito = leer();
    listaCarrito.innerHTML = '';

    if (!carrito.length) {
      vacioMsg.style.display = 'block';
      bloqueTotales.style.display = 'none';
      return;
    }

    vacioMsg.style.display = 'none';

    let total = 0;

    carrito.forEach((item, i) => {
      const subtotal = item.precio * item.cantidad;
      total += subtotal;

      const tarjeta = document.createElement('article');
      tarjeta.className = 'card';
      tarjeta.innerHTML = `
        <div class="title">${item.nombre}</div>
        <div class="price">${formato.format(item.precio)}</div>
        <div class="form-row" style="margin-top:8px;">
          <div class="btn" data-accion="menos" data-i="${i}">−</div>
          <div class="btn" style="pointer-events:none;">${item.cantidad}</div>
          <div class="btn" data-accion="mas" data-i="${i}">+</div>
          <div class="spacer"></div>
          <div class="btn btn-secondary" style="pointer-events:none;">Subtotal: ${formato.format(subtotal)}</div>
        </div>
        <div class="form-row" style="margin-top:8px; justify-content:flex-end;">
          <button class="btn" data-accion="borrar" data-i="${i}">Eliminar</button>
        </div>
      `;
      listaCarrito.appendChild(tarjeta);
    });

    const neto = Math.round(total / 1.19);
    const iva = total - neto;
    netoTxt.textContent = formato.format(neto);
    ivaTxt.textContent = formato.format(iva);
    totalTxt.textContent = formato.format(total);
    bloqueTotales.style.display = 'block';

    // Delegación de eventos (menos/mas/borrar)
    listaCarrito.querySelectorAll('[data-accion]').forEach(btn => {
      btn.addEventListener('click', () => {
        const accion = btn.dataset.accion;
        const i = parseInt(btn.dataset.i, 10);
        const c = leer();

        if (accion === 'menos') {
          if (c[i].cantidad > 1) c[i].cantidad--; else c.splice(i,1);
        }
        if (accion === 'mas') {
          c[i].cantidad++;
        }
        if (accion === 'borrar') {
          c.splice(i,1);
        }
        escribir(c);
        pintar();
      });
    });
  };

  vaciarBtn.addEventListener('click', () => {
    localStorage.setItem('carrito', '[]');
    pintar();
  });

  pintar();
});
