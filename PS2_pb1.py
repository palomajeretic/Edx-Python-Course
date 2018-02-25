for m in range(12):
    balance -= balance*monthlyPaymentRate
    balance+= balance*annualInterestRate/12

balance=round(balance,2)

print(balance)