import random


# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats repeat if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")
            print()


# instructions displays instructions if user wants
def instructions():

    print('''
    
    **** Instructions ****
    
    Objective:
    Try to answer as many of the questions as you can correctly
    
    How to Play:
    Choose how many math questions do you want
    
    You will be given a addition(+), subtraction(-), multiplication(x) and division(/) 
    You don't have a time limit but please try and speed run the quiz
    You have to answer correctly cause if you get it wrong you will get 
    a thumbs down if you get it right you will get a thumbs up
        ''')


def num_questions():
    while True:
        num = input("How many math questions do you want?").lower()

        try:
            num = int(num)

            if num >= 1:
                return num

        except ValueError:
            if num == "infinite" or num == "i":
                return "infinite"
        print()
        print("Enter a Number between 1 or more")
        print()


def ask_questions():
    number_1 = int(random.randint(1, 12))
    number_2 = int(random.randint(1, 12))
    pick_sign = random.randint(1, 4)

    if pick_sign == 1:
        sign = "+"
        right_answer = number_1 + number_2

    elif pick_sign == 2:
        sign = "-"
        right_answer = number_1 - number_2

    elif pick_sign == 3:
        sign = "/"
        right_answer = round(number_1 / number_2)

    else:
        sign = "x"
        right_answer = number_1 * number_2

    while True:
        answer = (input(f"Figure out {number_1} {sign} {number_2}"
                        f" your answer will be rounded to the nearest whole number"))
        quiz_history.append(f"{number_1} {sign} {number_2}?")
        try:
            answer = round(float(answer))
            quiz_history.append(f"you answered {answer}")
            if answer == right_answer:
                print("👍")
                quiz_history.append(f"you were correct")
                return f"{number_1} {sign} {number_2} = {right_answer} \nYou entered {answer} Correct!"

            else:
                print("👎")
                quiz_history.append(f"the correct answer was  {right_answer}")
                return "wrong"

        except ValueError:
            print("please enter a integer")

quiz_history = []

# main code
print()
print("+-+-=MATH QUIZ=-+-+")
print()

instructions_yn = yes_no("Do you want to read the instructions?")

if instructions_yn == "yes":
    instructions()

else:
    print()

total_questions = num_questions()


for num in range(0, total_questions):
    quiz_history.append(f"Question {num}!")
    ask_questions()

want_history = yes_no("do you want to see how you did? ")

if want_history == "yes":
    for item in quiz_history:
        print(item)
print("")
print("congrats thanks for playing")
