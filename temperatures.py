

def main():
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(MENU)
    get_choice()


def get_choice():
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            convert_c_to_f()
        elif choice == "F":
            convert_f_to_c()
        else:
            print("Invalid option")
        print()
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_c_to_f():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")


def convert_f_to_c():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Result: {celsius:.2f} C")


main()



