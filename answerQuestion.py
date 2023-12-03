import time, random
min_value = 2
max_value = 8
operators = ["+", "-", "*"]
total_problems = 2

def problem_creator():
    min_digit = random.randint(min_value, max_value)
    max_digit = random.randint(min_value, max_value)
    choose_operators = random.choice(operators)

    problem = str(min_digit) + " " + choose_operators + " " + str(max_digit)
    solution = eval(problem)
    return solution, problem

wrong_answers = 0
start_time = time.time()

for i in range(total_problems):
    solution, problem = problem_creator()
    while True:
        user_answer = input("Question:" + " " + str(problem) + " " + "Your Answer:" + " ")
        if user_answer.isdigit():
            user_answer = int(user_answer)

            if user_answer == solution:
                print("Correct Answer")
                break
            elif user_answer < solution:
                print("Answer Is Greater Than This")
            else:
                print("Answer Is Lesser Than This")
            wrong_answers+=1
        else:
            print("Enter A Number")
end_time = time.time()
total_time = round(end_time - start_time, 2)
print("You gave respond to all" + " " + str(total_problems) + " " + "Questions" + " " + "With in" + " " + str(total_time) + " " +"Seconds" + " " + "Wrong Answers" + " " + str(wrong_answers) + ".")
