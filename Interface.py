if self.operation == "+":
    if isANumber(Func1.function) and isANumber(Func1.function):
        return str(float(Func1.function) + float(Func2.function))
if self.operation == "-":
    if isANumber(Func1.function) and isANumber(Func2.function):
        return str(float(Func1.function) - float(Func2.function))
if self.operation == "/":
    if isANumber(Func1.function) and isANumber(Func2.function):
        return str(float(Func1.function) / float(Func2.function))
if self.operation == "*":
    if isANumber(Func1.function) and isANumber(Func2.function):
        return str(float(Func1.function) * float(Func2.function))
if self.operation == "^":
    if isANumber(Func1.function) and isANumber(Func2.function):
        return str(math.pow(float(Func1.function), float(Func2.function)))