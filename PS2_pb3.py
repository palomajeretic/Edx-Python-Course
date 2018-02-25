def yearly_unpaid_balance(balance, annualInterestRate, monthlyPaymentRate):
    for m in range(12):
        balance -= monthlyPaymentRate
        balance += balance*annualInterestRate/12
    return balance

monthlyPayment_lb=balance/12
monthlyPayment_ub=balance*(1+annualInterestRate/12)**12/12

monthlyPaymentRate=(monthlyPayment_lb+monthlyPayment_ub)/2


while abs(yearly_unpaid_balance(balance, annualInterestRate, monthlyPaymentRate)) >0.01 :
    if yearly_unpaid_balance(balance, annualInterestRate, monthlyPaymentRate) >0.01:
        monthlyPayment_lb=monthlyPaymentRate
    else:
        monthlyPayment_ub=monthlyPaymentRate
    monthlyPaymentRate=(monthlyPayment_lb+monthlyPayment_ub)/2
        
        
        
print(round(monthlyPaymentRate,2))