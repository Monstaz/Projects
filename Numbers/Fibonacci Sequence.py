# TODO Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number
#  or to the Nth number.

def fibonacci():
    fib1 = 0
    fib2 = 1

    while True:
        try:
            number = int(input("Enter a number to generate Fibonacci sequence: "))
            break
        except ValueError:
            print("You should enter an integer number")
            continue

    for i in range(number):
        fib1, fib2 = fib2, fib1+fib2
        print(fib1, end=' ')


if __name__ == "__main__":
    fibonacci()
