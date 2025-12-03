import logging
import os

# Configure logging
logging.basicConfig(
    filename="error_log.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -------- Program 1: File Handling with Exception Logging --------
try:
    filename = input("Enter file name to create: ")

    if os.path.exists(filename):
        raise FileExistsError("File already exists.")

    with open(filename, "w") as f:
        f.write("File created successfully.\n")
        print("File opened in write mode successfully.")

except Exception as e:
    print("File error occurred.")
    logging.error(e)


# -------- Program 2: Division with Exception Logging --------
try:
    a = int(input("\nEnter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result:", result)

except ZeroDivisionError as e:
    print("Division by zero error.")
    logging.error(e)

except (TypeError, ValueError) as e:
    print("Invalid input type.")
    logging.error(e)

except Exception as e:
    print("Unexpected error.")
    logging.error(e)

finally:
    print("\nProgram execution completed.")
