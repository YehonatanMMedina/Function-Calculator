import math


def isANumber(str):
    for i in range(len(str)):
        if not str[i].isnumeric():
            return False
    return True
def getStartInts(str):
    if str[0].isnumeric():
        i=0
        while i<len(str) and str[i].isnumeric():
            i=i+1
        return i
    else:
        return -1
class Function:
    operation = ' '
    placeOfOperation = -1

    def __init__(self, function):
        self.function= function
<<<<<<< HEAD
        self.func1=''
        self.func2=''
        self.functionParser()
        print(self.operation)
        print(self.func1)
        print(self.func2)

    def functionParser(self):
        counter = 0
=======
        counter =0
>>>>>>> parent of 609615a (Cleaned The constractor)

        if self.function[0] == '(':
            for i in range(len(self.function)):
                if self.function[i] == '(':
                    counter=counter+1
                if self.function[i] == ')':
                    counter=counter-1
                if counter == 0:
                    if i+1 != len(self.function):
                        self.placeOfOperation = i + 1
                        self.operation = self.function[i+1]
                    else:
                        #if (self.function[0] == '(') and (self.function[len(self.function) - 1] == ')'):
                        self.function = self.function[1:len(self.function) - 1]
                    break

        x= self.startingIntLength()
        if len(self.function)!=x and self.function!="x": #if not all of the function is a number

            if x>0 and len(self.function) >1:
                self.placeOfOperation = x
                self.operation=self.function[x]

            x = self.startingStringLength()
            if x > 0:
                self.placeOfOperation = x-1
                self.operation=self.function[0:x]

<<<<<<< HEAD
        isComplexFunc = False
        if x > 0:
            isComplexFunc = True

=======
            isComplexFunc=False
            if x>0:
                isComplexFunc = True
>>>>>>> parent of 609615a (Cleaned The constractor)

            self.func1 = self.function[0:self.placeOfOperation]
            self.func2 = self.function[self.placeOfOperation+1:len(self.function)]

<<<<<<< HEAD
        if isComplexFunc:
            self.func1 = ''

=======
            if isComplexFunc:
                self.func1=''
                
>>>>>>> parent of 609615a (Cleaned The constractor)
    def startingIntLength(self):
        if self.function[0].isnumeric():
            i=0
            while i<len(self.function) and self.function[i].isnumeric():
                i=i+1
            return i
        else:
            return -1
    def startingStringLength(self):
        if self.function[0].isalpha():
            i=0
            while self.function[i].isalpha():
                i=i+1
            return i
        else:
            return -1

    def calcvalue(self,x):
        if self.function == "x":
            return x
        if isANumber(self.function):
            return float(self.function)

        if len(self.func1)!=0:
            Func1 = Function(self.func1)
        Func2 = Function(self.func2)
        if self.operation == '+':
            return float(Func1.calcvalue(x)) + float(Func2.calcvalue(x))
        elif self.operation == '-':
            return float(Func1.calcvalue(x)) - float(Func2.calcvalue(x))
        elif self.operation == '*':
            return float(Func1.calcvalue(x)) * float(Func2.calcvalue(x))
        elif self.operation == '/':
            return float(Func1.calcvalue(x)) / float(Func2.calcvalue(x))
        elif self.operation=='ln':
            return math.log10(Func2.calcvalue(x))
        elif self.operation=='sin':
            return math.sin(Func2.calcvalue(x))
        elif self.operation == 'cos':
            return math.cos(Func2.calcvalue(x))
        elif self.operation == 'tan':
            return math.tan(Func2.calcvalue(x))
        elif self.operation == 'sqrt':
            return math.sqrt(Func2.calcvalue(x))
        elif self.operation == 'exp':
            return math.exp(Func2.calcvalue(x))
    def calcDerivative(self):
        if isANumber(self.function):
            return "0"
        if self.function == "x":
            return "1"
        #add for x^n
        if len(self.func1)!=0:
            Func1 = Function(self.func1)
        Func2 = Function(self.func2)

        if self.operation=="+":
            return Func1.calcDerivative() + " + " + Func2.calcDerivative()

fun = Function("(x)+(5)")
print(fun.calcvalue(5))
