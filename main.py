import random

#function to run the quiz 
def harry_potter_quiz_game():
    print("Welcome to the Harry Potter Quiz Game!")

    questions = [
        {"question": "What is the name of the train that takes students to Hogwarts?",
         "options": ["A) Phoenix Express", "B) Knight Bus", "C) Thestral Express", "D) Hogwarts Express"],
         "correct_answer": "D"},
        {"question": "Who is the headmaster of Hogwarts in the first movie?",
         "options": ["A) Severus Snape", "B) Albus Dumbledore", "C) Sirius Black", "D) Gellert Grindelwald"],
         "correct_answer": "B"},
        {"question": "What is the name of Hagrid's pet dragon in 'Harry Potter and the Philosopher's Stone'?",
         "options": ["A) Norbert", "B) Smaug", "C) Drogon", "D) Falkor"],
         "correct_answer": "A"},
        {"question": "Who kills Professor Dumbledore in 'Harry Potter and the Half-Blood Prince'?",
         "options": ["A) Bellatrix Lestrange", "B) Draco Malfoy", "C) Severus Snape", "D) Lord Voldemort"],
         "correct_answer": "C"},
        {"question": "Which house does Luna Lovegood belong to?",
         "options": ["A) Gryffindor", "B) Ravenclaw", "C) Slytherin", "D) Hufflepuff"],
         "correct_answer": "B"},
    ]

    #Triggers random questions 
    random.shuffle(questions)
    points = 0

    for question_data in questions:
        print(question_data["question"])
        for option in question_data["options"]:
            print(option)
        user_answer = input("Your answer (enter A, B, C, or D): ").upper()

        if user_answer == question_data["correct_answer"]:
            print("Correct!")
            points += 2
        else:
            print(f"Wrong answer! The correct answer is {question_data['correct_answer']}. You are back to the beginning.")
            points = 0
            break
    question_data = points 
    print(f"Game Over. You scored {points} points.")

#loop the game quiz 
if __name__ == "__main__":
    while True:
        user_choice = input("Type 1 to start the game or any other key to exit: ")

        if user_choice == "1":
            harry_potter_quiz_game()
        else:
            print("Exiting the Harry Potter Quiz Game. Goodbye!")
            break
