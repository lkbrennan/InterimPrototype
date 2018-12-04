import random
class mathsquiz:
    def run(self):
        print("Please enter in a difficulty")
        print("easy\nmedium\nhard")
        self.difficulty=input(">>>")

        self.lengthquiz=input("Please enter the desired number of questions >>> ")

        self.setDifficulty(self.difficulty)
        
        for x in range(0,int(self.lengthquiz)):
            print("Question " + str(x+1) + " out of " + self.lengthquiz)
            self.createSum()

        self.percentage = (self.correctcount/int(self.lengthquiz))*100
        print("Amount of correct Answers was " + str(self.correctcount) + "/" + str(self.lengthquiz))
        print("Percentage of correct answers was " + str(self.percentage) +"%")

        self.runagain = input("Would you like to play again? y/n >>> ")

        if(self.runagain == "y"):
            mathsquiz()

        if(self.runagain == "n"):
            print("Bye! Thanks for playing!")

    def setDifficulty(self,difficulty):

        if(difficulty == "easy"):
            self.minnum = 1
            self.maxnum = 99
            self.operator=[]
            self.operator.append("+")
            self.operator.append("-")

        if (difficulty == "medium"):
            self.minnum = 1
            self.maxnum = 99
            self.operator = []
            self.operator.append("+")
            self.operator.append("-")
            self.operator.append("x")

        if (difficulty == "hard"):
            self.minnum = 1
            self.maxnum = 999
            self.operator = []
            self.operator.append("+")
            self.operator.append("-")
            self.operator.append("x")
            self.operator.append("/")

    def switch(self,a,b):
        return {
            '+': a+b,
            '-': a-b,
            'x': a*b,
            '/': a/b
        }.get(self.op,"error")

    def createSum(self):
        self.num1 = self.getNumbers()
        self.num2 = self.getNumbers()
        self.op = self.operator[self.getOperator()]

        if(self.num2>self.num1):
            self.correctAns = self.switch(self.num2,self.num1)
            print(str(self.num2)+self.op+str(self.num1))

        else:
            self.correctAns = self.switch(self.num1,self.num2)
            print(str(self.num1)+self.op+str(self.num2))

        self.givenAns = input("Whats your answer? >>> ")

        if(int(self.givenAns) == self.correctAns):
            self.correctcount+=1
            print("Congrats, that was correct!")

        else:
            print("Wrong Answer!")
            print("Correct Answer is " + str(self.correctAns))
        

    def getNumbers(self):
        return random.randint(self.minnum,self.maxnum)

    def getOperator(self):
        j = random.randint(0,len(self.operator)-1)
        return j 
        
    def __init__(self):
        self.operator = []
        self.num1,self.num2,self.maxnum,self.minnum, self.lengthquiz = 0,0,0,0,0
        self.correctAns,self.givenAns, self.correctcount,self.percentage= 0,0,0,0
        self.op=""
        self.difficulty=""
        self.runagain=""
        self.run()

mathsquiz()        
