import functions as fuc


while True:
    user_answer = input("Would you like to add or view bills: ").capitalize()
    user_answer = user_answer.strip()

    if user_answer == 'Add':
        bill = input("Enter Bill name:")
        amount = input("Enter Bill Amount")

        fuc.create_new_bill(bill, amount)

    elif user_answer == 'View':
        fuc.view_bills()

    else:
        quit()
