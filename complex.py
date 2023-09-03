class Complex:
    def __init__(self,realp=0,imagp=0):
        self.realp = realp
        self.imagp = imagp

    def setComplex(self,realp,imagp):
        self.realp = realp
        self.imagp = imagp
    
    def readComplex(self):
        self.realp = int(input("Enter the real part :"))
        self.imagp = int(input("Enter the imaginary part :"))

    def showComplex(self):
        print('(',self.realp,')','+i','(',self.imagp,')',sep='')

    def addComplex(self,c2):
        c3 = Complex()
        c3.realp = self.realp + c2.realp
        c3.imagp = self.imagp + c2.imagp
        return c3
    

def add2Complex(a,b):
    c = a.addComplex(b)
    return c

compList = []

def main():
    n = int(input("Enter the value for N :"))
    for i in range(n):
        print("Object",i+1)
        obj = Complex()
        obj.readComplex()
        compList.append(obj)

    print("\n Entered Complex no. are :")
    for obj in compList:
        obj.showComplex()

    sumObj = Complex()
    for obj in compList:
        sumObj = add2Complex(sumObj,obj)

    print("\n Sum of N complex numbers is",end='')
    sumObj.showComplex()

main()