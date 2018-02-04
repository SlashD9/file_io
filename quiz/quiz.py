def show_menu():
    print("1. Ask questions")
    print("2. Add a question")
    print( "3. Exit game")
    
    option = input("Enter option: ")
    return option
    
def add_question():
    print("")
    question = input("Enter a question\n>")
    
    print("")
    print("Ok then, tell me the answer")
    answer = input("{0}\n>".format(question))
    
    file = open("questions.txt", "a")
    file.write(question + "\n")
    file.write(answer + "\n")
    file.close()

def ask_question():
    # first we will create two lists to hold our quesitions and answers
    questions = []
    answers = []
    
    # the with block helps with the file handling, we don't need to worry about 
    # closing the file.
    with open("questions.txt", "r") as file:
        lines = file.read().splitlines()
    
    # for i and text in the list of lines
    for i, text in enumerate(lines):
        # if the line is even, add that line to questions
        if i%2 == 0:
            questions.append(text)
        # else add the line to answers
        else:
            answers.append(text)
    
    # find out how many questions there are
    number_of_questions = len(questions)
    # create a variable to zip(questions, answers)
    questions_and_answers = zip(questions, answers)
    
    # create a score var to calculate the score
    score = 0
    
    
    # Create a Tuple of questions and answers.
    for question, answer in questions_and_answers:
        guess = input(question + "> ")
        # if the user guess is the same as the answer
        if guess == answer:
            score +=1
            print("right!")
            print(score)
        # if not the same we print it was wrong
        else:
            print("wrong!")
    # When all the questions have been answered we print the final score
    print("You got {0} correct out of {1}".format(score, number_of_questions))

def game_loop():
    while True:
        option = show_menu()
        if option == "1":
            ask_question()
        elif option == "2":
            add_question()
        elif option == "3":
            break
        else:
            print("Invalid Option")
        print("")
            
game_loop()