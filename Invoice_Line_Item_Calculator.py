# Course CIS261 Week 6 lab 1 Invoice line item calculator
# Emma Kailani Triad 05/12/2025

def get_price():
    while True:
        try:
            price = float(input('Enter Price: '))
            return price
        except ValueError:
            print('Invalid price, please try again.' )

    
def get_quantity():
    while True:
        try:
            quantity = float(input('Enter quantity: '))
            return quantity
        except ValueError:
            print('Invalid number, please try again.' )

#def main():
    #print("The Invoice Line TIem Calcuator\n")
    
    #TODO: implement main program loop
    # get price and quantity from user
    # calcualtor total
    # display results
    # ask if user wants to enter another line item
    # contunie until user chooses to exit

    #elif command == "exit":
        #print("Bye!")
        #break

# if __name__ == "__main__":
    #main()



