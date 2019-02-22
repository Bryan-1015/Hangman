'''
create a simple class
attribute = variables
method = functions usually working with attributes
'''

class CashRegister :
    global rate # Here should be the global variables. Global vars are accessible throughout the whole class
    rate = 0.078

    def __init__(self):  # after def is a space " "
        self.items = 0
        self.price = 0
        self.gold = 100

    #Methods
    def update_register(self, price):  # Important to put the
        self.items += 1
        self.price += price

    def display_register(self):
        return print("Number of items = ", self.items, "\n Total price =", self.price,'Rate of taxes', rate)

    def clean_register(self):
        CashRegister.final_price_tax(self)
        self.items = 0
        self.price = 0


    def final_price_tax(self):
        self.price = (1 + rate)*self.price
        return print('Final price,taxes included', round(self.price,2))



register1 = CashRegister()   # Don't forget ()
register1.update_register(100)
register1.update_register(29.50)
register1.update_register(2.05)
register1.display_register()
# register1.final_price_tax()
register1.clean_register()