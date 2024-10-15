class IOS():
    def __init__(self):
        self.str1=""
    def get_value(self):
        self.str1 = input("Enter a word(NOT CAPITAL)")
    def print_value(self):
        print("The result is", self.str1.upper())
obj = IOS()
obj.get_value()
obj.print_value()