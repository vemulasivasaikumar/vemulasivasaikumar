a = int(input("Enter a number: "))
odd_numbers = list(range(1, 2 * a, 2))
print(", ".join(map(str, odd_numbers)))
