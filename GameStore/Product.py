class Product:
    """class that holds product information"""

    _name = ""
    _price = 0.0
    _quantity = 0
    _discount = 0.0

    def __init__(self):
        self._name = ""
        self._price = 0.0
        self._quantity = 0
        self._discount = 0.0

    def __init__(self, name, price):
        self._name = name
        self._price = price
        

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getPrice(self):
        return self._price

    def setPrice(self, price):
        self._price = price

    def getQuantity(self):
        return self._quantity

    def setQuantity(self, quantity):
        self._quantity = quantity

    
    def getTotalPrice(self):        
        return self._quantity * self._price