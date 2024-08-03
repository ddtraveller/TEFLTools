// roster.js
let studentRoster = [];
let teacherRoster = [];
let classes = [];
let texts = {};

function loadJSON(callback) {
    var xhr = new XMLHttpRequest();
    xhr.overrideMimeType("application/json");
    xhr.open('GET', 'https://tl-web.s3.us-west-2.amazonaws.com/roster/roster.json', true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4) {
            if (xhr.status == "200") {
                console.log("JSON data loaded successfully");
                callback(null, xhr.responseText);
            } else {
                console.error("Failed to load roster.json: " + xhr.status);
                callback(new Error("Failed to load roster.json: " + xhr.status), null);
            }
        }
    };
    xhr.send(null);
}

function searchStudents(query) {
    if (!query.trim()) return studentRoster;
    query = query.toLowerCase().trim();
    return studentRoster.filter(student => {
        const fullName = `${student.firstName} ${student.lastName}`.toLowerCase();
        return fullName.includes(query);
    });
}

function updateStudentRosterDisplay(studentsToDisplay = studentRoster) {
    const tbody = document.querySelector('#studentRosterTable tbody');
    if (!tbody) {
        console.error("Student table body not found");
        return;
    }
    
    tbody.innerHTML = '';
    
    if (studentsToDisplay.length === 0) {
        const row = tbody.insertRow();
        row.innerHTML = '<td colspan="4">No matching students found</td>';
        return;
    }
    
    studentsToDisplay.forEach(student => {
        const row = tbody.insertRow();
        row.innerHTML = `
            <td>${student.lastName}, ${student.firstName}</td>
            <td>${student.birthDate}</td>
            <td>${student.class || 'Unassigned'}</td>
            <td>
                <button onclick="editStudentPrompt(${student.id})">${texts.editBtn || 'Edit'}</button>
                <button onclick="removeStudent(${student.id})">${texts.removeBtn || 'Remove'}</button>
                <button onclick="changeClassPrompt(${student.id}, 'student')">Change Class</button>
            </td>
        `;
    });
}

function updateTeacherRosterDisplay() {
    const tbody = document.querySelector('#teacherRosterTable tbody');
    if (!tbody) {
        console.error("Teacher table body not found");
        return;
    }
    
    tbody.innerHTML = '';
    
    if (teacherRoster.length === 0) {
        const row = tbody.insertRow();
        row.innerHTML = '<td colspan="4">No teachers found</td>';
        return;
    }
    
    teacherRoster.forEach(teacher => {
        const row = tbody.insertRow();
        row.innerHTML = `
            <td>${teacher.lastName}, ${teacher.firstName}</td>
            <td>${teacher.subject}</td>
            <td>${teacher.class || 'Unassigned'}</td>
            <td>
                <button onclick="editTeacherPrompt(${teacher.id})">Edit</button>
                <button onclick="removeTeacher(${teacher.id})">Remove</button>
                <button onclick="changeClassPrompt(${teacher.id}, 'teacher')">Change Class</button>
            </td>
        `;
    });
}

function handleSearch() {
    const searchInput = document.getElementById('searchInput');
    if (!searchInput) {
        console.error("Search input not found");
        return;
    }
    
    const searchQuery = searchInput.value;
    console.log("Searching for:", searchQuery);
    
    const searchResults = searchStudents(searchQuery);
    console.log("Search results:", searchResults);
    
    updateStudentRosterDisplay(searchResults);
}

function loadJSON(callback) {
    var xhr = new XMLHttpRequest();
    xhr.overrideMimeType("application/json");
    xhr.open('GET', 'https://tl-web.s3.us-west-2.amazonaws.com/roster/roster.json', true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4) {
            if (xhr.status == "200") {
                console.log("JSON data loaded successfully");
                callback(null, xhr.responseText);
            } else {
                console.error("Failed to load roster.json: " + xhr.status);
                callback(new Error("Failed to load roster.json: " + xhr.status), null);
            }
        }
    };
    xhr.send(null);
}

function init() {
    loadJSON((err, data) => {
        if (err) {
            console.error("Error loading text content:", err);
            return;
        }
        texts = JSON.parse(data);
        updatePageText();
        initializeRosters();
        
        const searchInput = document.getElementById('searchInput');
        if (searchInput) {
            searchInput.addEventListener('input', handleSearch);
        } else {
            console.error("Search input not found");
        }
        
        document.getElementById('addStudentBtn').addEventListener('click', addStudentPrompt);
        document.getElementById('addTeacherBtn').addEventListener('click', addTeacherPrompt);
        document.getElementById('createClassesBtn').addEventListener('click', createClasses);
        document.getElementById('saveToFileBtn').addEventListener('click', saveToFile);
        document.getElementById('loadFileBtn').addEventListener('click', loadFromFile);
        document.getElementById('fileInput').addEventListener('change', handleFileSelect);
        document.getElementById('toggleInstructionsBtn').addEventListener('click', toggleInstructions);
        
    });
}

