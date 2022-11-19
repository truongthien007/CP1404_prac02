# length = 10
# name = input("Enter a name with at least 10 characters: ")
# while len(name) < length:
#     print("invalid name")
#     name = input("Enter a name with at least 10 characters: ")
# print("*" * len(name), end=" ")

length = 10


def main():
    name = validate_name()
    print("*" * len(name), end=" ")


def validate_name():
    name = input("Enter a name with at least 10 characters: ")
    while len(name) < length:
        print("invalid name")
        name = input('Enter a name with at least 10 characters: ')
    return name


main()
