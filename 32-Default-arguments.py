#Defaul arguments = A default value for certain parameters,
#Default is used when that argument is omitted,
#Make you functions more flexible,
#Reduces # of arguments
#1. Positional, 2. Default, 3. Keyword, 4. Arbitrary


def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1-discount) * (1+tax)

print(net_price(500, 0.1, 0))