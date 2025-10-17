# keyword arguments = order of arguments does not matter

for x in range(1, 6):
    print(x, end=' ') # end is a keyword argument

def get_phone(country, area_code, number):
    phone_number = f"+{country} ({area_code}) {number}"
    return phone_number

print(get_phone(number="555-1234", country="1", area_code="800"))