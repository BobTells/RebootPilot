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
