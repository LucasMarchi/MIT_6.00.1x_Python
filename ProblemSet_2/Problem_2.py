#Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. 
#By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

def calculateLowestPayment(balance, annualInterestRate):
    
    balance_aux = balance
    monthlyPayment = 0
    updatedBalance = balance
    monthlyInterestRate = (annualInterestRate) / 12.0
    
    while updatedBalance >= 0:
        updatedBalance = 0
        monthlyPayment += 10
        balance_aux = balance
        #print("monthlyPayment: " + str(monthlyPayment))
        for i in range(12):
            monthlyUnpaidBalance = balance_aux - (monthlyPayment)
            #print("monthlyUnpaidBalance: " + str(monthlyUnpaidBalance))
            balance_aux = (monthlyUnpaidBalance) + (monthlyInterestRate * monthlyUnpaidBalance)
            #print("balance_aux: " + str(balance_aux))
        updatedBalance = balance_aux
        #print("updatedBalance: " + str(updatedBalance))
    return monthlyPayment    
    
print("Lowest Payment: " + str(calculateLowestPayment(3329, 0.2)))