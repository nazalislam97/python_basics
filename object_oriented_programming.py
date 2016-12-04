#!/usr/bin/env python3
# Naz-Al Islam
# Object Oriented Programming


print("Shopping Cart")
print("_" * 15)
print()

class Cart():
    
    def __init__(self, size = 0, cart = []):
        self.cart = cart
        self.size = size

    def addItem(self, item):
        self.cart.append(item)
        self.size += 1

    def showItem(self):
        print(self.cart)
        
    def prompt(self):
        item = input("Enter an item:  ")
        return item
        

#------------------------------------------------

c1 = Cart()
while True:
    order = c1.prompt()
    if order == "DONE":
        break
    c1.addItem(order)
    
c1.showItem()
