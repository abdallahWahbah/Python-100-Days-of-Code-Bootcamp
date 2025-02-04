class QuizBrain:
    def __init__(self, q_List):
        self.questionNumber = 0
        self.score = 0
        self.questionList = q_List 

    def stillHasQuestion(self):
        return self.questionNumber < len(self.questionList)

    def nextQuestion(self):
        currentQuestion = self.questionList[self.questionNumber]
        self.questionNumber += 1
        answer = input(f'Q.{self.questionNumber}: {currentQuestion.text} (True/False) ')
        self.checkAnswer(answer, currentQuestion.answer)

    def checkAnswer(self, userAnswer, correctAnswer):
        if userAnswer.lower() == correctAnswer.lower():
            print("You got it right!")
            self.score += 1 
        else:
            print(f"That is wrong, the corrent answer was {correctAnswer}")
        print(f'Your current score is: {self.score}/{self.questionNumber}')
        print('\n')

