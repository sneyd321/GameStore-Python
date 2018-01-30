from User import *
from Product import *
from Bill import *

#initialize objects
_user = User()
    
product1 = Product("Mario Kart 8", 49.99)
product2 = Product("Super Mario 3d World", 59.99)
product3 = Product("Legend Of Zelda: Breath of the Wild", 79.99)
product4 = Product("Mario Party 10", 39.99)
product5 = Product("Donkey Kong Country: Tropical Freeze", 59.99)

_bill = Bill()


def validatePhoneNumber(string):
    """function to validate whether the phone number was enter correctly. Returns str"""
    while True:
        try:
            #get the input from user
            phoneNum = int(input(string))
            #convert to string
            phoneNum = str(phoneNum)
            #if the length of the input is 10
            if len(phoneNum) == 10:
                #split str to properly format the phone number
                areaCode = phoneNum[:3]
                prefix = phoneNum[3:-4]
                line = phoneNum[6:]
                #format the number
                number = areaCode + "-" + prefix + "-" + line
                break
            #if phone number isnt long enough
            else:
                print("Invalid phone number please enter in this format: 1234567890")
                continue
        #if not a number was entered
        except ValueError:
            print("Invalid phone number. Please enter in this format: 1234567890")
            continue
    #return str
    return number   
    

def validatePostalCode(string):
    """Validates the postal code. Returns str"""
    while True:
        #get input from user 
        postalCode = input(string)
        #check if the postal code is length 7
        if len(postalCode) == 7:      
            return postalCode
        #otherwise prompt user again 
        else:
            print("Invalid postal code. Please enter in this format: A0A 0A0")
            continue
        
def validateName(string):
    """validates the name of the user. Returns a str"""
    while True:
        #get name from user
        name = input(string)
        #if name is less than 20 characters
        if len(name) < 20:
            return name
        #otherwise prompt user again
        else:
            print("Invalid name. Please enter a name smaller than 20 characters")
            continue

def askQuantity(string):ity
    """validate the user input for quantity of products. Returns int"""
    while True:
        try:
            #get input from user
            quantity = int(input(string))
            #if the quantity is between 0 and 100
            if quantity < 0 or quantity > 100:
                print("Please enter a value between 0 and 100")
                continue
            break
        #if the value is not a number
        except ValueError:
            print("Please enter a whole number.")
            continue
    #return quantity
    return quantity


def showItems(product):
    """prompt user and set quantity of products"""
    print("First we have ", product.getName(), " for $", product.getPrice(), sep="") 
    product.setQuantity(askQuantity("How many would you like? "))

def askDiscount(string):
    """ask user for their discount and validate it. returns int"""
    while True:
        try:
            #get input from user
            discount = int(input(string))
            break
        #if the input isnt a number
        except ValueError:
            print("Please enter a whole number.")
            continue
    #return discount
    return discount


print("Hello and welcome to this on-line game store.")
#ask user their name
_user.setName(validateName("Please tell me your name: "))
#ask user their phone number
_user.setPhoneNum(validatePhoneNumber("Please Enter your phone number: "))
#ask user their postal code
_user.setPostalCode(validatePostalCode("Please enter your postal code: "))

#show user the available items and ask how many they want
showItems(product1)
showItems(product2)
showItems(product3)
showItems(product4)
showItems(product5)

#Calculate the value of the discount
_bill.setDiscount(askDiscount("What is your discount? (0 - 100%): "))

#calculate discount
discountValue = _bill.calcDiscount()

#Calculate the subtotal for each item
_bill.calcSubtotal1(product1.getTotalPrice())
_bill.calcSubtotal1(product2.getTotalPrice())
_bill.calcSubtotal1(product3.getTotalPrice())
_bill.calcSubtotal1(product4.getTotalPrice())
_bill.calcSubtotal1(product5.getTotalPrice())

#Output
print("==============================================================================")
print("|",'{:>36}'.format("RS Games"),"|", '{:>0}'.format("Customer:"), '{:>25}'.format(_user.getName()), "|")
print("|",'{:>36}'.format("www.rsgames.com"),"|",'{:>35}'.format(_user.getPhoneNum()), "|")
print("|",'{:>38}'.format("|"), '{:>35}'.format(_user.getPostalCode()), "|")
print("|============================================================================|")
print("|",'{:>36}'.format("PRODUCT"),"|",'{:>8}'.format("QUANTITY"),"|",'{:>10}'.format("UNIT PRICE"),"|",'{:>10}'.format("TOTAL PRICE"),"|" )
print("|",'{:>36}'.format(product1.getName()),"|",'{:>8}'.format(product1.getQuantity()),"|",'{:>10}'.format(product1.getPrice()),"|",'{:>11}'.format(round(product1.getTotalPrice(),2)),"|" )
print("|",'{:>36}'.format(product2.getName()),"|",'{:>8}'.format(product2.getQuantity()),"|",'{:>10}'.format(product2.getPrice()),"|",'{:>11}'.format(round(product2.getTotalPrice(),2)),"|" )
print("|",'{:>36}'.format(product3.getName()),"|",'{:>8}'.format(product3.getQuantity()),"|",'{:>10}'.format(product3.getPrice()),"|",'{:>11}'.format(round(product3.getTotalPrice(),2)),"|" )
print("|",'{:>36}'.format(product4.getName()),"|",'{:>8}'.format(product4.getQuantity()),"|",'{:>10}'.format(product4.getPrice()),"|",'{:>11}'.format(round(product4.getTotalPrice(),2)),"|" )
print("|",'{:>36}'.format(product5.getName()),"|",'{:>8}'.format(product5.getQuantity()),"|",'{:>10}'.format(product5.getPrice()),"|",'{:>11}'.format(round(product5.getTotalPrice(),2)),"|" )
print("|----------------------------------------------------------------------------|")
print("|", '{:>60}'.format("Sub Total 1"),"|",'{:>11}'.format(_bill.getSubtotal1()),"|")
print("|", '{:>60}'.format("H.S.T"),"|",'{:>11}'.format(round(_bill.calcHST(), 2)),"|")
print("|", '{:>60}'.format("Sub Total 2"),"|",'{:>11}'.format(round(_bill.calcSubtotal2(), 2)),"|")
print("|", '{:>60}'.format("Discount"),"|",'{:>11}'.format(round(_bill.getDiscount(), 2)),"|")
print("|", '{:>60}'.format("Amount Due"),"|",'{:>11}'.format(round(_bill.calcTotalAmount(), 2)),"|")
print("|============================================================================|")






