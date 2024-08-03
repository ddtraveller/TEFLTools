let texts = {};

function loadJSON(callback) {
    var xhr = new XMLHttpRequest();
    xhr.overrideMimeType("application/json");
    xhr.open('GET', 'https://tl-web.s3.us-west-2.amazonaws.com/math/geometry_calculator.json', true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == "200") {
            callback(JSON.parse(xhr.responseText));
        }
    };
    xhr.send(null);
}

function init() {
    loadJSON(function(data) {
        texts = data;
        updatePageText();
        setupEventListeners();
        updateInputFields(); // Initialize with default shape
    });
}

function updatePageText() {
    document.title = texts.pageTitle;
    document.getElementById('mainHeader').textContent = texts.mainHeader;
    document.getElementById('toggleInstructionsBtn').textContent = texts.toggleInstructionsBtn;
    document.getElementById('instructionsHeader').textContent = texts.instructionsHeader;
    document.getElementById('instructionsText').textContent = texts.instructionsText;
    document.getElementById('calculateBtn').textContent = texts.calculateBtn;
    document.getElementById('resultHeader').textContent = texts.resultHeader;
    document.getElementById('equationHeader').textContent = texts.equationHeader;
    document.getElementById('equationInput').placeholder = texts.equationInputPlaceholder;
    document.getElementById('solveEquationBtn').textContent = texts.solveEquationBtn;
}

function setupEventListeners() {
    document.getElementById('toggleInstructionsBtn').addEventListener('click', toggleInstructions);
    document.getElementById('shapeSelect').addEventListener('change', updateInputFields);
    document.getElementById('calculateBtn').addEventListener('click', calculate);
    document.getElementById('solveEquationBtn').addEventListener('click', solveEquation);
}

function toggleInstructions() {
    const instructionsSection = document.getElementById('instructionsSection');
    const toggleButton = document.getElementById('toggleInstructionsBtn');
    if (instructionsSection.style.display === 'none') {
        instructionsSection.style.display = 'block';
        toggleButton.textContent = texts.hideInstructionsBtn;
    } else {
        instructionsSection.style.display = 'none';
        toggleButton.textContent = texts.toggleInstructionsBtn;
    }
}

