"""30. This Word Test Will Reveal If You're More Introverted Or Extroverted | Ryan Trepanier
    https://www.buzzfeed.com/andrewziegler/best-buzzfeed-quizzes """

import os
import time


def main():

    print("Answer these questions 9 to determine if you're an introvert or extrovert.\n")

    # list of quiz questions
    questions = [

        {"question1": "_old",
        "introvert": ["sold"],
        "extrovert": ["cold", "bold", "told"]
        },
        {"question2": "see_",
        "introvert": ["seem"],
        "extrovert": ["seed", "seek", "seen"]
        },
        {"question3": "ga_e",
        "introvert": ["gape"],
        "extrovert": ["gale", "game", "gave"]
        },
        {"question4": "wa_",
        "introvert": ["way"],
        "extrovert": ["wax", "war", "was"]
        },
        {"question5": "_atch",
        "introvert": ["watch"],
        "extrovert": ["batch", "catch", "latch"]
        },
        {"question6": "_oss",
        "introvert": ["loss"],
        "extrovert": ["moss", "boss", "toss"]
        },
        {"question7": "sto_e",
        "introvert": ["stove"],
        "extrovert": ["stone", "stole", "store"]
        },
        {"question8": "ba_k",
        "introvert": ["bask"],
        "extrovert": ["back", "bank", "bark"]
        },
        {"question9": "s_ar",
        "introvert": ["star"],
        "extrovert": ["sear", "scar", "soar"]
        }
    ]
    ## quiz
    intro = 0
    extro = 0
    for q in questions:
        print("Choose a word...\n")
        options = q["introvert"].copy()
        options.extend(q["extrovert"])
        options.sort()
        print(options)
        choice = input("\n>>>")
        choice.lower()
        while choice not in options:
            print("Invalid choice, try again.\n")
            choice = input("\n>>>").lower()
        if choice in q["introvert"]: 
            intro += 1
        else:
            extro += 1
        time.sleep(1)
        os.system('clear')

    if intro > extro:
        print("Better cancel your plans! You're an introvert!") 
    elif intro == extro:
        print("Wow! Looks like you're a rare hybrid of both introvert and extrovert.")
    else:
        print("EXTROVERTS UNITE! LET'S PARTY!!")   

main()