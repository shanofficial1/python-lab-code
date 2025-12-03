try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except TypeError:
    print("Error: Invalid data type for division.")

except ValueError:
    print("Error: Please enter valid integers.")

else:
    print("Division operation completed successfully.")

finally:
    print("Program ended.")
