from functions import *
from subprocess import run

try:
    run("clear", shell=True)

    print("\033[92m[*] Initializing Exponential Equation Calculator", end='', flush=True)
    print_dots(3)

    while True:
        print("\n\n================================Select Option================================")
        print("1. Create exponential equation\n2. Calculate exponential growth\n3. Calculate exponential decay\n4. Exit")

        try:
            option = int(input(">>> "))
        except ValueError:
            handle_error("Please enter an option from above")
            continue

        if option == 1:
            while True:
                equation = ["y = "]
                points_table = get_points()
                for j in points_table:
                    i = 0
                    status = 0
                    while i < len(j):
                        if j[i] == 0:
                            yInt = j[i + 1]
                            status += 1
                            break
                        i += 1
                    if status == 1:
                        break

                growth_rate = str(find_pattern(points_table))

                if growth_rate is None:
                    handle_error("There is no exponential pattern in the table provided. Try again", 1)
                    continue

                equation.append(str(yInt))
                equation.append(" * ")
                equation.append(growth_rate)
                equation.append("^x")
                result = ''.join(equation)

                print(f"\033[93m[*] Equation Calculated! The equation is \033[96m{result}\033[92m")
                del equation, result
                sleep(2)
                status = new_task("1. Calculate another equation\n2. Choose a different option\n")

                if status == 1:
                    continue

                elif status == 2:
                    break

            if status == 2:
                continue

        elif option == 2:
            while True:
                try:
                    yInt = Fraction(input("Enter the 'a' value (y-intercept): "))
                    growth_rate = float(input("Enter the 'r' value (growth rate): "))
                    time = int(input("Enter the 't' value (time in whatever measurement): "))
                except ValueError:
                    handle_error("Please enter a number")
                    continue

                print(f"\033[93m[*] Calculation complete! Result = \033[96m{calcExpGrowth(yInt, growth_rate, time)}\033[92m")
                sleep(2)
                status = new_task("1. Calculate Exponential Growth again\n2. Choose a different option\n")

                if status == 1:
                    continue

                elif status == 2:
                    break

            if status == 2:
                continue

        elif option == 3:
            while True:
                try:
                    yInt = float(input("Enter the 'a' value (y-intercept): "))
                    decay_rate = float(input("Enter the 'r' value (decay rate): "))
                    time = int(input("Enter the 't' value (time in whatever measurement): "))

                except ValueError:
                    handle_error("Please enter a number")
                    continue

                print(f"\033[93m[*] Calculation complete! Result = \033[96m{calcExpDecay(yInt, decay_rate, time)}\033[92m")
                sleep(2)
                status = new_task("1. Calculate Exponential Decay again\n2. Choose a different option\n")

                if status == 1:
                    continue

                elif status == 2:
                    break

            if status == 2:
                continue

        elif option == 4:
            raise KeyboardInterrupt

        else:
            handle_error("Please enter an option from above")
            continue
        break

except KeyboardInterrupt:
    print("\n\033[96m[*] Shutting down...\n\033[0m")
    exit(0)
