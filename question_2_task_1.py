
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

if len(first_name) > 2 and len(last_name) > 2:
    print(len(first_name))
    print(len(last_name))
else:
    print("must be more than 2 charcters")