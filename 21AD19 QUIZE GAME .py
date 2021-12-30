# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%"" CONGRATULATION")

# -------------------------
def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -------------------------

print("WELCOME TO THE QUIZE GAME")
questions = {
 "Who Is The Faculty for B10 PYTHON PROGRAMMING COURSE ?: ": "C",
 "What year was KCG COLLEGE STARTED ?: ": "A",
 "Who is The Founder Of the KCG COLLEGE ?: ": "C",
 "Who is The BOY Representative of B10 Department ?: ": "B"
 #Who is The BOY Representative of B10 Department ?: ": "B" #Who is Our CURRENT PRINCIPAL ? " :"D"
}

options = [["A. KAMALA HASAN SIR", "B. VIJAYAKANTH SIR", "C. PALANIAPPAN SIR", "D. RAJINIKANTH SIR"],
          ["A. 1998", "B. 1999","C. 2000", "D. 2016"],
          ["A. KCG SUDARSHAN", "B. KCG MUHAMMAD", "C. KCG VERGHESE", "D. KCG ABDUL"],
          ["A. DIKESH ","B. KUMARAN", "C. DINAKARAN", "D. ANAND"]]



new_game()

while play_again():
    new_game()

print("Byeeeeee!")
