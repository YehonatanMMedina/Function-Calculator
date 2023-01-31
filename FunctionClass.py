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
        self.func1=''
        self.func2=''
        self.functionParser()
    def functionParser(self):
        counter = 0

        if self.function[0] == '(':
            i=0
            while i<len(self.function)*3:

                if self.function[i%len(self.function)] == '(':
                    counter = counter + 1
                if self.function[i%len(self.function)] == ')':
                    counter = counter - 1
                if counter == 0:
                    if (i + 1)%len(self.function) != 0:
                        self.placeOfOperation = (i + 1)%len(self.function)
                        self.operation = self.function[(i + 1)%len(self.function)]
                        break
                    elif(self.function[0] == '(') and (self.function[len(self.function) - 1] == ')'):

                        self.function = self.function[1:len(self.function) - 1]
                        i=-1
                i=i+1
        x = self.startingIntLength()
        if len(self.function) != x and self.function != "x":  # if not all of the function is a number

            if x > 0 and len(self.function) > 1:
                self.placeOfOperation = x
                self.operation = self.function[x]

            if self.function[0]=='p'and self.function[1]=='i':
                if len(self.function)!=2:
                    self.placeOfOperation=2
                    self.operation = self.function[2]
            elif self.function[0]=='e':
                if len(self.function)!=1 and self.function[1]!='x':
                    self.placeOfOperation=1
                    self.operation=self.function[1]
            elif self.function[0]=='x':
                if len(self.function)!=1:
                    self.placeOfOperation=1
                    self.operation=self.function[1]
            else:

                x = self.startingStringLength()
                if x > 0:
                    self.placeOfOperation = x - 1
                    self.operation = self.function[0:x]

            isComplexFunc = False
            if x > 0:
                isComplexFunc = True

            self.func1 = self.function[0:self.placeOfOperation]
            self.func2 = self.function[self.placeOfOperation + 1:len(self.function)]

            if isComplexFunc:
                self.func1 = ''

    def newFunctionParser(self):
        counter = 0
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
                elif self.function[i].isalpha() and self.function[i]!='x' and not (self.operation == '+' or self.operation == '-') and not (self.operation == '*' or self.operation == '/'):
                    #function: get next string
                    #save operation and place of operation and use is complex like above to save func 1 and 2
            #save the functions
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
    def findDerivative(self):
        if self.function == "x":
            return "1"
        if isANumber(self.function) or self.function == "pi" or self.function == "e":
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
            return "(" + Func1.findDerivative() + ")+" + "(" + Func2.findDerivative() +")"
        if self.operation == "-":
            return "(" + Func1.findDerivative() + ")-(" + Func2.findDerivative() +")"
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

    def FRbinary_search(self, low=-10000000, high=10000000):

        # Check base case
        if high >= low:

            mid = (high + low) / 2

            # If value is exactly in the middle
            fmid=self.calcvalue(mid)
            if fmid == 0:
                return mid

            # If value is smaller than mid, then it can only
            # be present left in relation to the middle
            elif fmid > 0:
                return self.binary_search(low, mid)

            # If value is greater than mid, then it can only
            # be present right in relation to the middle
            else:
                return self.binary_search(mid, high)

        else:
            # x does not exist
            return -1

    def FRnewtonRaphson(self,x=0,epsilon=0.0000000000001):

        valueOfX = self.calcvalue(x) # f(x)
        if abs(valueOfX)<epsilon:
            return x
        derivativeFunctionStr = self.findDerivative()
        derivativeFunction = Function(derivativeFunctionStr)
        m= derivativeFunction.calcvalue(x)#derivative at x value
        b=valueOfX-m*x
        derivativeRoot = (-b)/m # where will the derivative function tuch the x acsis
        return self.FRnewtonRaphson(derivativeRoot)



fun = Function("(3)*(4)+(3)")
print(fun.calcvalue(3))
#print(fun.FRnewtonRaphson())
#print(math.sin(3+0.14159265358979303))
#print(math.sin(3))
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