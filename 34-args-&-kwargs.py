# *args = (arguments) allows you to pass multiple non-key arguments. ==> Tuples if its args
# Prefix each parameter with unpacking operator = *

# **kwargs = (keyword-arguments) allows to pass mulptiple keyword arguments. ==> Dictionaries if its kwargs
# Prefix each parameter with unpacking operator = *


####ARGS####
#Function to add 2 num together.

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
        

print(add(1,2,4,55,54,33))

#Funcion to display someone's name.

def display_name(*args):
    for arg in args:
        print(arg, end=" ")
        
display_name("Don", "Corleone")

####KWARGS####

#Function to print address.

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="55 street",
              city="Gotham City",
              state="California",
              zip="12342")
