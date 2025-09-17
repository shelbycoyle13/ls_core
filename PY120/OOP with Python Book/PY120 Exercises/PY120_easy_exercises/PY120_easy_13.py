# Reverse Engineering
# Write a class such that the following code prints the results indicated by the comments:

class Transform:
    def __init__(self, name):
        self.name = name

    def uppercase(self):
        return self.name.upper()

    @classmethod
    def lowercase(cls, str_): #I don't remember what it means to have a trailing _ LS Bot says: this is essentially to avoid naming conflicts an shadowing of built-in functions or keywords. str is already a built in function.
        return str_.lower() #Please explain this code

my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz #Is it because of this test case that it was a clue we needed to use a classmethod? i.e. because of seeing Transform call the lowercase method? LS Bot: Yes, exactly! Transform (our class) is the one calling lowercase. This syntax where we call using the class instead of the instance is only good with class methods and static methods. The method needs to be called on the class itself, so this is a class method.