function updateInputFields() {
    const shape = document.getElementById('shapeSelect').value;
    const inputSection = document.getElementById('inputSection');
    inputSection.innerHTML = '';

    switch (shape) {
        case 'annulus':
            inputSection.innerHTML = `
                <input type="number" id="outerRadius" placeholder="${texts.outerRadiusPlaceholder}" value="5">
                <input type="number" id="innerRadius" placeholder="${texts.innerRadiusPlaceholder}" value="3">
            `;
            break;
        case 'circle':
            inputSection.innerHTML = `<input type="number" id="radius" placeholder="${texts.radiusPlaceholder}" value="5">`;
            break;
        case 'distance2d':
            inputSection.innerHTML = `
                <input type="number" id="x1" placeholder="${texts.x1Placeholder}" value="0">
                <input type="number" id="y1" placeholder="${texts.y1Placeholder}" value="0">
                <input type="number" id="x2" placeholder="${texts.x2Placeholder}" value="3">
                <input type="number" id="y2" placeholder="${texts.y2Placeholder}" value="4">
            `;
            break;
        case 'parallelogram':
            inputSection.innerHTML = `
                <input type="number" id="base" placeholder="${texts.basePlaceholder}" value="5">
                <input type="number" id="height" placeholder="${texts.heightPlaceholder}" value="4">
            `;
            break;
        case 'rectangle':
            inputSection.innerHTML = `
                <input type="number" id="length" placeholder="${texts.lengthPlaceholder}" value="5">
                <input type="number" id="width" placeholder="${texts.widthPlaceholder}" value="3">
            `;
            break;
        case 'polygon':
            inputSection.innerHTML = `
                <input type="number" id="sides" placeholder="${texts.sidesPlaceholder}" min="3" max="14" value="5">
                <input type="number" id="sideLength" placeholder="${texts.sideLengthPlaceholder}" value="4">
            `;
            break;
        case 'pythagorean':
            inputSection.innerHTML = `
                <input type="number" id="a" placeholder="${texts.aPlaceholder}" value="3">
                <input type="number" id="b" placeholder="${texts.bPlaceholder}" value="4">
            `;
            break;
        case 'rhombus':
            inputSection.innerHTML = `
                <input type="number" id="diagonal1" placeholder="${texts.diagonal1Placeholder}" value="6">
                <input type="number" id="diagonal2" placeholder="${texts.diagonal2Placeholder}" value="8">
            `;
            break;
        case 'slope':
            inputSection.innerHTML = `
                <input type="number" id="x1" placeholder="${texts.x1Placeholder}" value="0">
                <input type="number" id="y1" placeholder="${texts.y1Placeholder}" value="0">
                <input type="number" id="x2" placeholder="${texts.x2Placeholder}" value="3">
                <input type="number" id="y2" placeholder="${texts.y2Placeholder}" value="4">
            `;
            break;
        case 'square':
            inputSection.innerHTML = `<input type="number" id="side" placeholder="${texts.sidePlaceholder}" value="5">`;
            break;
        case 'stadium':
            inputSection.innerHTML = `
                <input type="number" id="length" placeholder="${texts.lengthPlaceholder}" value="10">
                <input type="number" id="width" placeholder="${texts.widthPlaceholder}" value="5">
            `;
            break;
        case 'lawOfCosines':
            inputSection.innerHTML = `
                <input type="number" id="a" placeholder="${texts.aPlaceholder}" value="3">
                <input type="number" id="b" placeholder="${texts.bPlaceholder}" value="4">
                <input type="number" id="c" placeholder="${texts.cPlaceholder}" value="5">
            `;
            break;
        case 'lawOfSines':
            inputSection.innerHTML = `
                <input type="number" id="a" placeholder="${texts.aPlaceholder}" value="3">
                <input type="number" id="A" placeholder="${texts.APlaceholder}" value="30">
                <input type="number" id="b" placeholder="${texts.bPlaceholder}" value="4">
                <input type="number" id="B" placeholder="${texts.BPlaceholder}" value="45">
            `;
            break;
        case 'triangleEquilateral':
            inputSection.innerHTML = `<input type="number" id="side" placeholder="${texts.sidePlaceholder}" value="5">`;
            break;
        case 'triangleIsosceles':
            inputSection.innerHTML = `
                <input type="number" id="base" placeholder="${texts.basePlaceholder}" value="6">
                <input type="number" id="leg" placeholder="${texts.legPlaceholder}" value="5">
            `;
            break;
        case 'triangleRight':
            inputSection.innerHTML = `
                <input type="number" id="base" placeholder="${texts.basePlaceholder}" value="3">
                <input type="number" id="height" placeholder="${texts.heightPlaceholder}" value="4">
            `;
            break;
    }
}

