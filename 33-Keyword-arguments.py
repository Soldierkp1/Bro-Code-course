#keyword arguments = an argument preceded by an identifier,
#helps with readability.
#order of arguments doesn't matter.


def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first}{last}")
    
#hello(greeting="Hello", title="Mr. ", first="Don ", last="Toretto") # ==> positionals have to be behind keyword arguments.

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=123, first=456, last=7890)
print(phone_num)