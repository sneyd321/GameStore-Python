class Bill:
    """class that holds bill information"""
    _discount = 0.0
    HST = .13 #Constant
    _subtotal1 = 0.0
    _subtotal2 = 0.0
    _finalAmount = 0.0


    def __init__(self):
        self._discount = 0.0
        self._subtotal1 = 0.0
        self._subtotal2 = 0.0
        self._finalAmount = 0.0

    def getDiscount(self):
        return self._discount

    def setDiscount(self, discount):
        self._discount = discount

    def getSubtotal1(self):
        return self._subtotal1

    def setSubtotal1(self, subtotal):
        self._subtotal1 = subtotal

    def getSubtotal2(self):
        return self._subtotal2

    def setSubtotal2(self, subtotal):
        self._subtotal2 = subtotal

    def getFinalAmount(self):
        return self._finalAmount

    def setFinalAmount(self, amount):
        self._finalAmount = amount

    def calcDiscount(self):
        self._discount = round(self._discount/100, 2)

    def calcSubtotal1(self, price):
        self._subtotal1 += price
        

    def calcHST(self):
        return self._subtotal1 * self.HST

    def calcSubtotal2(self):
        self._subtotal2 = self.calcHST() + self._subtotal1
        return self._subtotal2

    def calcTotalAmount(self):
        discount = self._discount * self._subtotal2
        self._finalAmount = self._subtotal2 - discount
        return self._finalAmount