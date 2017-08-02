#Write a program that uses these bounds and bisection search (for more info check out the Wikipedia page on bisection search) to find the smallest monthly payment to the cent 
#(no more multiples of $10) such that we can pay off the debt within a year. Try it out with large inputs, and notice how fast it is (try the same large inputs in your solution to Problem 2 to compare!). 
#Produce the same return value as you did in Problem 2.

def calculateLowestPayment(balance, annualInterestRate):
    months = 12
    epsilon = 0.01
    
    monthlyInterestRate = annualInterestRate / 12.0
    
    # fixed payment bounds
    fixedMonthlyPaymentLow = balance / months
    fixedMonthlyPaymentHigh = (balance * (1 + monthlyInterestRate)**months) / 12.0
    
    fixedMonthlyPayment = 0
    
    while True:    
        previousBalance = balance
        fixedMonthlyPayment = (fixedMonthlyPaymentLow + fixedMonthlyPaymentHigh) / 2.0
        for m in range(months):
            monthlyUnpaidBalance = previousBalance - fixedMonthlyPayment
            updatedBalanceEachMonth = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
            previousBalance = updatedBalanceEachMonth
    
    #    print('Fixed Monthly Payment: {} Remaining Balance: {}'.format(round(fixedMonthlyPayment, 2), round(previousBalance, 2)))
        if abs(previousBalance) < epsilon:
            break
        elif previousBalance > epsilon:
            fixedMonthlyPaymentLow = fixedMonthlyPayment
        elif previousBalance < -epsilon:
            fixedMonthlyPaymentHigh = fixedMonthlyPayment
        else:
            break
    return fixedMonthlyPayment

    
print("Lowest Payment: " + str(round(calculateLowestPayment(3329, 0.2), 2)))