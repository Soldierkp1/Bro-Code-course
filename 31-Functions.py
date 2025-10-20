def happy_birthday(name, age):
    print(f"Happy Birthday to {name}!")
    print(f"You are {age}!")
    print(f"Happy Birthday to {name}!")
    print()


happy_birthday("Bro", 20)
happy_birthday("Steve", 30)
happy_birthday("Joe", 40)

######

def display_invoice(username, amount, due_date):
    print(f"Hello {username},")
    print(f"Your invoice amount is ${amount}.")
    print(f"The due date is {due_date}.")
    print("Thank you for your business!")
    print()

display_invoice("John", 500000.00, "tomorrow")

######
def add(x, y):
    z = x + y
    return z

def substract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("No", "vaseo")

print(full_name)