a = int(input("Enter a number: "))
count = a if a % 2 != 0 else a - 1
odd_numbers = list(range(1, 2 * count, 2))
print(", ".join(map(str, odd_numbers)))


