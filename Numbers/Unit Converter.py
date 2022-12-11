# TODO Converts various units between one another. The user enters the type of unit being entered, the type of unit they
#  want to convert to and then the value. The program will then make the conversion.(temp, currency, volume,
#  mass and more)

def temperature(value, user_unit):
    if user_unit == 'K':
        celsius = value - 277.15
        print(f"{value}{user_unit} equals:\n{round(celsius, 2)}C\n{celsius*9/5+32}F")
    elif user_unit == 'C':
        print(f"{value}{user_unit} equals:\n{value+273.15}K\n{value*9/5+32}F")
    elif user_unit == 'F':
        celsius = (value-32) * 5/9
        print(f"{value}{user_unit} equals:\n{round(celsius, 2)}C\n{round(celsius + 273.15, 2)}K")
    else:
        print("wrong")


def volume_convert(value, user_type):
    type_to = input(f"In what type {value}{user_type}3 convert to: ")

    if type_to in types_list and type_to != user_type:

        if user_type == 'dm':
            metrs = value/1000
        elif user_type == 'cm':
            metrs = value/1000000
        elif user_type == 'mm':
            metrs = value/1000000000
        else:
            metrs = value

        if type_to == 'dm':
            total = metrs*1000
        elif type_to == 'cm':
            total = metrs * 1000000
        elif type_to == 'mm':
            total = metrs * 1000000000
        else:
            total = metrs
    else:
        print("There's wrong type and it can't be that origin type!")
        return
    return print(f"{value}{user_type} equals {total}{type_to}3")


def mass_convert(value, user_type):
    type_to = input(f"In what type {value}{user_type} convert to: ")
    if user_type == 'g':
        kilo = value/1000
    elif user_type == 't':
        kilo = value * 1000
    else:
        kilo = value



types_list = ['c', 'f', 'k', 'mm', 'cm', 'dm', 'm', 'g', 'kg', 't', 'lb', 'oz']

unit = int(input("Enter value to convert: "))

unit_type = input("Supported types:\nTemperature(C-celsius, F, K)\nVolume(m, dm, cm, mm)\nEnter type: ").lower()
if unit_type in types_list:
    print(unit_type)
    if unit_type in types_list[0:3:]:
        temperature(unit, unit_type.upper())
    elif unit_type in types_list[3:7]:
        volume_convert(unit, unit_type)
    elif unit_type in types_list[7:12]:
        pass



