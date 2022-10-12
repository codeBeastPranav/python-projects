#contact book

name = []
number = []

x = 0
how_many = int(input("how many contacts do you want to add to your contact book: "))



while x < how_many:
    recepient_name = input("what is the name of the recipient: ")
    phone_number = int(input("enter the phone number: "))

    if len(str(phone_number)) > 10:
        print("invalid phone number")
        break
    else:
        name.append(recepient_name)
        print(name)
    
        number.append(phone_number)
        print(number)
    
    x = x + 1