function updatePageText() {
    document.title = texts.pageTitle;
    document.getElementById('mainHeader').textContent = texts.mainHeader;
    document.getElementById('addStudentBtn').textContent = texts.addStudentBtn;
    document.getElementById('addTeacherBtn').textContent = texts.addTeacherBtn;
    document.getElementById('createClassesBtn').textContent = texts.createClassesBtn;
    document.getElementById('saveToFileBtn').textContent = texts.saveToFileBtn;
    document.getElementById('loadFileBtn').textContent = texts.loadFileBtn;
    document.getElementById('currentStudentRosterHeader').textContent = texts.currentStudentRosterHeader;
    document.getElementById('currentTeacherRosterHeader').textContent = texts.currentTeacherRosterHeader;
    document.getElementById('toggleInstructionsBtn').textContent = texts.prompts.toggleInstructionsBtn;
}

function toggleInstructions() {
    const instructionsSection = document.getElementById('instructionsSection');
    const toggleButton = document.getElementById('toggleInstructionsBtn');
    if (instructionsSection.style.display === 'none' || instructionsSection.style.display === '') {
        instructionsSection.style.display = 'block';
        toggleButton.textContent = 'Hide Instructions/Subar Orientasaun';
    } else {
        instructionsSection.style.display = 'none';
        toggleButton.textContent = 'Show Instructions/Hatudu Orientasaun';
    }
}

function addStudent(firstName, lastName, birthDate) {
    const student = {
        id: Date.now(),
        firstName: firstName,
        lastName: lastName,
        birthDate: birthDate
    };
    studentRoster.push(student);
    updateStudentRosterDisplay();
}

function addTeacher(firstName, lastName, subject) {
    const teacher = {
        id: Date.now(),
        firstName: firstName,
        lastName: lastName,
        subject: subject
    };
    teacherRoster.push(teacher);
    updateTeacherRosterDisplay();
}

function editStudent(id, firstName, lastName, birthDate) {
    const index = studentRoster.findIndex(student => student.id === id);
    if (index !== -1) {
        studentRoster[index] = {
            ...studentRoster[index],
            firstName: firstName,
            lastName: lastName,
            birthDate: birthDate
        };
        updateStudentRosterDisplay();
    }
}

function editTeacher(id, firstName, lastName, subject) {
    const index = teacherRoster.findIndex(teacher => teacher.id === id);
    if (index !== -1) {
        teacherRoster[index] = {
            ...teacherRoster[index],
            firstName: firstName,
            lastName: lastName,
            subject: subject
        };
        updateTeacherRosterDisplay();
    }
}

function removeStudent(id) {
    studentRoster = studentRoster.filter(student => student.id !== id);
    updateStudentRosterDisplay();
}

function removeTeacher(id) {
    teacherRoster = teacherRoster.filter(teacher => teacher.id !== id);
    updateTeacherRosterDisplay();
}

function addStudentPrompt() {
    const firstName = prompt(texts.prompts.firstName);
    const lastName = prompt(texts.prompts.lastName);
    const birthDate = prompt(texts.prompts.birthDate);
    if (firstName && lastName && birthDate) {
        addStudent(firstName, lastName, birthDate);
    }
}

function addTeacherPrompt() {
    const firstName = prompt("Enter teacher's first name:");
    const lastName = prompt("Enter teacher's last name:");
    const subject = prompt("Enter teacher's subject:");
    if (firstName && lastName && subject) {
        addTeacher(firstName, lastName, subject);
    }
}

function editStudentPrompt(id) {
    const student = studentRoster.find(s => s.id === id);
    if (student) {
        const firstName = prompt("Enter new first name:", student.firstName);
        const lastName = prompt("Enter new last name:", student.lastName);
        const birthDate = prompt("Enter new birth date (YYYY-MM-DD):", student.birthDate);
        if (firstName && lastName && birthDate) {
            editStudent(id, firstName, lastName, birthDate);
        }
    }
}

function editTeacherPrompt(id) {
    const teacher = teacherRoster.find(t => t.id === id);
    if (teacher) {
        const firstName = prompt("Enter new first name:", teacher.firstName);
        const lastName = prompt("Enter new last name:", teacher.lastName);
        const subject = prompt("Enter new subject:", teacher.subject);
        if (firstName && lastName && subject) {
            editTeacher(id, firstName, lastName, subject);
        }
    }
}

