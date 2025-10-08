# function = A block of reusable code
#            place () after the function name to invoke it

def happy_birthday(name,age):
    print(f"Happy Birthday to {name}!")
    print(f"You are {age} years old!")
    print("Happy Birthday to you!")
    print()

happy_birthday('Jodie', 20)
happy_birthday('John', 30)
happy_birthday('Jane', 40)


def display_invoice(username, amount, due_date):
    print(f'Hello {username}')
    print(f'Your bill of ${amount:.2f} is due: {due_date}')

display_invoice('johndoe', 100.00, '2024-07-01')


# return = statement used to end a function
#          and send a result back to the caller

def add(x, y):
    return x + y

print(add(5, 7))


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return f"{first} {last}"

print(create_name('jodie', 'starling'))