
import random


def main():
    score = float(input("Enter score: "))
    score_result = determine_score(score)
    print(score_result)
    print(determine_score(random.randint(0, 100)))


def determine_score(score):
    """ to get valid score and determine the result """
    if 0 > score or score > 100:
        score_result = "Invalid score"
    elif score < 50:
        score_result = "Bad"
    elif score < 90:
        score_result = "Pass"
    else:
        score_result = "Excellent"
    return score_result


main()
