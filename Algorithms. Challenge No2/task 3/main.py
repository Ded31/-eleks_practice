def get_pascal_row(row):
    prev = 1
    print(prev, end=" ")
    for i in range(1, row + 1):
        current = (prev * (row - i + 1)) // i
        print(current, end=" ")
        prev = current


row = int(input('Input row: '))
get_pascal_row(row)
