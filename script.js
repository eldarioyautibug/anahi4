/* ─── NAVEGACIÓN ─────────────────────────────────────── */
function navegar(seccion, elemento) {
  document.querySelectorAll('.pantalla').forEach(p => p.classList.remove('pantalla-activa'));

  const destino = document.getElementById('seccion-' + seccion);
  if (destino) destino.classList.add('pantalla-activa');

  document.querySelectorAll('.menu-link').forEach(l => l.classList.remove('activo'));
  if (elemento) elemento.classList.add('activo');

  if (window.innerWidth <= 820) {
    document.getElementById('nav-links')?.classList.remove('show');
  }

  window.scrollTo({ top: 0, behavior: 'smooth' });
  setTimeout(rescanReveals, 80);
}

/* ─── INIT ────────────────────────────────────────────── */
document.addEventListener('DOMContentLoaded', () => {

  /* ── Loader ── */
  const loader = document.createElement('div');
  loader.className = 'page-loader';
  loader.innerHTML = `<div class="loader-ring"></div><div class="loader-text">Cargando proyecto</div>`;
  document.body.appendChild(loader);
  window.addEventListener('load', () => {
    setTimeout(() => loader.classList.add('hidden'), 300);
    setTimeout(() => loader.remove(), 1050);
  });
  setTimeout(() => { loader.classList.add('hidden'); setTimeout(() => loader.remove(), 750); }, 2800);

  /* ── Barra de progreso ── */
  const bar = document.createElement('div');
  bar.className = 'scroll-progress-bar';
  document.body.appendChild(bar);
  initScrollProgress(bar);

  /* ── Menú móvil ── */
  const toggle = document.getElementById('menu-toggle');
  const navEl  = document.getElementById('nav-links');
  if (toggle && navEl) {
    toggle.addEventListener('click', e => { e.stopPropagation(); navEl.classList.toggle('show'); });
    document.addEventListener('click', e => {
      if (!navEl.contains(e.target) && !toggle.contains(e.target)) navEl.classList.remove('show');
    });
    document.addEventListener('keydown', e => { if (e.key === 'Escape') navEl.classList.remove('show'); });
  }

  /* ── Header scroll ── */
  window.addEventListener('scroll', () => {
    document.querySelector('.header')?.classList.toggle('scrolled', window.scrollY > 50);
  }, { passive: true });

  autoMarkReveals();
  initRevealObserver();
  initCardTilt();
  initParallax();
});

/* ─── AUTO MARK REVEALS ───────────────────────────────── */
function autoMarkReveals() {
  document.querySelectorAll('.conceptos-grid, .var-grid, .grid-navegacion-cards, .rpubs-grid')
    .forEach(el => el.classList.add('reveal-stagger'));

  document.querySelectorAll('.tabla-contenedor, .wrapper-tabla-scroll, .mapa-container')
    .forEach(el => el.classList.add('reveal-zoom'));
}

/* ─── INTERSECTION OBSERVER ───────────────────────────── */
let _revealObs = null;

function initRevealObserver() {
  if (!('IntersectionObserver' in window)) {
    document.querySelectorAll('.reveal-up,.reveal-left,.reveal-right,.reveal-zoom,.reveal-stagger')
      .forEach(el => el.classList.add('is-visible'));
    return;
  }

  _revealObs = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('is-visible');
        _revealObs.unobserve(e.target);
      }
    });
  }, { threshold: 0.10, rootMargin: '0px 0px -50px 0px' });

  rescanReveals();
}

function rescanReveals() {
  if (!_revealObs) return;
  document.querySelectorAll(
    '.reveal-up:not(.is-visible),.reveal-left:not(.is-visible),.reveal-right:not(.is-visible),.reveal-zoom:not(.is-visible),.reveal-stagger:not(.is-visible)'
  ).forEach(el => _revealObs.observe(el));
}

/* ─── TILT 3D ─────────────────────────────────────────── */
function initCardTilt() {
  if (window.matchMedia('(pointer: coarse)').matches) return;
  const MAX = 7;

  document.querySelectorAll('.tarjeta-concepto, .reg-card, .card-minimal-inferencial, .tarjeta-v').forEach(card => {
    card.style.transformStyle = 'preserve-3d';

    card.addEventListener('mousemove', e => {
      const r  = card.getBoundingClientRect();
      const rx = -((e.clientY - r.top  - r.height / 2) / (r.height / 2)) * MAX;
      const ry =  ((e.clientX - r.left - r.width  / 2) / (r.width  / 2)) * MAX;
      card.style.transform = `perspective(900px) rotateX(${rx.toFixed(2)}deg) rotateY(${ry.toFixed(2)}deg) translateY(-6px)`;
    });

    card.addEventListener('mouseleave', () => { card.style.transform = ''; });
  });
}

