from enum import Enum, auto

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.core.window import Window

Builder.load_file("box.kv")

Window.size = (400, 600)


class Action(Enum):
    DIV = auto()
    MULT = auto()
    MINUS = auto()
    PLUS = auto()


def addingNumbers(number: float, strNumber: str, digit: int):
    """
        this function help to add digit to number and string representation of a number
        return number and strNumber
    """
    if number == 0:
        strNumber = str(digit)
    else:
        strNumber += str(digit)
    number = float(strNumber)
    return number, strNumber


class MyLayout(Widget):

    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        """
            there are we declare:
            number - which is our main number
            stringNumber - string representation of a number1
            number2 - which is our additional number
            stringNumber2 - string representation of a number2
            turnNumber - decide what number choose: main or additive
            numberLabel - label which shows current number
        """
        self.stringNumber = "0"
        self.number = 0
        self.stringNumber2 = "0"
        self.number2 = 0
        self.turnNumber = False  # if False - choosing first Number, if True - choosing second Number
        self.currentAction = None
        self.ids.numberLabel.text = self.stringNumber

    def buttonClearPress(self):
        # self.ids.numberLabel.text = "Ready!"
        self.stringNumber = "0"
        self.number = 0
        self.stringNumber2 = "0"
        self.number2 = 0
        self.turnNumber = False
        self.ids.numberLabel.text = self.stringNumber

    def buttonSquarePress(self):
        self.number = self.number ** 2
        self.stringNumber = str(self.number)
        self.ids.numberLabel.text = self.stringNumber

    def buttonSqrtPress(self):
        self.number = self.number ** 0.5
        self.number = round(self.number, 3)
        self.stringNumber = str(self.number)
        self.ids.numberLabel.text = self.stringNumber

    def buttonDivPress(self):
        if not self.turnNumber:
            self.turnNumber = True
            self.currentAction = Action.DIV
        elif self.turnNumber:
            self.number = self.number / self.number2
            self.stringNumber = str(self.number)
            self.ids.numberLabel.text = self.stringNumber
            self.number2 = 0
            self.stringNumber2 = "0"
            self.currentAction = Action.DIV
            self.turnNumber = True

    def button7Press(self):
        if not self.turnNumber:
            self.number, self.stringNumber = addingNumbers(self.number, self.stringNumber, 7)
            self.ids.numberLabel.text = self.stringNumber
        else:
            self.number2, self.stringNumber2 = addingNumbers(self.number2, self.stringNumber2, 7)
            self.ids.numberLabel.text = self.stringNumber2

    def button8Press(self):
        if not self.turnNumber:
            self.number, self.stringNumber = addingNumbers(self.number, self.stringNumber, 8)
            self.ids.numberLabel.text = self.stringNumber
        else:
            self.number2, self.stringNumber2 = addingNumbers(self.number2, self.stringNumber2, 8)
            self.ids.numberLabel.text = self.stringNumber2

    def button9Press(self):
        if not self.turnNumber:
            self.number, self.stringNumber = addingNumbers(self.number, self.stringNumber, 9)
            self.ids.numberLabel.text = self.stringNumber
        else:
            self.number2, self.stringNumber2 = addingNumbers(self.number2, self.stringNumber2, 9)
            self.ids.numberLabel.text = self.stringNumber2

    def buttonMultPress(self):
        if not self.turnNumber:
            self.turnNumber = True
            self.currentAction = Action.MULT
        if self.turnNumber:
            self.number = self.number * self.number2
            self.stringNumber = str(self.number)
            self.ids.numberLabel.text = self.stringNumber
            self.number2 = 0
            self.stringNumber2 = "0"
            self.currentAction = Action.MULT
            self.turnNumber = True

    def button4Press(self):
        if not self.turnNumber:
            self.number, self.stringNumber = addingNumbers(self.number, self.stringNumber, 4)
            self.ids.numberLabel.text = self.stringNumber
        else:
            self.number2, self.stringNumber2 = addingNumbers(self.number2, self.stringNumber2, 4)
            self.ids.numberLabel.text = self.stringNumber2

    def button5Press(self):
        if not self.turnNumber:
            self.number, self.stringNumber = addingNumbers(self.number, self.stringNumber, 5)
            self.ids.numberLabel.text = self.stringNumber
        else:
            self.number2, self.stringNumber2 = addingNumbers(self.number2, self.stringNumber2, 5)
            self.ids.numberLabel.text = self.stringNumber2

    def button6Press(self):
        if not self.turnNumber:
            self.number, self.stringNumber = addingNumbers(self.number, self.stringNumber, 6)
            self.ids.numberLabel.text = self.stringNumber
        else:
            self.number2, self.stringNumber2 = addingNumbers(self.number2, self.stringNumber2, 6)
            self.ids.numberLabel.text = self.stringNumber2

    def buttonMinusPress(self):
        if not self.turnNumber:
            self.turnNumber = True
            self.currentAction = Action.MINUS
        if self.turnNumber:
            self.number = self.number - self.number2
            self.stringNumber = str(self.number)
            self.ids.numberLabel.text = self.stringNumber
            self.number2 = 0
            self.stringNumber2 = "0"
            self.currentAction = Action.MINUS
            self.turnNumber = True

    def button1Press(self):
        if not self.turnNumber:
            self.number, self.stringNumber = addingNumbers(self.number, self.stringNumber, 1)
            self.ids.numberLabel.text = self.stringNumber
        else:
            self.number2, self.stringNumber2 = addingNumbers(self.number2, self.stringNumber2, 1)
            self.ids.numberLabel.text = self.stringNumber2

    def button2Press(self):
        if not self.turnNumber:
            self.number, self.stringNumber = addingNumbers(self.number, self.stringNumber, 2)
            self.ids.numberLabel.text = self.stringNumber
        else:
            self.number2, self.stringNumber2 = addingNumbers(self.number2, self.stringNumber2, 2)
            self.ids.numberLabel.text = self.stringNumber2

    def button3Press(self):
        if not self.turnNumber:
            self.number, self.stringNumber = addingNumbers(self.number, self.stringNumber, 3)
            self.ids.numberLabel.text = self.stringNumber
        else:
            self.number2, self.stringNumber2 = addingNumbers(self.number2, self.stringNumber2, 3)
            self.ids.numberLabel.text = self.stringNumber2

    def buttonPlusPress(self):
        if not self.turnNumber:
            self.turnNumber = True
            self.currentAction = Action.PLUS
        if self.turnNumber:
            self.number = self.number + self.number2
            self.stringNumber = str(self.number)
            self.ids.numberLabel.text = self.stringNumber
            self.number2 = 0
            self.stringNumber2 = "0"
            self.currentAction = Action.PLUS
            self.turnNumber = True

    def buttonChangeSignPress(self):
        if not self.turnNumber:
            if self.number > 0:
                self.number *= -1
                self.stringNumber = "-" + self.stringNumber
            elif self.number < 0:
                self.number *= -1
                self.stringNumber = self.stringNumber[1:]
            self.ids.numberLabel.text = self.stringNumber
        if self.turnNumber:
            if self.number2 > 0:
                self.number2 *= -1
                self.stringNumber2 = "-" + self.stringNumber2
            elif self.number2 < 0:
                self.number2 *= -1
                self.stringNumber2 = self.stringNumber2[1:]
            self.ids.numberLabel.text = self.stringNumber2

    def button0Press(self):
        if not self.turnNumber and self.number != 0:
            self.number, self.stringNumber = addingNumbers(self.number, self.stringNumber, 0)
            self.ids.numberLabel.text = self.stringNumber
        else:
            if self.number != 0:
                self.number2, self.stringNumber2 = addingNumbers(self.number2, self.stringNumber2, 0)
                self.ids.numberLabel.text = self.stringNumber2

    def buttonDotPress(self):
        if not self.turnNumber:
            if not "." in self.stringNumber:
                self.stringNumber += "."
                self.number = str(self.stringNumber)
                self.ids.numberLabel.text = self.stringNumber
        if self.turnNumber:
            if not "." in self.stringNumber2:
                self.stringNumber2 += "."
                self.number2 = str(self.stringNumber2)
                self.ids.numberLabel.text = self.stringNumber2

    def buttonEqualPress(self):
        if self.turnNumber:
            if self.currentAction == Action.DIV:
                if self.number2 != 0:
                    self.number = self.number / self.number2
                    if len(str(self.number)) > 10:
                        self.number = round(self.number, 9)
                    self.stringNumber = str(self.number)
                    self.ids.numberLabel.text = self.stringNumber
                    self.number2 = 0
                    self.stringNumber2 = "0"
                    self.currentAction = None
                    self.turnNumber = False

            if self.currentAction == Action.MULT:
                self.number = self.number * self.number2
                if len(str(self.number)) > 10:
                    self.number = round(self.number, 9)
                self.stringNumber = str(self.number)
                self.ids.numberLabel.text = self.stringNumber
                self.number2 = 0
                self.stringNumber2 = "0"
                self.currentAction = None
                self.turnNumber = False

            if self.currentAction == Action.MINUS:
                self.number = self.number - self.number2
                if len(str(self.number)) > 10:
                    self.number = round(self.number, 9)
                self.stringNumber = str(self.number)
                self.ids.numberLabel.text = self.stringNumber
                self.number2 = 0
                self.stringNumber2 = "0"
                self.currentAction = None
                self.turnNumber = False

            if self.currentAction == Action.PLUS:
                self.number = self.number + self.number2
                if len(str(self.number)) > 10:
                    self.number = round(self.number, 9)
                self.stringNumber = str(self.number)
                self.ids.numberLabel.text = self.stringNumber
                self.number2 = 0
                self.stringNumber2 = "0"
                self.currentAction = None
                self.turnNumber = False

# def resourcePath():
#     '''Returns path containing content - either locally or in pyinstaller tmp file'''
#     if hasattr(sys, '_MEIPASS'):
#         return os.path.join(sys._MEIPASS)
#
#     return os.path.join(os.path.abspath("."))


class AwesomeApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    AwesomeApp().run()
