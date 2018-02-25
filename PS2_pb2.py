def yearly_unpaid_balance(balance, annualInterestRate, monthlyPaymentRate):
    for m in range(12):
        balance -= monthlyPaymentRate
        balance += balance*annualInterestRate/12
    return balance

monthlyPaymentRate=0

while yearly_unpaid_balance(balance, annualInterestRate, monthlyPaymentRate)>0:
    monthlyPaymentRate+=10

print(monthlyPaymentRate)