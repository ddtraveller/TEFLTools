let translations;
let gradebook = {
    students: [],
    assignments: [],
    grades: {},
    points: {}
};

function loadTranslations(data) {
    translations = data;
    document.getElementById('pageTitle').textContent = translations.pageTitle;
    document.getElementById('mainHeader').textContent = translations.mainHeader;
    document.getElementById('introText').textContent = translations.introText;
    document.getElementById('newGradebookBtn').textContent = translations.newGradebookBtn;
    document.getElementById('loadGradebookLabel').textContent = translations.loadGradebookLabel;
    document.getElementById('addStudentBtn').textContent = translations.addStudentBtn;
    document.getElementById('addAssignmentBtn').textContent = translations.addAssignmentBtn;
    document.getElementById('calculateAveragesBtn').textContent = translations.calculateAveragesBtn;
    document.getElementById('saveGradebookBtn').textContent = translations.saveGradebookBtn;
}

function setupInitialOptions() {
    document.getElementById('newGradebookBtn').addEventListener('click', createNewGradebook);
    document.getElementById('loadGradebookInput').addEventListener('change', loadGradebookFromCSV);
}

function createNewGradebook() {
    gradebook = { students: [], assignments: [], grades: {}, points: {} };
    showGradebookContent();
}

function loadGradebookFromCSV(event) {
    const file = event.target.files[0];
    const reader = new FileReader();
    reader.onload = function(e) {
        const csv = e.target.result;
        parseCSV(csv);
        showGradebookContent();
    };
    reader.readAsText(file);
}

function parseCSV(csv) {
    const lines = csv.split('\n');
    const headers = lines[0].split(',');
    gradebook.assignments = headers.slice(1, -2);
    gradebook.points = {};
    
    gradebook.assignments.forEach((assignment, index) => {
        gradebook.points[assignment] = parseInt(headers[index + 1 + gradebook.assignments.length]) || 10;
    });
    
    for (let i = 1; i < lines.length; i++) {
        const values = lines[i].split(',');
        const student = values[0];
        gradebook.students.push(student);
        gradebook.grades[student] = {};
        
        for (let j = 1; j <= gradebook.assignments.length; j++) {
            const assignment = gradebook.assignments[j-1];
            gradebook.grades[student][assignment] = values[j];
        }
    }
}

function showGradebookContent() {
    document.getElementById('initialOptions').style.display = 'none';
    document.getElementById('gradebookContent').style.display = 'block';
    setupGradebookOptions();
    updateGradebookTable();
}

function setupGradebookOptions() {
    document.getElementById('addStudentBtn').addEventListener('click', addStudent);
    document.getElementById('addAssignmentBtn').addEventListener('click', addAssignment);
    document.getElementById('calculateAveragesBtn').addEventListener('click', calculateAverages);
    document.getElementById('saveGradebookBtn').addEventListener('click', saveGradebookToCSV);
}

function addStudent() {
    const studentName = prompt(translations.addStudentPrompt);
    if (studentName && !gradebook.students.includes(studentName)) {
        gradebook.students.push(studentName);
        gradebook.grades[studentName] = {};
        updateGradebookTable();
    }
}

function addAssignment() {
    const assignmentName = prompt(translations.addAssignmentPrompt);
    if (assignmentName && !gradebook.assignments.includes(assignmentName)) {
        gradebook.assignments.push(assignmentName);
        gradebook.points[assignmentName] = 10;
        updateGradebookTable();
    }
}

function updateGradebookTable() {
    const table = document.getElementById('gradebookTable');
    table.innerHTML = '';

    // Header row
    const headerRow = table.insertRow();
    headerRow.insertCell().textContent = translations.studentHeader;
    gradebook.assignments.forEach(assignment => {
        const cell = headerRow.insertCell();
        cell.innerHTML = `${assignment}<br>(${gradebook.points[assignment]} ${translations.pointsLabel})`;
        cell.addEventListener('click', () => editPoints(assignment));
    });
    headerRow.insertCell().textContent = translations.averageHeader;

    // Student rows
    gradebook.students.forEach(student => {
        const row = table.insertRow();
        row.insertCell().textContent = student;
        gradebook.assignments.forEach(assignment => {
            const cell = row.insertCell();
            const grade = gradebook.grades[student][assignment] || '';
            cell.textContent = grade;
            cell.addEventListener('click', () => editGrade(student, assignment, cell));
        });
        row.insertCell(); // Empty cell for average (to be filled later)
    });
}

function editPoints(assignment) {
    const newPoints = prompt(`${translations.editPointsPrompt} ${assignment}`, gradebook.points[assignment]);
    if (newPoints !== null) {
        gradebook.points[assignment] = parseInt(newPoints) || 10;
        updateGradebookTable();
    }
}

function editGrade(student, assignment, cell) {
    const newGrade = prompt(`${translations.editGradePrompt} ${student} - ${assignment}`);
    if (newGrade !== null) {
        gradebook.grades[student][assignment] = newGrade;
        cell.textContent = newGrade;
    }
}

function calculateAverages() {
    const table = document.getElementById('gradebookTable');
    gradebook.students.forEach((student, index) => {
        let totalPoints = 0;
        let earnedPoints = 0;
        gradebook.assignments.forEach(assignment => {
            const grade = parseFloat(gradebook.grades[student][assignment]);
            const points = gradebook.points[assignment];
            if (!isNaN(grade)) {
                totalPoints += points;
                earnedPoints += (grade / 100) * points;
            }
        });
        const average = totalPoints > 0 ? (earnedPoints / totalPoints) * 100 : 0;
        table.rows[index + 1].cells[gradebook.assignments.length + 1].textContent = average.toFixed(2) + '%';
    });
}

function saveGradebookToCSV() {
    let csv = 'Student,' + gradebook.assignments.join(',') + ',' + translations.averageHeader + ',';
    csv += gradebook.assignments.map(assignment => `${assignment} ${translations.pointsLabel}`).join(',') + '\n';

    gradebook.students.forEach(student => {
        csv += student + ',';
        csv += gradebook.assignments.map(assignment => gradebook.grades[student][assignment] || '').join(',');
        
        // Calculate and add average
        let totalPoints = 0;
        let earnedPoints = 0;
        gradebook.assignments.forEach(assignment => {
            const grade = parseFloat(gradebook.grades[student][assignment]);
            const points = gradebook.points[assignment];
            if (!isNaN(grade)) {
                totalPoints += points;
                earnedPoints += (grade / 100) * points;
            }
        });
        const average = totalPoints > 0 ? (earnedPoints / totalPoints) * 100 : 0;
        csv += ',' + average.toFixed(2) + '%,';

        // Add point values
        csv += gradebook.assignments.map(assignment => gradebook.points[assignment]).join(',');
        csv += '\n';
    });

    const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
    const link = document.createElement('a');
    if (link.download !== undefined) {
        const url = URL.createObjectURL(blob);
        link.setAttribute('href', url);
        link.setAttribute('download', 'gradebook.csv');
        link.style.visibility = 'hidden';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }
}