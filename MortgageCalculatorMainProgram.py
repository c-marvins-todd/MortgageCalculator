#Mortgage Calculator by Catherine Todd

#Requirements and goals in 'MortgageCalculatorRequirements.txt'

#Variables

mortgageAmount=0.00#Mortage Amount
interestRate=0.00 #Interest Rate
paymentAmount=0.00 #Monthly payment required
surplusAmount=0.00 #Any Surplus Payment made in a month
principleAmount=0.00 #Principle of Mortgage
principlePercent=0.00 #Percent of Principle paid off by required monthly payments
loanMonth=0.00 #The month we are calculating
principlePaid=0.00 #The amount of the principle paid
interestAmount=0.00 #The amount of interest of the loan
interestPaid=0.00 #Amount of interest paid
interstRemaining=0.00 #The remaining amount of interest due
paidTotal=0.00 #the total amount of the mortgage paid
userChoice=0 #filler varibale for user's choices as they use app

#Main Function
def main():
    intro()
    userChoice= menu()
    

#Intro
def intro():
    print("Welcome to the Mortgage Calculator Program!\n")
    
#Menu
def menu():
    print("Select an option from the menu by entering the number.\n")
    print("Menu Options:\n")
    print("1.)View My Mortgage Summary\n")
    print("2.)Edit My Mortgage Details\n")
    print("3.)Quit\n")
    i= int(input('Please enter the number corresponsing to your choice.'))
    return i
    

#Replay Menu
def replayMenu():
    print("Would you like to...\n")
    print("1.)Go Back to the main menu")
    print("2.)Quit the program")




