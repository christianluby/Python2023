# a dictionary that stores questions and answers
# have a variable that stores the score of a player
# loop through the dictiomnary using key value pairs
# display each question to the user and allow them to answer
# tell them if they are right or wrong
# show the final resort when quiz is completed
quiz = {
    "question1" : {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
        "question2" : {
        "question": "What is the capital of Puerto Rico?",
        "answer": "San Juan"
    },
        "question3" : {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
        "question4" : {
        "question": "What is the capital of Austria?",
        "answer": "Vienna"
    },
        "question5" : {
        "question": "What is the capital of Portugal?",
        "answer": "Lisbon"
    },
        "question6" : {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
        "question7" : {
        "question": "What is the capital of Holland?",
        "answer": "Amsterdam"
    },
        "question8" : {
        "question": "What is the capital of England?",
        "answer": "London"
    },
}

score = 0

for key, value in quiz.items():
    print(value["question"])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        print("Correct")
        score +=1
        print("Your score is: " + str(score))
        print("")
        print("")

    else:
        print("Incorrect")
        print("The answer is :" + value['answer'])
        print("Your score is: " + str(score))
        print("")
        print("")

quiz_length= len(quiz)

print("You got " + str(score) + " out of " + str(quiz_length) + " questions correctly")
print("your percentage is " + str(score/8 * 100) + "%")