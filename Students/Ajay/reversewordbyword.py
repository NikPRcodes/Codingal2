class Reverse:
    sentence = ""
    def __init__(self, y = ["Ajay", "am","I", "Hello"]):
        self.y = y
    def reverse(self):
        for i in self.y:
            rev = i[::-1]
            self.sentence = self.sentence + rev + " "
        return self.sentence
obj = Reverse()
print(obj.reverse())