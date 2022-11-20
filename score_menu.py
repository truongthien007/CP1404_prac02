

MENU = "(G)et score (must be 0-100 inclusive), (P)rint result, (S)how stars, (Q)uit "


def main():
    print(MENU)
    choice = input("Your choice: ").upper()
    while choice != "Q":
        if choice == "G":
            """to get valid score"""
            validate_score()
        elif choice == "P":
            """print the result"""
            final_score = validate_score()
            result = determine_score(final_score)
            print(result)
        elif choice == "S":
            "print as many stars as score"
            final_score = validate_score()
            print("*" * final_score)
        else:
            print("Invalid input")
        print(MENU)
        choice = input("Your choice: ").upper()
    print("Farewell")


def validate_score():
    """check valid score"""
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


def determine_score(final_score):
    """determine the result"""
    if final_score < 50:
        result = "Bad"
    elif final_score < 90:
        result = "Pass"
    else:
        result = "Excellent"
    return result


main()
