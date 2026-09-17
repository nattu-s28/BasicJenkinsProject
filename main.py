from calculator import add, subtract, multiply, divide

def main():
    print("Python Calculator")
    print("-----------------")

    a = 10
    b = 10

    print("-----------------")
    print("Addition:", add(a, b))
    print("-----------------")
    print("Subtraction:", subtract(a, b))
    print("-----------------")
    print("Multiplication:", multiply(a, b))
    print("-----------------")
    print("Division:", divide(a, b))
    print("-----------------")


if __name__ == "__main__":
    main()