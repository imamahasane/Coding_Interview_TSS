

n = int(input("Enter your first number"))
m = int(input("Enter your second number"))

def division(a, b):
    try:
        return a / b
    
    except ZeroDivisionError:
        print("Can't division by zro")

print(division(n, m))