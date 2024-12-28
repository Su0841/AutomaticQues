import csv
from itertools import islice
from random import shuffle

def AnswerCheck(answer, CorrectAnswer):
    if answer != CorrectAnswer:
        print("SAI")
        print(f"Câu trả lời đúng: {CorrectAnswer}")
        print("-------------------------------------------------------------------------------------------")
        print("-------------------------------------------------------------------------------------------")

def MultChoice(start, end):
    QUES = "ques"
    RIGHT = "right"
    ANSWERS = "answers"
    LETTERS = ["A", "B", "C","D"]

    with open("/workspaces/170288548/ques/LS_MC.csv", newline='') as data:
        reader = list(islice(csv.DictReader(data), start, end))
        shuffle(reader)

        for i, row in enumerate(reader, start=1):
            print(f"{i}.{row[QUES]}")

            correct = None
            choices = row[ANSWERS].split(";")
            shuffle(choices)
            for j, choice in enumerate(choices):
                if choice == row[RIGHT]:
                    correct = LETTERS[j]

                print(f"{LETTERS[j]}. {choice}")

            AnswerCheck(input("Answear: ").upper(), correct)
            print()

def TrueFalse(start, end):
    TOPIC = "topic"
    ANSWER = "answers"
    STATEMENTS = "statements"
    RO_NUMS = ["I", "II", "III", "IV"]

    with open("/workspaces/170288548/ques/LS_TF.csv", newline='') as data:
        reader = list(islice(csv.DictReader(data), start, end))
        shuffle(reader)

        for i, row in enumerate(reader, start=1):
            print(f"{i}.{row[TOPIC]}")

            questions = []
            statements = row[STATEMENTS].split(";")
            answers = row[ANSWER].split(";")
            for j in range(4):
                questions.append({"statement": statements[j], "answer": answers[j]})

            shuffle(questions)
            for j, ques in enumerate(questions):
                print(f"{RO_NUMS[j]}. {ques.get("statement")}")
                AnswerCheck(input("Answear: "), ques.get("answer"))

            print()
        print()

if __name__ == "__main__":
    print("Multiple Choice (1) or True False (2) or ALL (3)")
    type = int(input("Type: "))

    if type != 3:
        FROM = int(input("Từ câu: ")) - 1
        TO = int(input("Đến câu: "))

        if type == 1:
            MultChoice(FROM, TO)
        else:
            TrueFalse(FROM, TO)

    else:
        MultChoice(0, 35)
        TrueFalse(0, 6)