function createClasses() {
    if (studentRoster.length === 0 || teacherRoster.length === 0) {
        alert("Please add students and teachers before creating classes.");
        return;
    }

    const studentsPerClass = Math.ceil(studentRoster.length / teacherRoster.length);
    classes = [];

    for (let i = 0; i < teacherRoster.length; i++) {
        const classStudents = studentRoster.slice(i * studentsPerClass, (i + 1) * studentsPerClass);
        const className = `Class ${i + 1}`;
        classes.push({
            name: className,
            teacher: teacherRoster[i],
            students: classStudents
        });

        teacherRoster[i].class = className;
        classStudents.forEach(student => student.class = className);
    }

    updateStudentRosterDisplay();
    updateTeacherRosterDisplay();
    displayClasses();
}

function displayClasses() {
    const classesContainer = document.getElementById('classesContainer');
    classesContainer.innerHTML = '<h2>Classes</h2>';

    classes.forEach(cls => {
        const classDiv = document.createElement('div');
        classDiv.innerHTML = `
            <h3>${cls.name}</h3>
            <p>Teacher: ${cls.teacher.lastName}, ${cls.teacher.firstName}</p>
            <p>Students:</p>
            <ul>
                ${cls.students.map(student => `<li>${student.lastName}, ${student.firstName}</li>`).join('')}
            </ul>
        `;
        classesContainer.appendChild(classDiv);
    });
}

function changeClassPrompt(id, type) {
    const person = type === 'student' ? studentRoster.find(s => s.id === id) : teacherRoster.find(t => t.id === id);
    if (!person) return;

    const newClass = prompt(`Enter new class for ${person.firstName} ${person.lastName}:`, person.class || '');
    if (newClass !== null) {
        person.class = newClass || 'Unassigned';
        if (type === 'student') {
            updateStudentRosterDisplay();
        } else {
            updateTeacherRosterDisplay();
        }
        updateClasses();
    }
}

function updateClasses() {
    classes = [];
    const classMap = new Map();

    studentRoster.forEach(student => {
        if (student.class && student.class !== 'Unassigned') {
            if (!classMap.has(student.class)) {
                classMap.set(student.class, { name: student.class, teacher: null, students: [] });
            }
            classMap.get(student.class).students.push(student);
        }
    });

    teacherRoster.forEach(teacher => {
        if (teacher.class && teacher.class !== 'Unassigned') {
            if (classMap.has(teacher.class)) {
                classMap.get(teacher.class).teacher = teacher;
            } else {
                classMap.set(teacher.class, { name: teacher.class, teacher: teacher, students: [] });
            }
        }
    });

    classes = Array.from(classMap.values());
    displayClasses();
}

function saveToFile() {
    const data = {
        students: studentRoster,
        teachers: teacherRoster,
        classes: classes
    };
    const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'school_roster.json';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}

function initializeRosters() {
    // Sample data for testing
    studentRoster = [
        {id: 1, firstName: 'John', lastName: 'Doe', birthDate: '2000-01-01'},
        {id: 2, firstName: 'Jane', lastName: 'Smith', birthDate: '2001-02-15'},
        {id: 3, firstName: 'Bob', lastName: 'Johnson', birthDate: '1999-11-30'}
    ];
    teacherRoster = [
        {id: 1, firstName: 'Alice', lastName: 'Brown', subject: 'Math'},
        {id: 2, firstName: 'Charlie', lastName: 'Davis', subject: 'Science'}
    ];
    updateStudentRosterDisplay();
    updateTeacherRosterDisplay();
}

function loadFromFile() {
    document.getElementById('fileInput').click();
}

function handleFileSelect(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            try {
                const data = JSON.parse(e.target.result);
                if (validateLoadedData(data)) {
                    studentRoster = data.students || [];
                    teacherRoster = data.teachers || [];
                    classes = data.classes || [];
                    updateStudentRosterDisplay();
                    updateTeacherRosterDisplay();
                    displayClasses();
                    alert("File loaded successfully!");
                } else {
                    alert("Invalid file format. Please use a correctly formatted JSON file.");
                }
            } catch (error) {
                console.error("Error parsing JSON file:", error);
                alert("Error loading file. Please make sure it's a valid JSON file.");
            }
        };
        reader.readAsText(file);
    }
}

function validateLoadedData(data) {
    // Basic validation, you can expand this as needed
    return data && (Array.isArray(data.students) || Array.isArray(data.teachers));
}

window.onload = init;