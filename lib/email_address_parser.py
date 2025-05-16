# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, string):
        self.string = string
        
    def parse(self):
        myList = list(set(re.split(r',?\s|,\s?', self.string)))
        myList.sort()
        myList = [item for item in myList if re.match(r"^[A-z]\w+\.?\w+@[A-z]+\.[a-z]{2,3}", item)]
        return myList