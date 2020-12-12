from collections import Counter


with open('day6/input', 'r') as input:
    inputlines = input.read().splitlines()
inputlines.append('')


class Quiz:
    def __init__(self):
        self.answers = []
    def addline(self, line:str):
        self.answers.append(line)
    def getanswers(self):
        self.questions_answered = 0
        self.allanswers = [y for x in self.answers for y in x]
        self.countletters = Counter(self.allanswers)
        for letter in self.countletters:
            if self.countletters[letter] == len(self.answers):
                self.questions_answered += 1
        return self.questions_answered


quizResults = []
for line in inputlines:
    try:
        assert currentQuiz
    except:
        currentQuiz = Quiz()
    if len(line) > 0:
        currentQuiz.addline(line)
    else:
        quizResults.append(currentQuiz)
        currentQuiz = Quiz()


print(sum([i.getanswers() for i in quizResults]))