/* ─── PARALLAX HERO ───────────────────────────────────── */
function initParallax() {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const hero = document.querySelector('.hero');
  if (!hero) return;
  let ticking = false;

  window.addEventListener('scroll', () => {
    if (!ticking) {
      requestAnimationFrame(() => {
        const y = window.scrollY;
        const content = hero.querySelector('.hero-content');
        if (content && hero.getBoundingClientRect().bottom > 0) {
          content.style.transform = `translateY(${Math.min(y * 0.09, 55)}px)`;
          content.style.opacity   = Math.max(1 - y / (window.innerHeight * 0.82), 0).toString();
        }
        ticking = false;
      });
      ticking = true;
    }
  }, { passive: true });
}

/* ─── SCROLL PROGRESS ─────────────────────────────────── */
function initScrollProgress(bar) {
  if (!bar) return;
  let ticking = false;
  const update = () => {
    const h = document.documentElement;
    const pct = h.scrollHeight - h.clientHeight > 0
      ? (h.scrollTop / (h.scrollHeight - h.clientHeight)) * 100
      : 0;
    bar.style.width = pct + '%';
    ticking = false;
  };
  window.addEventListener('scroll', () => {
    if (!ticking) { requestAnimationFrame(update); ticking = true; }
  }, { passive: true });
  update();
}

/* ─── DROPDOWN "MÁS" ──────────────────────────────────── */
function toggleMas(ev) {
  if (ev) { ev.preventDefault(); ev.stopPropagation(); }
  document.getElementById('nav-mas')?.classList.toggle('open');
}

document.addEventListener('click', (e) => {
  const li = document.getElementById('nav-mas');
  if (li && !li.contains(e.target)) li.classList.remove('open');
});
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') document.getElementById('nav-mas')?.classList.remove('open');
});

/* ─── BACKGROUND CANVAS GLOBAL (partículas en todo el sitio) ─── */
(function () {
  const canvas = document.getElementById('bg-particles');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const palette = ['#E7F5DC', '#C1F1B9', '#8BC190', '#68A77C', '#728156'];
  let w, h, particles, mouseX = 0, mouseY = 0;

  function resize() {
    w = canvas.width  = window.innerWidth;
    h = canvas.height = window.innerHeight;
  }

  function mkP(spread) {
    const layer = Math.random();   // 0 = lejano (lento+pequeño), 1 = cercano (rápido+grande)
    return {
      x:      Math.random() * w,
      y:      spread ? Math.random() * h : -10,
      r:      0.5 + layer * 2.2,
      speed:  0.15 + layer * 0.5,
      alpha:  0.12 + layer * 0.5,
      color:  palette[Math.floor(Math.random() * palette.length)],
      wobble: Math.random() * Math.PI * 2,
      wSpd:   (Math.random() - 0.5) * 0.022,
      layer:  layer,
    };
  }

  function init() {
    resize();
    particles = Array.from({ length: 160 }, () => mkP(true));
  }

  function frame() {
    ctx.clearRect(0, 0, w, h);

    // Líneas conectoras entre partículas cercanas (efecto constelación)
    for (let i = 0; i < particles.length; i++) {
      const a = particles[i];
      for (let j = i + 1; j < particles.length; j++) {
        const b = particles[j];
        const dx = a.x - b.x, dy = a.y - b.y;
        const d2 = dx * dx + dy * dy;
        if (d2 < 9000) {
          ctx.save();
          ctx.globalAlpha = (1 - d2 / 9000) * 0.15;
          ctx.strokeStyle = '#8BC190';
          ctx.lineWidth = 0.6;
          ctx.beginPath();
          ctx.moveTo(a.x, a.y);
          ctx.lineTo(b.x, b.y);
          ctx.stroke();
          ctx.restore();
        }
      }
    }

    // Partículas
    particles.forEach(p => {
      p.y += p.speed;
      p.wobble += p.wSpd;
      p.x += Math.sin(p.wobble) * 0.4;

      // Drift suave hacia el cursor (parallax cursor)
      const dx = mouseX - p.x, dy = mouseY - p.y;
      const dist = Math.sqrt(dx*dx + dy*dy);
      if (dist < 180) {
        p.x -= (dx / dist) * 0.3 * p.layer;
        p.y -= (dy / dist) * 0.3 * p.layer;
      }

      if (p.y > h + 10) Object.assign(p, mkP(false));
      if (p.x < -10)    p.x = w + 10;
      if (p.x > w + 10) p.x = -10;

      ctx.save();
      ctx.globalAlpha = p.alpha;
      ctx.fillStyle = p.color;
      ctx.shadowBlur = 6;
      ctx.shadowColor = p.color;
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fill();
      ctx.restore();
    });

    requestAnimationFrame(frame);
  }

  window.addEventListener('resize', init);
  window.addEventListener('mousemove', (e) => { mouseX = e.clientX; mouseY = e.clientY; }, { passive: true });
  init();
  frame();
})();

