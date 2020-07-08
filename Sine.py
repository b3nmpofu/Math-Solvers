import math

def div(a, b):
    return a // b


def mul(a, b):
    return a * b


def sine(a):
    return math.sin(a)


print("Select format your question?")
print("1. sin xy(for example)")
print("2. sin x/y(for example)")
print("3. sin xy/z(for example)")
print("4.sin x")

example = input("Format: ")

if example in ('1', '2', '3', '4'):
    print("Solution")
    x = float(input("Enter The value of x: "))


    if example == '1':
        y = float(input("Enter The value of y: "))
        num1 = x * y
        print("The sine of ", x, "x", y, "=", sine(num1))

    elif example == '2':
        y = float(input("Enter The value of y: "))
        ans = div(x , y)

        print("The sine of", x, "/", y, "=", sine(ans))

    elif example == '3':
        y = float(input("Enter The value of y: "))
        z = float(input("Enter The value of z: "))
        ans = mul(x, y)
        ans2 = div(ans, z)
        print("The sine of", x, "=", sine(ans2))

    elif example == '4':
        print("The sine of", x, "=", sine(x))

    else:
     print("Invalid")
else:
     print("Done Bwa")
