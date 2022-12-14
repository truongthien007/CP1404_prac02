
"""
menu
function main
    display menu
    get choice
    while choice != "Q":
        if choice == "G":
           function validate_score()
        else if choice == "P":
            final_score = validate_score()
            result = determine_score(final_score)
            display result
        else if choice == "S":
            final_score = validate_score()
            display stars
        else:
            display invalid
        display menu
        get choice
    display goodbye

def validate_score():
    get score
    while score < 0 or score > 100:
        display invalid
        get score
    return score


def determine_score(final_score):
    if final_score < 50:
        result = "Bad"
    else if final_score < 90:
        result = "Pass"
    else:
        result = "Excellent"
    return result


main()


"""
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
            # final_score is the valid score after validate
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
