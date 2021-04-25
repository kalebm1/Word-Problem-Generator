import random

# boys_names_file = open("etc/boy-names.txt")
# girls_names_file = open("etc/girl-names.txt")
# item_file = open("etc/item-list.txt")
# times = ["day","week","month","year"]

class wordProblem():
    def __init__(self,gender="boy",t = "mult",dificulty="medium",item="apple",time = "week"):
        self.gender = gender
        self.type = t
        self.dificulty = dificulty
        self.item = item
        self.name = self.getRandomName()
        self.times = ["day","week","month","year"]
        self.time = time
        self.answer = 0


    def randomizeProblem(self):
        #Made to fully randomize the word problem components.
        gender = random.randint(0,100)
        if(gender<=49):
            self.gender = "boy"
        else:
            self.gender = "girl"
        
        typ = random.randint(0,3)
        if(typ==0):
            self.type = "add"
        elif(typ==1):
            self.type = "sub"
        elif(typ==2):
            self.type = "mult"
        elif(typ==3):
            self.type = "div"
        
        dif = random.randint(0,2)
        if(dif==0):
            self.dificulty="easy"
        elif(dif==1):
            self.dificulty="medium"
        elif(dif==2):
            self.dificulty="hard"
        
        self.item = self.getRandomItem()

        self.name = self.getRandomName()

        tim = random.randint(0,3)
        self.time = self.times[tim]

    def buildWordProblem(self):
        if(self.type=="mult"):
            #build multiply problem
            problem = self.buildMultProblem()
        elif(self.type=="add"):
            #build addition problem
            problem = self.buildAddProblem()
        elif(self.type=="sub"):
            #build subtraction problem
            problem = self.buildSubProblem()
        elif(self.type=="div"):
            #build division problem
            problem = self.buildDivProblem()
        else:
            print("Word Problem Type Not Supported: "+self.type)
        
        return problem
    
    def getGender(self):
        return self.gender
    
    def getType(self):
        return self.getType
    
    def getDif(self):
        return self.dificulty
    
    def getItem(self):
        return self.item    
    
    def getName(self):
        #put random name code here
        return self.name
    
    def getAnswer(self):
        return self.answer
    
    def setGender(self,gender):
        self.gender = gender

    def setType(self,t):
        self.type = t

    def setDif(self,dif):
        self.dificulty = dif

    def setItem(self,item):
        self.item = item
    
    def setName(self,name):
        self.name = name
    
    def getRandomItem(self):
        #put random item code here...
        item_file = open("etc/item-list.txt")
        item_list = item_file.readlines()
        item = item_list[random.randint(0,189)].rstrip("\n")
        item_file.close()
        return item

    
    def getRandomName(self):
        #put random name code here...
        boys_names_file = open("etc/boy-names.txt")
        girls_names_file = open("etc/girl-names.txt")
        retname = "lol"
        if(self.gender == "boy"):
            #get boy name here.
            boys_names = boys_names_file.readlines()
            retname = boys_names[random.randint(0,999)].capitalize().rstrip("\n")
        elif(self.gender=="girl"):
            #get girl name here.
            girls_names = girls_names_file.readlines()
            retname = girls_names[random.randint(0,999)].capitalize().rstrip("\n")
        else:
            print("Error, invalid gender specified: "+self.gender)
        
        boys_names_file.close()
        girls_names_file.close()
        return retname

    def printAllInfo(self):
        print("---------PRINTING ALL PROBLEM INFO-----------\n")
        print("Kids name = "+self.name+"\n")
        print("Kids gender = "+self.gender+"\n")
        print("Difficulty = "+self.dificulty+"\n")
        print("Item = "+self.item+"\n")
        print("Type = "+self.type+"\n")
        print("Time = "+self.time+"\n")
    
    def buildAddProblem(self):
        wordproblem = ""
        answer = 0
        num1 = self.getRandNum()
        num2 = self.getRandNum()
        answer = num1+num2
        
        wordproblem+= self.name+" has "+str(num1)+" "+self.item+". "

        if(self.gender=="boy"):
            wordproblem+="He "
        else:
            wordproblem+="She "
        
        wordproblem+="receives "+str(num2)+" from "+self.getRandomName()+". "

        wordproblem+="How many "+self.item+" does "+self.name+" have now?"
        self.answer = answer
        return wordproblem

    
    def buildSubProblem(self):
        wordproblem = ""
        answer = 0
        num1 = self.getRandNum()
        num2 = self.getRandNum()
        answer = num1-num2
        
        wordproblem+= self.name+" has "+str(num1)+" "+self.item+". "

        if(self.gender=="boy"):
            wordproblem+="He "
        else:
            wordproblem+="She "
        
        wordproblem+="takes "+str(num2)+" from "+self.getRandomName()+". "

        wordproblem+="How many "+self.item+" does "+self.name+" have now?"
        self.answer = answer
        return wordproblem
    
    def buildMultProblem(self):
        wordproblem = ""
        answer = 0
        num1 = self.getRandNum()
        num2 = self.getRandNum()
        answer = num1*num2


        wordproblem+= self.name+" has "+str(num1)+" "+self.item+". "

        if(self.gender=="boy"):
            wordproblem+="He "
        else:
            wordproblem+="She "
        
        wordproblem+="gets "+str(num2)+" times more from "+self.getRandomName()+" the next "+self.time+". "

        wordproblem+="How many "+self.item+" does "+self.name+" have now?"
        self.answer = answer

        return wordproblem
    
    def buildDivProblem(self):
        equaler = False
        wordproblem = ""
        answer = 0.0
        num1 = self.getRandNum()
        num2 = self.getRandNum()
        answer = num1/num2
        rounded = round(answer)
        if(answer==rounded):
            equaler=True
        while(not(equaler)):
            num2 = self.getRandNum()
            #code where answer never equals 1 ya dig
            # if(num1==num2):
            #     num2+=4
            answer = num1/num2
            rounded = round(answer)
            if(answer==rounded):
                equaler=True
        
        wordproblem+= self.name+" has "+str(num1)+" "+self.item+". "

        if(self.gender=="boy"):
            wordproblem+="He "
        else:
            wordproblem+="She "
        
        wordproblem+="divdes them between "+str(num2)+" of "

        if(self.gender=="boy"):
            wordproblem+="his friends. "
        else:
            wordproblem+="her friends. "

        wordproblem+="How many "+self.item+" does "+self.name+" have now?"
        self.answer = answer

        return wordproblem

    def getRandNum(self):
        if(self.dificulty=="easy"):
            return random.randint(1,20)
        elif(self.dificulty=="medium"):
            return random.randint(21,99)
        elif(self.dificulty=="hard"):
            return random.randint(100,300)
        else:
            print("Error: Difficulty not recognized: "+self.dificulty)


if __name__=='__main__':
    problem = wordProblem()
    problem.randomizeProblem()
    problem.setType("div")
    print(problem.buildWordProblem())
    print("Answer = "+str(problem.getAnswer()))
