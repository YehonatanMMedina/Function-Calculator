import FunctionClass


def functionParser(self):
    counter = 0

    if self.function[0] == '(':
        i = 0
        while i < len(self.function) * 3:

            if self.function[i % len(self.function)] == '(':
                counter = counter + 1
            if self.function[i % len(self.function)] == ')':
                counter = counter - 1
            if counter == 0:
                if (i + 1) % len(self.function) != 0:
                    self.placeOfOperation = (i + 1) % len(self.function)
                    self.operation = self.function[(i + 1) % len(self.function)]
                    break
                elif (self.function[0] == '(') and (self.function[len(self.function) - 1] == ')'):

                    self.function = self.function[1:len(self.function) - 1]
                    i = -1
            i = i + 1
    x = self.startingIntLength()
    if len(self.function) != x and self.function != "x":  # if not all of the function is a number

        if x > 0 and len(self.function) > 1:
            self.placeOfOperation = x
            self.operation = self.function[x]

        if self.function[0] == 'p' and self.function[1] == 'i':
            if len(self.function) != 2:
                self.placeOfOperation = 2
                self.operation = self.function[2]
        elif self.function[0] == 'e':
            if len(self.function) != 1 and self.function[1] != 'x':
                self.placeOfOperation = 1
                self.operation = self.function[1]
        elif self.function[0] == 'x':
            if len(self.function) != 1:
                self.placeOfOperation = 1
                self.operation = self.function[1]
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
