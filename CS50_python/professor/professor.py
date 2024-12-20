'''
In a file called professor.py, implement a program that: Prompts the user for a level.
If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is
a non-negative integer with n digits. No need to support operations other than addition (+).
Prompts the user to solve each of those problems. If an answer is not correct (or not even a number),
the program should output EEE and prompt the user again, allowing the user up to three tries in total
for that problem. If the user has still not answered correctly after three tries,
the program should output the correct answer.
The program should ultimately output the user’s score: the number of correct answers out of 10.

Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts)
the user for a level and returns 1, 2, or 3, and generate_integer returns a randomly generated
non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:
'''

import random
import sys

#Main calls other functions to get level, get random numbers, keep count of questions, errors, and score

def main():

    score = 0
    questionNumber = 10

    level = get_level()

    while True:

        if questionNumber > 0:

            firstNumber, secondNumber, questionNumber = generate_integer(level, questionNumber)

            result = get_addition(firstNumber, secondNumber)

            attempts = 3
            while attempts:
                user_answer = get_user_answer(firstNumber, secondNumber)

                if int(user_answer) != int(result):
                    print("EEE")
                    attempts -= 1
                    if attempts == 0:
                        print(f"{firstNumber} + {secondNumber} = {result}")
                else:
                    score += 1
                    break
        else:
            print(f"Score = {score}")
            sys.exit()

#the function get_level prompts user to provide difficulty level
def get_level():
    while True:
        try:
            l = (input("Level: "))
            if 4 > int(l) > 0:
                return int(l)
        except ValueError:
            pass

#the function generate_integer generates random numbers based on selected difficulty level
def generate_integer(level,qn):

    while True:

        try:
            if level == 1:
                n1 = random.randint(0,9)
                n2 = random.randint(0,9)
            elif level == 2:
                n1 = random.randint(10,99)
                n2 = random.randint(10,99)
            else:
                n1 = random.randint(100,999)
                n2 = random.randint(100,999)

            qn -= 1
            return (n1, n2, qn)

        except ValueError:
            pass

# get_addition adds the random numbers generated by generate_integer
def get_addition(n1, n2):
    return n1 + n2

#the function get_user_answer prompts user to provide their answer to the addition of random numbers
def get_user_answer(n1, n2):
    print(f"{n1} + {n2} = ", end = "")
    return  input()


if __name__ == "__main__":
    main()