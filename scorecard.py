class Student:
    def __init__(self,name="",usn="",score=[0,0,0,0]):
        self.name = name
        self.usn = usn
        self.score = score

    def getMarks(self):
        self.name = input("Enter student name :")
        self.usn = input("Enter student usn :")
        self.score[0] = int(input("Enter marks in Subject 1 :"))
        self.score[1] = int(input("Enter marks in Subject 2 :"))
        self.score[2] = int(input("Enter marks in Subject 3 :"))
        self.score[3] = self.score[0] + self.score[1] + self.score[2]

    def display(self):
        percentage = self.score[3]/3
        spcstr = '='*81
        print(spcstr)
        print("SCORE CARD DETAILS".center(81))
        print(spcstr)
        print("%15s"%("NAME"),"%12s"%("USN"),"%8s"%("MARKS 1"),"%8s"%("MARKS 2"),"%8s"%("MARKS 3"),"%8s"%("TOTAL"),"%12s"%("PERCENTAGE"))
        print(spcstr)
        print("%15s"%(self.name),"%12s"%(self.usn),"%8s"%(self.score[0]),"%8s"%(self.score[1]),"%8s"%(self.score[2]),"%8s"%(self.score[3]),"%12s"%("%.2f"%(percentage)))
        print(spcstr)

def main():
    S1 = Student()
    S1.getMarks()
    S1.display()

main()    
