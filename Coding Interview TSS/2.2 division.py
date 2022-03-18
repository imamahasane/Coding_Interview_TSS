
n = int(input("Enter your first number"))
m = int(input("Enter your second number"))

def division(a, b):
    if b == 0:
        return -1
    return a / b

print(division(n, m))