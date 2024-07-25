let translations;

function loadTranslations(data) {
    translations = data;
    // Set text content for various elements
    document.getElementById('pageTitle').textContent = translations.pageTitle;
    document.getElementById('mainHeader').textContent = translations.mainHeader;
    document.getElementById('introText').textContent = translations.introText;
    document.getElementById('incomeLabel').textContent = translations.incomeLabel;
    document.getElementById('calculateButton').textContent = translations.calculateButton;
    document.getElementById('resultsHeader').textContent = translations.resultsHeader;
    document.getElementById('projectionHeader').textContent = translations.projectionHeader;
    document.getElementById('investmentInputsHeader').textContent = translations.investmentInputsHeader;
    document.getElementById('savingsLabel').textContent = translations.savingsLabel;
    document.getElementById('savingsRateLabel').textContent = translations.rateLabel;
    document.getElementById('realEstateLabel').textContent = translations.realEstateLabel;
    document.getElementById('realEstateRateLabel').textContent = translations.rateLabel;
    document.getElementById('stocksLabel').textContent = translations.stocksLabel;
    document.getElementById('stocksRateLabel').textContent = translations.rateLabel;

    // Add these lines to set the text for the new buttons
    document.getElementById('loadBudgetBtn').textContent = translations.loadBudgetBtn;
    document.getElementById('saveBudgetBtn').textContent = translations.saveBudgetBtn;

    // Set default rates
    document.getElementById('savingsRate').value = translations.defaultSavingsRate;
    document.getElementById('realEstateRate').value = translations.defaultRealEstateRate;
    document.getElementById('stocksRate').value = translations.defaultStocksRate;
}

function setupFileOptions() {
    document.getElementById('loadBudgetBtn').addEventListener('click', () => {
        document.getElementById('loadBudgetInput').click();
    });
    document.getElementById('loadBudgetInput').addEventListener('change', loadBudgetFromCSV);
    document.getElementById('saveBudgetBtn').addEventListener('click', saveBudgetToCSV);
}

function setupExpenseInputs(categories) {
    const container = document.getElementById('expenseInputs');
    categories.forEach(category => {
        const div = document.createElement('div');
        div.className = 'input-group';
        div.innerHTML = `
            <label for="${category}">${translations[category]}</label>
            <input type="number" id="${category}" required>
        `;
        container.appendChild(div);
    });

    document.getElementById('calculateButton').addEventListener('click', calculateBudget);
}

function calculateBudget() {
    const income = parseFloat(document.getElementById('income').value);
    const expenses = {};
    let totalExpenses = 0;

    translations.expenseCategories.forEach(category => {
        const amount = parseFloat(document.getElementById(category).value) || 0;
        expenses[category] = amount;
        totalExpenses += amount;
    });

    const balance = income - totalExpenses;

    const investments = {
        savings: parseFloat(document.getElementById('savings').value) || 0,
        realEstate: parseFloat(document.getElementById('realEstate').value) || 0,
        stocks: parseFloat(document.getElementById('stocks').value) || 0
    };

    const investmentRates = {
        savings: parseFloat(document.getElementById('savingsRate').value) / 100,
        realEstate: parseFloat(document.getElementById('realEstateRate').value) / 100,
        stocks: parseFloat(document.getElementById('stocksRate').value) / 100
    };

    displayResults(income, expenses, balance);
    createChart(expenses);
    displayProjections(investments, investmentRates);
}

function displayResults(income, expenses, balance) {
    const resultsDiv = document.getElementById('results');
    resultsDiv.style.display = 'block';

    const balanceDiv = document.getElementById('balance');
    balanceDiv.textContent = `${translations.balanceLabel}: $${balance.toFixed(2)}`;
    balanceDiv.className = balance < 0 ? 'negative' : '';

    const balanceText = document.getElementById('balanceText');
    balanceText.textContent = balance < 0 ? translations.overspendingText : translations.savingsText;
}

function createChart(expenses) {
    const ctx = document.getElementById('budgetChart').getContext('2d');
    new Chart(ctx, {
        type: 'pie',
        data: {
            labels: Object.keys(expenses).map(key => translations[key]),
            datasets: [{
                data: Object.values(expenses),
                backgroundColor: [
                    '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40',
                    '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40'
                ]
            }]
        }
    });
}

function displayProjections(investments, rates) {
    const projectionYears = [1, 3, 20];
    const projectionsDiv = document.getElementById('projections');
    projectionsDiv.innerHTML = '';

    Object.entries(investments).forEach(([type, amount]) => {
        const rate = rates[type];
        const typeHeader = document.createElement('h4');
        typeHeader.textContent = translations[type];
        projectionsDiv.appendChild(typeHeader);

        projectionYears.forEach(years => {
            const projectedAmount = amount * Math.pow(1 + rate, years);
            const p = document.createElement('p');
            p.textContent = `${years} ${translations.years}: $${projectedAmount.toFixed(2)}`;
            projectionsDiv.appendChild(p);
        });
    });
}

function loadBudgetFromCSV(event) {
    const file = event.target.files[0];
    const reader = new FileReader();
    reader.onload = function(e) {
        const csv = e.target.result;
        const lines = csv.split('\n');
        const headers = lines[0].split(',');
        const values = lines[1].split(',');

        document.getElementById('income').value = values[0];

        translations.expenseCategories.forEach((category, index) => {
            document.getElementById(category).value = values[index + 1];
        });

        document.getElementById('savings').value = values[values.length - 6];
        document.getElementById('savingsRate').value = values[values.length - 5];
        document.getElementById('realEstate').value = values[values.length - 4];
        document.getElementById('realEstateRate').value = values[values.length - 3];
        document.getElementById('stocks').value = values[values.length - 2];
        document.getElementById('stocksRate').value = values[values.length - 1];

        calculateBudget();
    };
    reader.readAsText(file);
}

function saveBudgetToCSV() {
    let csv = 'Income,';
    csv += translations.expenseCategories.join(',') + ',';
    csv += 'Savings,SavingsRate,RealEstate,RealEstateRate,Stocks,StocksRate\n';

    csv += document.getElementById('income').value + ',';
    translations.expenseCategories.forEach(category => {
        csv += (document.getElementById(category).value || '0') + ',';
    });
    csv += document.getElementById('savings').value + ',';
    csv += document.getElementById('savingsRate').value + ',';
    csv += document.getElementById('realEstate').value + ',';
    csv += document.getElementById('realEstateRate').value + ',';
    csv += document.getElementById('stocks').value + ',';
    csv += document.getElementById('stocksRate').value;

    const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
    const link = document.createElement('a');
    if (link.download !== undefined) {
        const url = URL.createObjectURL(blob);
        link.setAttribute('href', url);
        link.setAttribute('download', 'budget.csv');
        link.style.visibility = 'hidden';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }
}

// Initial setup
fetch('translations.json')
    .then(response => response.json())
    .then(data => {
        loadTranslations(data);
        setupExpenseInputs(data.expenseCategories);
        setupFileOptions();
    })
    .catch(error => console.error('Error loading translations:', error));