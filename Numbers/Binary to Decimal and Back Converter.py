# TODO Design a converter to convert a decimal number to a binary number, or a binary number to its decimal equivalent.


def decimal_to_binary(number):

    binary_number = ""

    while number > 0:
        binary = number % 2
        number //= 2
        binary_number += str(binary)

    print(binary_number[::-1])


def binary_to_decimal(number):
    decimal_number = 0
    number = str(number)
    times = len(number)

    for i in range(times-1, -1, -1):
        decimal_number += 2 ** i * int(number[times - (i+1)])

    print(decimal_number)


def main():
    while True:
        try:
            user_number = int(input("Enter a decimal or binary number: "))
            break
        except ValueError:
            print("Only integer numbers!")

    while True:
        choose = input("What conversion to use:\n1 - Decimal to binary\n2 - Binary to Decimal\nType exit - to exit\n")

        if choose == '1':
            decimal_to_binary(user_number)
            return
        elif choose == '2':
            numbers = ('2','3','4','5','6','7','8','9')
            if set([i for i in str(user_number)]).intersection(numbers):
                print("Binary number only consists 1 and 0!")
                continue
            else:
                binary_to_decimal(user_number)
            return
        elif choose.lower() == 'exit':
            return
        else:
            print("Choose the option!")


if __name__ == "__main__":
    main()


# Or simply:
# def decimal_to_binary(number):
#     print(f"The binary equivalent of {number} is: {bin(number)}")
# def binary_to_decimal(number):
#     print(f"The decimal equivalent of {number} is: {int(str(number), 2) }")
