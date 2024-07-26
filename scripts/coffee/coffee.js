document.getElementById('calculateBtn').addEventListener('click', calculateProfit);

function calculateProfit() {
    const drinkSize = parseFloat(document.getElementById('drinkSize').value) || 0;
    const ingredientCost = parseFloat(document.getElementById('ingredientCost').value) || 0;
    const laborCost = parseFloat(document.getElementById('laborCost').value) || 0;
    const overheadCost = parseFloat(document.getElementById('overheadCost').value) || 0;
    const sellingPrice = parseFloat(document.getElementById('sellingPrice').value) || 0;

    const totalCost = ingredientCost + laborCost + overheadCost;
    const profit = sellingPrice - totalCost;
    const profitMargin = (profit / sellingPrice) * 100;

    document.getElementById('totalCost').textContent = totalCost.toFixed(2);
    document.getElementById('profit').textContent = profit.toFixed(2);
    document.getElementById('profitMargin').textContent = profitMargin.toFixed(2);
}