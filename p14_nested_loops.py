# nested loops = A loop within another loop (outer, inner)
#                outer loop:
#                    inner loop
rows = int(input("Enter the rows: "))
columns = int(input("Enter the columns: "))
symbol = input('Enter a symbol to use: ')

for x in range(1, rows + 1):
    for y in range(1, columns + 1):
        print(symbol, end = ' ')
    print()    # print new line after inner loop