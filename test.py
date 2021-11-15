# develop branch
def multiply(a, b):
    return a * b


def divide(a, b):
    return a // b


if __name__ == '__main__':
    print(multiply(2, 3))

while True:
    try:
        a = int(input("enter a"))
        b = int(input("enter b"))
        print(multiply(a, b))
        print(divide(a, b))
        print("ALL DONE")
        break
    except ValueError:
        print("Please enter the number")

print("222")
