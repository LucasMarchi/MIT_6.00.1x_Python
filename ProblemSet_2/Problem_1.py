#Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

def calculateBalance(balance, annualInterestRate, monthlyPaymentRate):
    
    for i in range(12):
        #print("Balance: " + str(balance))
        minimumPayment = balance * monthlyPaymentRate
        #print("minimumPayment: " + str(minimumPayment))
        unpaidBalance = balance - minimumPayment
        #print("unpaidBalance: " + str(unpaidBalance))
        interest = annualInterestRate/12.0 * unpaidBalance
        #print("interest: " + str(interest))
        balance = unpaidBalance + interest
    
    return balance    
    
print("Remaining balance: " + str(round(calculateBalance(5000, 0.18, 0.02), 2)))