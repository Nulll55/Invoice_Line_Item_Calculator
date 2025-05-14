# Course CIS261 Week 6 lab 1 Invoice line item calculator
# Emma Kailani Tirado 05/12/2025

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
            quantity = int(input('Enter quantity: '))
            return quantity
        except ValueError:
            print('Invalid number, please try again.' )


def display_info(price, quantity, total):
    print(f'\nPRICE:    {price: .2f}')
    print(f'QUANTITY:   {quantity}')
    print(f'TOTAL:      {total: .2f}')

def main():
    print("The Invoice Line TIem Calcuator\n")
    answer = "y"
    while answer.lower() =="y":
        price = get_price
        quantity = get_quantity
        total = price * quantity
        display_info(price, quantity, total)
        answer = input("Enter another line item? (y/n): ")
        print()
    else:
        print("Bye!")

if __name__ == "__main__":
    main()



