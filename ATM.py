class ATM:
    def __init__(self, pin, cardnumber):
        self.pin=pin
        self.cardnumber=cardnumber

    
    def balanceinquiry(self):
        print("your balance is: $10000")

    def cashwidthdrawal(self, amount):
        new_amount = 10000-amount
        print("Your widthdrawal: " + str(amount) + " Your Remaining balance is: ", str(new_amount))

def main():
        name= input("What is your name bro? ")
        print("Hello, " + name)
        cardnumber= input("Insert your card number: ")
        pin = input("Enter your pin: ")
        new_user = ATM(cardnumber, pin)

        print("Choose your activity")
        print("1. Balance Inquiry")
        print("2. Cash Widthdrawal")
        activity= int(input("Enter Activity choice: "))

        if (activity == 1):
            new_user.balanceinquiry()
        elif (activity == 2):
            amount = int(input("Enter the amount: "))
            new_user.cashwidthdrawal(amount)
        else:
            print("Enter a valid number")

if __name__ == "__main__":
    main()


