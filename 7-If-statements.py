#if statement is used to some code if the statement given is True, else: do something else.

age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up.")
elif age >= 18: 
    print("You are signed up.")
elif age < 0:
    print("You haven't been born yet broski.")
else:
    print("You are underage. Can't sign up.")

response = input("Would you like food? (Y/N) ")

if response == "Y":
    print("Have some food.")
else:
    print("No food for you.")