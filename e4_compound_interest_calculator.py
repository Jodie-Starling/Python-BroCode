principal = 0
rate = 0
time = 0

while True:
    principal = float(input("Enter the principal amount: "))
    if principal <= 0:
        print("Principal amount must be greater than 0.")
    else:
        break    # 另一种写法，区分和下面的if语句

while rate <= 0:
    rate = float(input("Enter the annual interest rate (in %): "))
    if rate <= 0:
        print("Interest rate must be greater than 0.")

while time <= 0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Time must be greater than 0.")

print(principal)
print(rate)
print(time)

print(f'balance after {time} years: ${principal * (1 + rate / 100) ** time:.2f}')