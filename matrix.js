const canvas = document.getElementById('matrixCanvas');
const ctx = canvas.getContext('2d');

const columns = 50;
const columnWidth = 20;
const fontSize = 15;
const characters = '0123456789ABCDEF';

canvas.width = columns * columnWidth;
canvas.height = window.innerHeight;

const columnsData = Array.from({ length: columns }, () => ({
  length: Math.floor(Math.random() * (canvas.height / fontSize)),
  speed: Math.random() * 2 + 1,
  position: Math.floor(Math.random() * characters.length),
}));

function draw() {
  ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = '#0f0';
  ctx.font = `${fontSize}px monospace`;

  columnsData.forEach((column, index) => {
    const x = index * columnWidth;
    let y = 0;

    for (let i = 0; i < column.length; i++) {
      const charIndex = (column.position + i) % characters.length;
      const char = characters[charIndex];
      const yPos = y * fontSize;

      ctx.fillText(char, x, yPos);
      y++;
    }

    column.position = (column.position + column.speed) % characters.length;
  });

  requestAnimationFrame(draw);
}

window.addEventListener('resize', () => {
  canvas.height = window.innerHeight;
  columnsData.forEach(column => {
    column.length = Math.floor(Math.random() * (canvas.height / fontSize));
  });
});

draw();
