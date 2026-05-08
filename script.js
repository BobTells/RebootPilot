const videoToggle = document.querySelector('[data-video-toggle]');
const toolToggle = document.querySelector('[data-tool-toggle]');
const videoStage = document.getElementById('videoStage');
const notebook = document.getElementById('toolNotebook');
const frame = notebook ? notebook.querySelector('iframe') : null;

videoToggle?.addEventListener('click', () => videoStage.classList.toggle('is-open'));
toolToggle?.addEventListener('click', () => {
  notebook.classList.add('is-open');
  if (frame && !frame.src) frame.src = frame.dataset.src;
});

document.querySelectorAll('[data-close-stage]').forEach((button) => {
  button.addEventListener('click', () => {
    const id = button.getAttribute('data-close-stage');
    document.getElementById(id)?.classList.remove('is-open');
  });
});
