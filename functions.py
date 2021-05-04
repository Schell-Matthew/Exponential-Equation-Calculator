from time import sleep
from fractions import Fraction

def print_dots(num):
    for i in range(num):
        sleep(1)
        print('.', end='', flush=True)

def handle_error(message, option=0):
    if option == 0:
        print(f"\033[91m[!] Invalid input. {message}", end='')

    else:
        print(f"\033[91m[!] {message}", end='')

    print_dots(3)
    print("\n\033[92m")

def new_task(message):
    while True:
        try:
            print("================================Select Option================================")
            print(f"Would you like to:\n\n{message}3. Exit")
            choice = int(input(">>> "))

            if choice == 1:
                return 1

            elif choice == 2:
                return 2

            elif choice == 3:
                raise KeyboardInterrupt

            else:
                handle_error("Please enter a valid option")
                continue

        except ValueError:
            handle_error("Please enter a valid option")
            continue


def get_points():
    while True:
        user_input = input("\033[92mEnter the points from the table in the format x,y | x,y\n>>> ")
        commas = user_input.count(',')
        pipes = user_input.count('|')

        if len(user_input) == 0:
            handle_error("Please enter at least 2 points")
            continue

        if commas == 0 or pipes == 0:
            handle_error("Please separate x and y values with ',' and coordinates with '|'")
            continue

        if pipes >= commas:
            handle_error("Please separate x and y values with ',' and coordinates with '|' but don't end with '|'")
            continue

        tmp = [char for char in user_input if char != ' ']
        values = ''.join(tmp)
        del tmp

        val_list = []
        tmp = values.split('|')

        for item in tmp:
            val_list.append(item.split(','))

        num = 0
        for i in val_list:
            if len(i) > 2:
                handle_error("Only enter 1 x-value and 1 y-value for each point")
                num += 1
                break

        if num == 1:
            continue
        del num

        num = 0
        for j in val_list:
            i = 0
            while i < len(j):
                if '/' in j[i]:
                    try:
                        j[i] = Fraction(j[i])
                    except ValueError:
                        handle_error("Your fractions may be incomplete. Try again")
                        num += 1
                        break
                i += 1

            if num == 1:
                break

        if num == 1:
            continue

        try:
            for j in val_list:
                i = 0
                while i < len(j):
                    if type(j[i]) != Fraction:
                        j[i] = int(j[i])
                    i += 1

        except ValueError:
            handle_error("No characters except for ',' and '|' are allowed")
            continue

        index = 0
        num = 0
        yIntCounter = 0
        try:
            while index < len(val_list):
                if val_list[index][0] == 0:
                    yIntCounter += 1

                if val_list[index][0] + 1 != val_list[index + 1][0] and val_list[index][0] - 1 != val_list[index + 1][0]:
                    handle_error("Please write points with x values that are in ascending or descending order")
                    num += 1
                    break

                index += 1
        except IndexError:
            pass

        if num == 1:
            continue

        if yIntCounter > 1 or yIntCounter < 1:
            handle_error("There should be 1 y-intercept")
            continue

        num = 0
        for item in val_list:
            if val_list.count(item) > 1:
                handle_error("There are duplicate points, Please remove them")
                num += 1
                break

        if num == 1:
            continue
        del num

        break

    return val_list


def find_pattern(point_list):
    i, j = 1, 1
    pattern = Fraction(point_list[1][1], point_list[0][1])

    while j < len(point_list):
        while i < len(point_list[j]):
            if Fraction(point_list[j][i], point_list[j - 1][i]) != pattern:
                return None
            i += 1
        j += 1

    return pattern

def calcExpGrowth(yint, rate, time):
    one = (1 + rate) ** time
    result = one * yint
    return result

def calcExpDecay(yint, rate, time):
    one = (1 - rate) ** time
    result = one * yint
    return result
