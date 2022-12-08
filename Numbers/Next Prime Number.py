# TODO Have the program find prime numbers until the user chooses to stop asking for the next one.

def prime_number(number):
    for x in range(3, number+1, 2):
        if number % x == 0:
            if number // x == 1:
                print(number)
                return True
            else:
                return False


def main():
    print("First prime number is 2. Next is:")
    for i in range(3, 10000, 2):
        if prime_number(i):
            next_prime = input("Type Enter or any button to see next prime number or type exit to end program")
            if next_prime.lower() == 'exit':
                break


if __name__ == "__main__":
    main()