const videoToggle = document.querySelector('[data-video-toggle]');
const videoStage = document.getElementById('videoStage');
const scrim = document.getElementById('drawerScrim');
const drawers = Array.from(document.querySelectorAll('.notebook'));

function openDrawer(id) {
  drawers.forEach((d) => d.classList.toggle('is-open', d.id === id));
  const el = document.getElementById(id);
  if (!el) return;
  const iframe = el.querySelector('iframe');
  if (iframe && !iframe.src && iframe.dataset.src) iframe.src = iframe.dataset.src;
  if (scrim) {
    scrim.hidden = false;
    requestAnimationFrame(() => scrim.classList.add('is-visible'));
  }
  document.body.classList.add('drawer-open');
}

function closeDrawers() {
  drawers.forEach((d) => d.classList.remove('is-open'));
  if (scrim) {
    scrim.classList.remove('is-visible');
    setTimeout(() => { scrim.hidden = true; }, 300);
  }
  document.body.classList.remove('drawer-open');
}

videoToggle?.addEventListener('click', () => videoStage.classList.toggle('is-open'));

document.querySelectorAll('[data-tool-toggle]').forEach((el) => {
  el.addEventListener('click', () => openDrawer('toolNotebook'));
});

document.querySelectorAll('[data-bulletin-toggle]').forEach((el) => {
  el.addEventListener('click', (e) => {
    e.preventDefault();
    openDrawer('bulletinDrawer');
  });
});

document.querySelectorAll('[data-close-drawer]').forEach((button) => {
  button.addEventListener('click', closeDrawers);
});

document.querySelectorAll('[data-close-stage]').forEach((button) => {
  button.addEventListener('click', () => {
    const id = button.getAttribute('data-close-stage');
    document.getElementById(id)?.classList.remove('is-open');
  });
});

scrim?.addEventListener('click', closeDrawers);
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') closeDrawers();
});

const comicTrack = document.getElementById('comicTrack');
const comicCounter = document.getElementById('comicCounter');
const comicBanner = document.getElementById('comicBanner');
const comicPrev = document.querySelector('[data-comic-prev]');
const comicNext = document.querySelector('[data-comic-next]');
const comicDots = Array.from(document.querySelectorAll('[data-comic-dot]'));
const comicSlideCount = comicTrack ? comicTrack.children.length : 0;
let comicIndex = 0;

function updateComic() {
  if (!comicTrack) return;
  comicTrack.style.transform = `translateX(-${comicIndex * 100}%)`;
  if (comicCounter) comicCounter.textContent = `${comicIndex + 1} / ${comicSlideCount}`;
  if (comicBanner) comicBanner.hidden = comicIndex < 3;
  comicDots.forEach((dot, i) => {
    dot.setAttribute('aria-current', i === comicIndex ? 'true' : 'false');
  });
  if (comicPrev) comicPrev.disabled = comicIndex === 0;
  if (comicNext) comicNext.disabled = comicIndex === comicSlideCount - 1;
}

function comicGo(delta) {
  const next = comicIndex + delta;
  if (next < 0 || next >= comicSlideCount) return;
  comicIndex = next;
  updateComic();
}

comicPrev?.addEventListener('click', () => comicGo(-1));
comicNext?.addEventListener('click', () => comicGo(1));
comicDots.forEach((dot) => {
  dot.addEventListener('click', () => {
    comicIndex = parseInt(dot.dataset.comicDot, 10) || 0;
    updateComic();
  });
});

document.addEventListener('keydown', (e) => {
  if (!comicTrack) return;
  const t = e.target;
  if (t && (t.matches?.('input, textarea, select') || t.isContentEditable)) return;
  const drawerOpen = drawers.some((d) => d.classList.contains('is-open'));
  if (drawerOpen) return;
  if (e.key === 'ArrowLeft') comicGo(-1);
  if (e.key === 'ArrowRight') comicGo(1);
});

if (comicTrack) {
  let touchStartX = null;
  comicTrack.addEventListener('touchstart', (e) => { touchStartX = e.touches[0].clientX; }, { passive: true });
  comicTrack.addEventListener('touchend', (e) => {
    if (touchStartX === null) return;
    const dx = e.changedTouches[0].clientX - touchStartX;
    if (Math.abs(dx) > 40) comicGo(dx < 0 ? 1 : -1);
    touchStartX = null;
  });
  updateComic();
}
