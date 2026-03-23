try:
    x = int(input("Enter a number: "))
    ans = 10/x

except ZeroDivisionError:
    print("Division by 0 is not allowed")

except ValueError:
    print("Anything other than integer is not allowed")

else:
    print(ans)

finally:
    print("End of program")