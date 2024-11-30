let balance = 0;
let expenditure = 0;

function credit() {
    let amount = parseFloat(document.getElementById('transactionAmount').value);
    if (!isNaN(amount) && amount > 0) {
        balance += amount;
        updateBalance();
    }
}

function debit() {
    let amount = parseFloat(document.getElementById('transactionAmount').value);
    if (!isNaN(amount) && amount > 0 && amount <= balance) {
        balance -= amount;
        expenditure += amount;
        updateBalance();
        updateExpenditure();
    }
}

function updateBalance() {
    document.getElementById('balance').textContent = `Your Account Balance is: Rs. ${balance}`;
}

function updateExpenditure() {
    document.getElementById('expenditure').textContent = `Your Total Expenditure is: Rs. ${expenditure}`;
}