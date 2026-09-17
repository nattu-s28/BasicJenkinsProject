from calculator import add, subtract, multiply, divide

def main():
    print("Python Calculator")
    print("-----------------")

    a = 10
    b = 10

    print("Addition:", add(a, b))
    print("Subtraction:", subtract(a, b))
    print("Multiplication:", multiply(a, b))
    print("Division:", divide(a, b))


if __name__ == "__main__":
    main()