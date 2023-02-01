import math
def clearMinuses(str):
    for i in range(len(str)-1):
        if(str[i]=='+'):
            if str[i+1]=='-':
                str = str[0:i] + '-' + str[i+2:len(str)]
        if(str[i]=='*'):
            if str[i+1]=='-':
                x = getIntFromThisIndex(str,i+2)
                if len(x) ==0:
                    str = str[0:i] + "*(-1)" + str[i + 2 + len(x):len(str)]
                else:
                    str = str[0:i] + "*(-" + str[i+2:i+2+len(x)]+")"+str[i+2+len(x):len(str)]
    return str
def isANumber(str):
    if len(str) == 0:
        return False

    for i in range(len(str)):
        if not (str[i].isnumeric() or str[i]=='.' or(str[i] =='-' and not str[i-1].isnumeric())):
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
def getStringStartingFromThisIndex(function, i):
    n=i
    while i < len(function) and function[i].isalpha():
        i=i+1
    return function[n:i]
def getIntFromThisIndex(function, i):
    n=i
    while i < len(function) and function[i].isnumeric():
        i=i+1
    return function[n:i]
class Function:
    operation = ' '
    placeOfOperation = -1

    def __init__(self, function):
        self.function= function
        self.func1=''
        self.func2=''
        self.newFunctionParser()

    def newFunctionParser(self):
        counter = 0
        while self.canRemoveSograim():
            self.function = self.function[1:len(self.function)-1]
        if len(self.function) != 0:
            if self.function[0]=='-':
                self.function = "(" + self.function +")"

        for i in range(len(self.function)):
            if self.function[i] == "(":
                counter = counter + 1
            if self.function[i] == ")":
                counter = counter - 1
            if counter ==0:
                if self.function[i]=="+":
                    self.operation ="+"
                    self.placeOfOperation=i
                elif self.function[i]=="-":
                    self.operation ="-"
                    self.placeOfOperation=i
                elif self.function[i] =="*" and not (self.operation == '+' or self.operation == '-'):
                    self.operation = "*"
                    self.placeOfOperation = i
                elif self.function[i] =="/" and not (self.operation == '+' or self.operation == '-'):
                    self.operation = "/"
                    self.placeOfOperation = i
                elif self.function[i]=="^"  and not (self.operation == '+' or self.operation == '-') and not (self.operation == '*' or self.operation == '/'):
                    self.operation ="^"
                    self.placeOfOperation = i
                elif self.function[i].isalpha() and self.function[i]!='x' and not (self.operation == '+' or self.operation == '-') and not (self.operation == '*' or self.operation == '/') and not (self.operation=='^'):
                    candidateOperation = getStringStartingFromThisIndex(self.function,i)
                    if candidateOperation == "sin" or candidateOperation == "cos" or candidateOperation== "tan" or candidateOperation == "exp"or candidateOperation == "ln":
                        self.operation = candidateOperation
                        self.placeOfOperation = i + len(self.operation) -1
        self.func1 = self.function[0:self.placeOfOperation]
        self.func2 = self.function[self.placeOfOperation + 1:len(self.function)]

        if self.operation == "sin" or self.operation == "cos" or self.operation == "tan" or self.operation == "exp" or self.operation == "ln":
            self.func1=""


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
        if self.function == "e":
            return math.e
        if self.function == "pi":
            return math.pi
        if isANumber(self.function) :
            return float(self.function)
        if self.function[0] == "(" and self.function[len(self.function)-1]==")" and isANumber(self.function[1:len(self.function)-2]):
            return float(self.function[1:len(self.function)-1])

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
        elif self.operation == '^':
            return math.pow(float(Func1.calcvalue(x)),float(Func2.calcvalue(x)))
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
    def canRemoveSograim(self):
        counter = 0
        if len(self.function)==0:
            return False

        if self.function[0] =="(" and self.function[len(self.function)-1]==")":
            for i in range(1,len(self.function)-2):
                if self.function[i] == "(":
                    counter = counter + 1
                if self.function[i] == ")":
                    counter = counter - 1
                if counter < 0:
                    return False
            return True
    def findDerivative(self):
        if self.function == "x":
            return "1"
        if isANumber(self.function) or self.function == "pi" or self.function == "e":
            return "0"
        if isANumber(self.function[1:len(self.function)-2]) and self.function[0]=="(" and self.function[len(self.function)-1]==")":
            return "0"
        #"x^2"
        if len(self.function)==5 and self.function[0].isnumeric() and self.function[1]=="*" and self.function[2]=="x" and self.function[3]=="^" and self.function[4].isnumeric():
                return "(" + self.function[0] + +"*"+ self.function[4] + ")*" + "x^"+ str(int(self.function[4])-1)
        if len(self.function)==3 and self.function[0]=="x" and self.function[1]=="^" and self.function[2].isnumeric():
                return "(" + self.function[2]+")*x^"+ str(int(self.function[2])-1)
        if self.operation== "+"or self.operation== "-" or self.operation== "*" or self.operation== "/":
            Func1= Function(self.func1)
        Func2 = Function(self.func2)

        if self.operation == "+":
            return Func1.findDerivative() + "+" + Func2.findDerivative()
        if self.operation == "-":
            return Func1.findDerivative() + "-" + Func2.findDerivative()
        if self.operation == "*":
            return "(" + Func1.findDerivative()+")*(" + Func2.function + ")+(" + Func2.findDerivative() + ")*(" +Func1.function +")"
        if self.operation == "/":
            return "(" + "(" + Func1.findDerivative()+")*(" + Func2.function + ")-(" + Func2.findDerivative() + ")*(" +Func1.function + "))" + "/" + "((" +Func2.function+")^2)"
        if self.operation == 'ln':
            return "(" +str(1) + "/" +"("+ Func2.function + ")" + ")*"+ "(" + Func2.findDerivative() + ")"
        if self.operation == "sin":
            return "cos(" + Func2.function + ")*("+ Func2.findDerivative()+")"
        if self.operation == "cos":
            return "-sin(" + Func2.function+ ")*" + "(" + Func2.findDerivative()+ ")"
        if self.operation == "tan":
            return "(" +str(1) + "/" + "(cos("+ Func2.function+"))^2" +")" + "*" + "("+ Func2.findDerivative() +")"
        if self.operation == "sqrt":
            return "(" + Func2.findDerivative() + ")/(2*sqrt("+Func2.function+"))"
        if self.operation == "exp":
            return "("+Func2.findDerivative() + ")/(2*sqrt(" + Func2.function + "))"

    def FRbinary_search(self, low=-10000000, high=10000000,epsilon=0.001 ,counter=0):

        # Check base case
        if high >= low:

            mid = (high + low) / 2

            # If value is exactly in the middle
            fmid=self.calcvalue(mid)
            if abs(fmid) <epsilon:
                return mid

            # If value is smaller than mid, then it can only
            # be present left in relation to the middle
            elif fmid > 0:
                print(counter)
                return self.FRbinary_search(low, mid,epsilon,counter+1)

            # If value is greater than mid, then it can only
            # be present right in relation to the middle
            else:
                print(counter)
                return self.FRbinary_search(mid, high,epsilon,counter+1)

        else:
            # x does not exist
            return -1

    def FRnewtonRaphson(self,x=68,epsilon=0.000000001):

        valueOfX = self.calcvalue(x) # f(x)
        if abs(valueOfX)<epsilon:
            return x
        derivativeFunctionStr =clearMinuses(self.findDerivative())
        derivativeFunction = Function(derivativeFunctionStr)
        m= derivativeFunction.calcvalue(x)#derivative at x value
        nextx = x - valueOfX/m

        return self.FRnewtonRaphson(nextx,epsilon)

    def FRslope(self,lowx=-500,highx=705,epsilon=0.000000001,counter=0):

        lowy=self.calcvalue(lowx)
        highy=self.calcvalue(highx)
        #finding the slopes: m,b || y=mx+b
        m=(highy-lowy)/(highx-lowx)
        b= highy-m*highx
        x0 = (-b)/m # נקודת החיתוך של הישר עם ציר הx
        fx0 = self.calcvalue(x0)
        if(abs(fx0)<epsilon):
            return x0
        if fx0 > 0:
            lowx=x0
        else:
            highx=x0
        return self.FRslope(lowx,highx,epsilon,counter+1)
fun = Function("sin((-5)*4)")
print(fun.findDerivative())
    
"""


print("Welcome to my numeric analasis project")
function = input("Enter A Function:")
f= Function(function)
action=int(input("What do you want to find: 1-value, 2-derivative"))
if action == 1:
    x = input("Enter x coordinate")
    print("The value of the function at x=" +str(x)+ " is:")
    print(f.calcvalue(x))
if(action == 2):
    print("the derivative of the function is:")
    print(f.findDerivative())
"""