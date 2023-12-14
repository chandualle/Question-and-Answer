import random, time

operators = ["+", "-", "*"]
def get_numeric_input(prompt):
    while True:
        value = input(prompt + " ")
        if value.isdigit():
            return int(value)
        else:
            print(value + " is not a number. Please enter a valid number.")

min_value = get_numeric_input("Enter Minimum Value:")
max_value = get_numeric_input("Enter Maximum Value:")
totalQuestions = get_numeric_input("How many questions:")

def problem_generator():

    lowerNumber = random.randint(min_value,max_value)
    higherNumber = random.randint(min_value,max_value)
    take_oprator = random.choice(operators)

    problem = str(lowerNumber) + " " + take_oprator + " " + str(higherNumber)
    solution = eval(problem)
    return solution, problem

wrongAnswers = 0
startTime = time.time()

for i in range(totalQuestions):
    solution, problem = problem_generator()
    while True:
        userAnswer = input("Question is" + " " + problem + " " + "and Your answer is" + " : ")
        if userAnswer.isdigit():
            userAnswer = int(userAnswer)

            if userAnswer == solution:
                print("Yeah! Your Answer Is Correct")
                break
            elif userAnswer < solution:
                print("You gussed lower number")
            else:
                print("You gussed higher number")
            wrongAnswers += 1
        else:
            print("Please enter an number")
endTime = time.time()
totalTime = round(endTime - startTime, 2)
print("You answered all questions and you gave wrong answers" + " " + str(wrongAnswers) + " " + "Took Time" + " " + str(totalTime))
