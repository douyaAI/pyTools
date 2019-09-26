class Question:
    def __init__(self, filename):
        self.index = 0
        self.questions = self.parse(filename)

    def getQuestion(self):
        i = self.index
        self.index = (self.index + 1) % len(self.questions)
        return self.questions[i]

    def parse(self, filename):
        result = []
        data = open(filename, 'r')
        for line in data:
            result.append(line)
        return result


