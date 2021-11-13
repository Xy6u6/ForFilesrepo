def multiply(a, b):
    return a * b

while True:
    try:
            a = int(input("enter a"))
            b = int(input("enter b"))
            print(multiply(a, b))
            break
    except ValueError:
        print("Please enter the number")

