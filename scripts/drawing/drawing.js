let translations;
let canvas, ctx;
let isDrawing = false;
let lastX = 0;
let lastY = 0;

function loadTranslations(data) {
    translations = data;
    document.getElementById('pageTitle').textContent = translations.pageTitle;
    document.getElementById('mainHeader').textContent = translations.mainHeader;
    document.getElementById('clearBtn').textContent = translations.clearBtn;
    document.getElementById('saveBtn').textContent = translations.saveBtn;
}

function setupDrawingApp() {
    canvas = document.getElementById('drawingCanvas');
    ctx = canvas.getContext('2d');

    // Set canvas size
    canvas.width = window.innerWidth * 0.8;
    canvas.height = window.innerHeight * 0.8;

    // Event listeners
    canvas.addEventListener('mousedown', startDrawing);
    canvas.addEventListener('mousemove', draw);
    canvas.addEventListener('mouseup', stopDrawing);
    canvas.addEventListener('mouseout', stopDrawing);

    document.getElementById('clearBtn').addEventListener('click', clearCanvas);
    document.getElementById('saveBtn').addEventListener('click', saveDrawing);

    // Touch events for mobile
    canvas.addEventListener('touchstart', handleTouch);
    canvas.addEventListener('touchmove', handleTouch);
    canvas.addEventListener('touchend', stopDrawing);
}

function startDrawing(e) {
    isDrawing = true;
    [lastX, lastY] = [e.offsetX, e.offsetY];
}

function draw(e) {
    if (!isDrawing) return;
    ctx.beginPath();
    ctx.moveTo(lastX, lastY);
    ctx.lineTo(e.offsetX, e.offsetY);
    ctx.strokeStyle = document.getElementById('colorPicker').value;
    ctx.lineWidth = document.getElementById('brushSize').value;
    ctx.lineCap = 'round';
    ctx.stroke();
    [lastX, lastY] = [e.offsetX, e.offsetY];
}

function stopDrawing() {
    isDrawing = false;
}

function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

function saveDrawing() {
    const dataURL = canvas.toDataURL('image/png');
    const link = document.createElement('a');
    link.download = 'my-drawing.png';
    link.href = dataURL;
    link.click();
}

function handleTouch(e) {
    e.preventDefault();
    const touch = e.touches[0];
    const mouseEvent = new MouseEvent("mousemove", {
        clientX: touch.clientX,
        clientY: touch.clientY
    });
    canvas.dispatchEvent(mouseEvent);
}