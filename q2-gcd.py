# Repeat the following steps until b becomes 0:

# Set temp = b

# Set b = a % b (remainder when a is divided by b)

# Set a = temp

# When b becomes 0, the current value of a is the GCD.

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))      
print("GCD of",a,"and",b,"is",gcd(a,b))