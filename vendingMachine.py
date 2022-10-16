MACHINE_ITEMS = 6
MAX_QUANTITY_ITEMS = 50

def navItems():
    navItems = ['1. Hershey"s Chocolate(small) -- 10$', '2. Hershey"s Chocolate(Big) -- 25$', "3. Coco cola -- 40$",
                '4. Pepsi -- 35$', '5. Hot Cheetos -- 50$']

    for i in navItems:
        print(i)

hershey_small_amount = 10
hershey_big_amount = 25
coco_cola = 40
pepsi = 35
hot_cheetos = 50

item1 = "Hershey's Chocolate(small)"
item2 = "Hershey's Chocolate(Big)"
item3 = "Coco cola"
item4 = "Pepsi"
item5 = "Hot Cheetos"


def getting_user_data(user_data):
    if user_data.isdigit():
        user_data = int(user_data)
        if user_data < 0:
            print("Must be greater than 0")
        elif user_data >= MACHINE_ITEMS:
            print(f"Number must be below {MACHINE_ITEMS}")
        else:
            print("hi, Welcome")


def order(user_data, hershey_small_amount, item1, hershey_big_amount, item2, coco_cola, item3, pepsi, item4, hot_cheetos, item5):
    print('__________________________')
    if user_data == '1':
        print('You have selected: ' + item1)
        quantity = int(input("Enter quantity: "))
        if quantity > MAX_QUANTITY_ITEMS:
            print("Out of stock")
        elif quantity <= MAX_QUANTITY_ITEMS:
            print(item1, f'Amount: {quantity * hershey_small_amount}' + '$')

            def hershey_payment_small(quantity):
                paymentInput = int(input(f"Give the amount for {item1}: {quantity * hershey_small_amount}: "))
                finalAamount = quantity * hershey_small_amount

                if paymentInput < finalAamount:
                    print("Give the full amount.")
                elif paymentInput > finalAamount:
                    print("We dont give the change. pls enter proper amount.")
                else:
                    print("Here is your snack")

            hershey_payment_small(quantity)
    # ----------------------
    elif user_data == '2':
        print('You have selected: ' + item2)
        quantity = int(input("Enter quantity: "))
        if quantity > MAX_QUANTITY_ITEMS:
            print("Out of stock")
        elif quantity <= MAX_QUANTITY_ITEMS:
            print(item2, f'Amount: {quantity * hershey_big_amount}' + '$')

            def hershey_payment_big(quantity):
                paymentInput = int(input(f"Give the amount for {quantity * hershey_big_amount}: "))
                finalAamount = quantity * hershey_big_amount

                if paymentInput < finalAamount:
                    print("Give the full amount.")
                elif paymentInput > finalAamount:
                    print("We dont give the change. pls enter proper amount.")
                else:
                    print("Here is your snack")

            hershey_payment_big(quantity)

    # ----------------------
    elif user_data == '3':
        print('You have selected: ' + item3)
        quantity = int(input("Enter quantity: "))
        if quantity > MAX_QUANTITY_ITEMS:
            print("Out of stock")
        elif quantity <= MAX_QUANTITY_ITEMS:
            print(item3, f'Amount: {quantity * coco_cola}' + '$')

            def coco_cola_payment(quantity):
                paymentInput = int(input(f"Give the amount for {quantity * coco_cola}: "))
                finalAamount = quantity * coco_cola

                if paymentInput < finalAamount:
                    print("Give the full amount.")
                elif paymentInput > finalAamount:
                    print("We dont give the change. pls enter proper amount.")
                else:
                    print("Here is your snack")

            coco_cola_payment(quantity)
    # ----------------------
    elif user_data == '4':
        print('You have selected: ' + item4)
        quantity = int(input("Enter quantity: "))
        if quantity > MAX_QUANTITY_ITEMS:
            print("Out of stock")
        elif quantity <= MAX_QUANTITY_ITEMS:
            print(item4, f'Amount: {quantity * pepsi}' + '$')

            def pepsi_payment(quantity):
                paymentInput = int(input(f"Give the amount for {quantity * pepsi}: "))
                finalAamount = quantity * pepsi

                if paymentInput < finalAamount:
                    print("Give the full amount.")
                elif paymentInput > finalAamount:
                    print("We dont give the change. pls enter proper amount.")
                else:
                    print("Here is your snack")

            pepsi_payment(quantity)
    # ----------------------
    elif user_data == '5':
        print('You have selected: ' + item5)
        quantity = int(input("Enter quantity: "))
        if quantity > MAX_QUANTITY_ITEMS:
            print("Out of stock")
        elif quantity <= MAX_QUANTITY_ITEMS:
            print(item5, f'Amount: {quantity * hot_cheetos}' + '$')

            def paymentSystem(quantity):
                paymentInput = int(input(f"Give the amount for {quantity * hot_cheetos}: "))
                finalAamount = quantity * hot_cheetos
                if paymentInput < finalAamount:
                    print("Give the full amount.")
                elif paymentInput > finalAamount:
                    print("We dont give the change. pls enter proper amount.")
                else:
                    print("Here is your snack")

            paymentSystem(quantity)


while True:
    print('-----------------------------------||||VENDING MACHINE|||||-----------------------------')
    navItems()
    user_data = input('Enter index no. to get the snack: ')
    getting_user_data(user_data)
    order(user_data, hershey_small_amount, item1, hershey_big_amount, item2, coco_cola, item3, pepsi, item4, hot_cheetos, item5)
