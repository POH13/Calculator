import sys


def calc(command, numbers):
    help_usage = "usage: calculator.py <command> <number> ... <number> \n" \
                 "<command>: ADD, SUB, MUL, DIV \n" \
                 "<number>: any amount of integers or floats seperator by spaces(' ')"

    list_of_numbers = []
    # if numbers are invalid, exit
    for each_number in numbers:
        if not str(each_number).isnumeric():
            print("Invalid numbers! Exiting program")
            print(help_usage)
            exit()
        list_of_numbers.append(float(each_number))

    # if list_of_numbers have 0/1 number only, exit
    if len(list_of_numbers) <= 1:
        print(help_usage)

    result = list_of_numbers[0]
    command = command.upper()
    if command == "ADD":
        result = sum(list_of_numbers)
    elif command == "SUB":
        for number in list_of_numbers[1:]:
            result -= number
    elif command == "MUL":
        for number in list_of_numbers[1:]:
            result *= number
    elif command == "DIV":
        for number in list_of_numbers[1:]:
            if number == 0:
                print("Error: Division by zero! Exiting program")
                exit()
            result /= number
    else:
        print(help_usage)
        exit()

    if result.is_integer():
        return int(result)
    else:
        return result


if __name__ == "__main__":
    print(calc(sys.argv[1], sys.argv[2:]))
