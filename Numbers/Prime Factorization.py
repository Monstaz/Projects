# TODO Have the user enter a number and find all Prime Factors (if there are any) and display them.


def prime():
    count = 3

    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Number must be integer!")
        return

    while number % 2 == 0:
        number /= 2
        print(2)

    while number != 1.0:
        if number % count == 0:
            print(count)
            number /= count
            continue
        else:
            count += 2


if __name__ == "__main__":
    prime()
