numbers = [1, 5, 10, 15, 20, 25, 30]
num = int(input("Enter the number to be searched: "))
idx = 0
for val in numbers:
    if val == num:
        print(f"{num} found at {idx+1}")
        break
    idx += 1
