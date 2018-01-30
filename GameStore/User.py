
class User:
    """class that holds user information"""
    _name = ""
    _phoneNum = ""
    _postalCode = ""
    

    def __init__(self):
        self._name = ""
        self._phoneNum = ""
        self._postalCode = ""
        

    

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getPhoneNum(self):
        return self._phoneNum

    def setPhoneNum(self, phoneNum):
        self._phoneNum = phoneNum

    def getPostalCode(self):
        return self._postalCode

    def setPostalCode(self, postalCode):
        self._postalCode = postalCode

   