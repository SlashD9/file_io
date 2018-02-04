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
    
    # Create a Tuple of questions and answers.
    for question, answer in zip(questions, answers):
        guess = input(question + "> ")

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