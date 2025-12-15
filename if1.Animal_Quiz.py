import random

#Quiz:data: 5 Questions about animals #

questions =[
    {"question": "Which species of rhinoceros is currently classified as critically endangered?",
     "options":["Red Rhinoceros","Black Rhinoceros", "Indian Rhinoceros", "White Rhinoceros"],
     "answer":"White Rhinoceros"
     },
     {"question": "What is the tortoise famous for having on its back?",
      "options":["scales", "feathers","shell", "carapace"],
      "answer":"shell"
     },
     {"question": "What animal is known as the king of the jungle?",
     "options":["Tiger", "Lion", "Elephant","Bear"],
     "answer":"Lion"
     },
     {"question":"Which animal is the fastest land animal?",
      "options":["Cheater","Leopar","Bear","Dog"],
      "answer":"Cheater"
     },
     {"question":"What animal changes its colour to blend in with nature?",
      "options":[ "Gecko","Lizard", "Chameleon", "Cobra"],
      "answer":"Chameleon"}

]
#Writing the functions#

def ask_questions(q_data):
    """Ask a question with multiple choice options"""
    print("\n" + q_data["question"])
    for i, option in enumerate(q_data["options"], start=1):
        print(f"{i}. {option}")
        choice = input("enter the number of your choice (1-4): ")

        #using if, else, elif#
        if choice =="1":
            selected =q_data["options"][0]
        elif choice =="2":
            selected =q_data ["options"][1]
        elif choice =="3":
            selected =q_data ["options"][2]
        elif choice =="4":
            selected =q_data ["options"][3]
        else:
         print("Invald choice! please enter 1-4.")
         return False
        if selected.Lower()== q_data["answer"].lower():
            print("correct")
            return True
        else:
            print(f" Wrong! The correct answer is {q_data["answer"]}.")
            return False
        def run_quiz():
        #Run the quiz with multiple choice questions.#
            print("  Welcome to the Animal quiz!,  \n")
        score -0

        random.shuffle(questions)
        for q in questions:
            if ask_questions(q):
             score +=1
        print(f"\nYour final score: {score}/{len(questions)}")

        #main program#
        if __name__ =="__main__":
            run_quiz()
    
