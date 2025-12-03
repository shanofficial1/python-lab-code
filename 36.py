class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Overload + operator
    def __add__(self, other):
        return Complex(self.real + other.real,
                       self.imag + other.imag)

    # Overload - operator
    def __sub__(self, other):
        return Complex(self.real - other.real,
                       self.imag - other.imag)

    def display(self):
        sign = "+" if self.imag >= 0 else "-"
        print(f"{self.real} {sign} {abs(self.imag)}i")


# Input
r1 = float(input("Enter real part of first complex number: "))
i1 = float(input("Enter imaginary part of first complex number: "))

r2 = float(input("Enter real part of second complex number: "))
i2 = float(input("Enter imaginary part of second complex number: "))

# Objects
c1 = Complex(r1, i1)
c2 = Complex(r2, i2)

# Operations
sum_result = c1 + c2
diff_result = c1 - c2

# Output




print("\nSum of Complex Numbers:")
sum_result.display()

print("Difference of Complex Numbers:")
diff_result.display()
