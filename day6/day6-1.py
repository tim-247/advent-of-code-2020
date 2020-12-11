with open('day6/input', 'r') as input:
    inputlines = input.read().splitlines()
inputlines.append('')


class Quiz:
    """
    docstring
    """
    def __init__(self):
        self.answers = ''
    def addline(self, line:str):
        self.answers += line
    def getanswers(self):
        return len(set(self.answers))


quizResults = []
for line in inputlines:
    try:
        currentQuiz = currentQuiz
    except:
        currentQuiz = Quiz()
    if len(line) > 0:
        currentQuiz.addline(line)
    else:
        quizResults.append(currentQuiz)
        currentQuiz = Quiz()


print(sum([i.getanswers() for i in quizResults]))
