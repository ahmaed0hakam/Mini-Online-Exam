import random

qFile = open("questions.txt", "r")
cFile = open("answers.txt", "r")
times = int(input("Enter the number of questions (from 1 to 21): "))
qLines = []
cLines = []
for line in qFile:
    qLines.append(line.replace("\n", ''))
for line in cFile:
    cLines.append(line.replace("\n", ''))
score = 0
rAnswer = None
mistakes = {}
questionsList = []
qNum = 1
while len(questionsList) < times:
    questionsList.append(random.choice(qLines))
    questionsList = list(set(questionsList))
for q in questionsList:
    choicesNum = 'a'
    num = int(q[:2])
    choicesList = cLines[(num - 1) * 4:(num * 4)]
    random.shuffle(choicesList)
    q = str(qNum) + q[2:]
    print("\n", q)
    for line in range(len(choicesList)):
        choicesList[line] = str(choicesNum) + ". " + choicesList[line]

        print("\t", choicesList[line].replace("*", ""))
        choicesNum = chr(ord(choicesNum) + 1)
    for line in range(len(choicesList)):
        choicesList[line] = choicesList[line].lower()
    uAnswer = input("Your answer is: ").lower()
    while ord(uAnswer) < 97 or ord(uAnswer) > 100:
        uAnswer = input("Wrong input, re-enter your choice: ").lower()
    for choice in choicesList:
        if uAnswer[0] == choice[0]:
            rAnswer = choice
            break
        else:
            rAnswer = ""
    for choice in choicesList:
        if '*' in choice:
            choice = choice.replace("*", "")
            rightAnswer = choice
    if '*' in rAnswer:
        score += 1
    else:
        mistakes[qNum] = rightAnswer
    print("==============================================================================================")
    qNum += 1
print("Your score: ", score, " of ", times)
if mistakes:
    print("==============================================================================================\n")
    print("Your mistakes and the right solutions (question number and solution, consecutively):\n")
    for key in mistakes.keys():
        print("Question number", key, ":", mistakes[key])
qFile.close()
cFile.close()