/* ─── HERO CANVAS PARTÍCULAS — para todos los .particle-canvas ── */
(function () {
  const canvases = document.querySelectorAll('.particle-canvas');
  if (!canvases.length) return;

  const palette = ['#E7F5DC', '#C1F1B9', '#8BC190', '#68A77C', '#728156', '#ffffff', '#a8d5b0'];

  canvases.forEach(canvas => {
    const ctx = canvas.getContext('2d');
    let w, h, particles;

    function resize() {
      w = canvas.width  = canvas.offsetWidth  || canvas.parentElement.offsetWidth;
      h = canvas.height = canvas.offsetHeight || canvas.parentElement.offsetHeight;
    }

    function mkP(spread) {
      return {
        x:      Math.random() * (w || 800),
        y:      spread ? Math.random() * (h || 600) : -8,
        r:      Math.random() * 2.4 + 0.3,
        speed:  Math.random() * 0.6 + 0.15,
        alpha:  Math.random() * 0.6 + 0.1,
        color:  palette[Math.floor(Math.random() * palette.length)],
        wobble: Math.random() * Math.PI * 2,
        wSpd:   (Math.random() - 0.5) * 0.028,
      };
    }

    function init() {
      resize();
      particles = Array.from({ length: 110 }, () => mkP(true));
    }

    function frame() {
      ctx.clearRect(0, 0, w, h);
      particles.forEach(p => {
        p.y += p.speed;
        p.wobble += p.wSpd;
        p.x += Math.sin(p.wobble) * 0.5;
        if (p.y > h + 10) Object.assign(p, mkP(false));
        ctx.save();
        ctx.globalAlpha = p.alpha;
        ctx.fillStyle   = p.color;
        ctx.shadowBlur  = 5;
        ctx.shadowColor = p.color;
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();
      });
      requestAnimationFrame(frame);
    }

    window.addEventListener('resize', init);
    // Reinit cuando cambia la pantalla (porque pasa de display:none a block)
    new ResizeObserver(() => { if (canvas.offsetWidth !== w) init(); }).observe(canvas);

    init();
    frame();
  });
})();

/* ─── BUSCADOR Y FILTRO ───────────────────────────────── */
const buscador   = document.getElementById("buscador-tabla");
const filtroTipo = document.getElementById("filtro-tipo");
const filasTabla = document.querySelectorAll("#miTabla tbody tr");

function filtrarTabla() {
  const texto = buscador.value.toLowerCase();
  const tipo  = filtroTipo.value;
  filasTabla.forEach(fila => {
    const textoOk = fila.textContent.toLowerCase().includes(texto);
    const tipoOk  = tipo === "Todos" || fila.cells[3]?.textContent.trim() === tipo;
    fila.style.display = textoOk && tipoOk ? "" : "none";
  });
}

if (buscador && filtroTipo) {
  buscador.addEventListener("keyup",  filtrarTabla);
  filtroTipo.addEventListener("change", filtrarTabla);
}

/* ─── MODAL ───────────────────────────────────────────── */
function cerrarModal() {
  const overlay = document.getElementById('overlay');
  if (!overlay) return;
  overlay.classList.add('closing');
  setTimeout(() => overlay.remove(), 350);
}

document.getElementById('overlay')?.addEventListener('click', function(e) {
  if (e.target === this) cerrarModal();
});