function calculate() {
    const shape = document.getElementById('shapeSelect').value;
    let result = '';

    switch (shape) {
        case 'annulus':
            const outerRadius = parseFloat(document.getElementById('outerRadius').value);
            const innerRadius = parseFloat(document.getElementById('innerRadius').value);
            const annulusArea = Math.PI * (outerRadius * outerRadius - innerRadius * innerRadius);
            result = `${texts.areaText}: ${annulusArea.toFixed(2)}`;
            break;
        case 'circle':
            const radius = parseFloat(document.getElementById('radius').value);
            const circleArea = Math.PI * radius * radius;
            result = `${texts.areaText}: ${circleArea.toFixed(2)}`;
            break;
        case 'distance2d':
            const x1 = parseFloat(document.getElementById('x1').value);
            const y1 = parseFloat(document.getElementById('y1').value);
            const x2 = parseFloat(document.getElementById('x2').value);
            const y2 = parseFloat(document.getElementById('y2').value);
            const distance = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
            result = `${texts.distanceText}: ${distance.toFixed(2)}`;
            break;
        case 'parallelogram':
            const base = parseFloat(document.getElementById('base').value);
            const height = parseFloat(document.getElementById('height').value);
            const parallelogramArea = base * height;
            result = `${texts.areaText}: ${parallelogramArea.toFixed(2)}`;
            break;
        case 'rectangle':
            const length = parseFloat(document.getElementById('length').value);
            const width = parseFloat(document.getElementById('width').value);
            const rectangleArea = length * width;
            result = `${texts.areaText}: ${rectangleArea.toFixed(2)}`;
            break;
        case 'polygon':
            const sides = parseInt(document.getElementById('sides').value);
            const sideLength = parseFloat(document.getElementById('sideLength').value);
            const polygonArea = (sides * Math.pow(sideLength, 2)) / (4 * Math.tan(Math.PI / sides));
            result = `${texts.areaText}: ${polygonArea.toFixed(2)}`;
            break;
        case 'pythagorean':
            const a = parseFloat(document.getElementById('a').value);
            const b = parseFloat(document.getElementById('b').value);
            const c = Math.sqrt(a * a + b * b);
            result = `${texts.hypotenuseText}: ${c.toFixed(2)}`;
            break;
        case 'rhombus':
            const diagonal1 = parseFloat(document.getElementById('diagonal1').value);
            const diagonal2 = parseFloat(document.getElementById('diagonal2').value);
            const rhombusArea = (diagonal1 * diagonal2) / 2;
            result = `${texts.areaText}: ${rhombusArea.toFixed(2)}`;
            break;
        case 'slope':
            const slopeX1 = parseFloat(document.getElementById('x1').value);
            const slopeY1 = parseFloat(document.getElementById('y1').value);
            const slopeX2 = parseFloat(document.getElementById('x2').value);
            const slopeY2 = parseFloat(document.getElementById('y2').value);
            const slope = (slopeY2 - slopeY1) / (slopeX2 - slopeX1);
            result = `${texts.slopeText}: ${slope.toFixed(2)}`;
            break;
        case 'square':
            const side = parseFloat(document.getElementById('side').value);
            const squareArea = side * side;
            result = `${texts.areaText}: ${squareArea.toFixed(2)}`;
            break;
        case 'stadium':
            const stadiumLength = parseFloat(document.getElementById('length').value);
            const stadiumWidth = parseFloat(document.getElementById('width').value);
            const stadiumArea = stadiumLength * stadiumWidth + Math.PI * Math.pow(stadiumWidth / 2, 2);
            result = `${texts.areaText}: ${stadiumArea.toFixed(2)}`;
            break;
        case 'lawOfCosines':
            const cosA = parseFloat(document.getElementById('a').value);
            const cosB = parseFloat(document.getElementById('b').value);
            const cosC = parseFloat(document.getElementById('c').value);
            const cosAngle = Math.acos((cosA * cosA + cosB * cosB - cosC * cosC) / (2 * cosA * cosB)) * (180 / Math.PI);
            result = `${texts.angleText}: ${cosAngle.toFixed(2)}°`;
            break;
        case 'lawOfSines':
            const sinA = parseFloat(document.getElementById('a').value);
            const sinAngleA = parseFloat(document.getElementById('A').value) * (Math.PI / 180);
            const sinB = parseFloat(document.getElementById('b').value);
            const sinAngleB = parseFloat(document.getElementById('B').value) * (Math.PI / 180);
            const sinC = (sinA * Math.sin(sinAngleB)) / Math.sin(sinAngleA);
            result = `${texts.sideCText}: ${sinC.toFixed(2)}`;
            break;
case 'triangleEquilateral':
            const eqSide = parseFloat(document.getElementById('side').value);
            const eqArea = (Math.sqrt(3) / 4) * eqSide * eqSide;
            result = `${texts.areaText}: ${eqArea.toFixed(2)}`;
            break;
        case 'triangleIsosceles':
            const isoBase = parseFloat(document.getElementById('base').value);
            const isoLeg = parseFloat(document.getElementById('leg').value);
            const isoHeight = Math.sqrt(isoLeg * isoLeg - (isoBase * isoBase / 4));
            const isoArea = (isoBase * isoHeight) / 2;
            result = `${texts.areaText}: ${isoArea.toFixed(2)}`;
            break;
        case 'triangleRight':
            const rightBase = parseFloat(document.getElementById('base').value);
            const rightHeight = parseFloat(document.getElementById('height').value);
            const rightArea = (rightBase * rightHeight) / 2;
            result = `${texts.areaText}: ${rightArea.toFixed(2)}`;
            break;
    }

    document.getElementById('resultText').textContent = result;
}

function solveEquation() {
    const equation = document.getElementById('equationInput').value;
    try {
        const result = eval(equation);
        document.getElementById('equationResult').textContent = `${texts.resultText}: ${result}`;
    } catch (error) {
        document.getElementById('equationResult').textContent = texts.invalidEquation;
    }
}

window.onload = init;