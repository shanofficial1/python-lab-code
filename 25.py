import csv

# Open CSV file in write mode
with open("1st_MCA_2023_25.csv", mode="w", newline="") as file:
    writer = csv.writer(file)

    # Write header
    writer.writerow(["Name", "Email"])

    n = int(input("Enter number of students: "))

    for i in range(n):
        name = input("Enter student name: ")
        email = input("Enter student email: ")
        writer.writerow([name, email])

print("1st_MCA_2023_25.csv file created successfully.")
