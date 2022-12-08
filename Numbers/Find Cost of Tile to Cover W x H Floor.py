# TODO Calculate the total cost of tile it would take to cover a floor plan of width and height,
#  using a cost entered by the user.


def square(width, length):
    return width * length
    pass


def price(w1, l1, w2, l2, cost):
    return square(w1, l1) / square(w2, l2) * cost


def digit_check(param):
    while True:
        try:
            arg = float(input(f"Enter {param}: "))
            if arg == 0:
                print(f"{param} can not equals 0!")
                continue
            return arg
        except ValueError:
            print(f"{param} should be integer!")


def main():
    floor_width = digit_check("floor width")
    floor_length = digit_check("floor length")
    tile_length = digit_check("tile length")
    tile_width = digit_check("tile width")
    tile_cost = digit_check("tile cost")

    if square(floor_width, floor_length) < square(tile_width, tile_length):
        print("Tile can not be bigger than floor")
        return

    total = price(floor_width, floor_length, tile_width, tile_length, tile_cost)
    print(f"Total cost: {total} y.e.")


if __name__ == "__main__":
    main()
