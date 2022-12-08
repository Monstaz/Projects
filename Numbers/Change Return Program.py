# TODO The user enters a cost and then the amount of money given. The program will figure out the change
#  and the number of quarters, dimes, nickels, pennies needed for the change.

def main():
    coins = []

    while True:
        try:
            cost = float(input("cost: "))
            money = float(input("money given: "))
            if cost > money:
                print("cost can't be bigger than money you given!")
                continue
            break
        except ValueError:
            print("Enter only digits!")

    dollars = money-round(cost, 2)
    change = int((dollars*100)-int(dollars)*100)

    if change == 0:
        print(f"Your change is: {int(dollars)} dollars")
        return

    if change // 25 > 0:
        quarters = change // 25
        change -= quarters * 25
        coins.append(f"{quarters} quarters ")

    if change // 10 > 0:
        dimes = change // 10
        change -= dimes * 10
        coins.append(f"{dimes} dimes ")

    if change // 5 > 0:
        nickels = change // 5
        change -= nickels * 5
        coins.append(f"{nickels} nickels ")

    if change // 1 > 0:
        pennies = change // 1
        coins.append(f"{pennies} pennie ")

    total_coins = ''
    for coin in coins:
        total_coins += coin

    print(f"your change: {int(dollars)} dollars {total_coins} ")


if __name__ == "__main__":
    main()