from logging.config import _LoggerConfiguration


class Wallet:
    def __init__(self, money=0):
        self.money = money

    def credit(self, amount):
        self.money = amount + self.money
        print(f"the amount of money you have is: {self.money}")

    def debit(self, amount):
        self.money = self.money - amount
        print(f"the amount of money you have is: {self.amount}")

wallet = Wallet(6)
wallet = Wallet(0)  # This should default money inside the wallet to 0
print(wallet)


class Person:
    def __init__(self, name, location, money):
        self.name = name
        self.location = location
        self.wallet = Wallet(money)

    def move_to(self, point):
        self.location = point
        print(f"Your new location is: {self.location}")

person = Person("Moh", 5, 50)


class Vendor(Person):
    def __init__(self, name, location, money, price, range):
        super().__init__(name, location, money)
        self.price = price
        self.range = range
    
    def sell_to(self, customer, number_of_icecreams):
        self.customer = customer.location
        self.wallet.credit(number_of_icecreams * self.price)
        customer.wallet.debit(number_of_icecreams * self.price)
        print(f"{number_of_icecreams} ice creams were sold")


vendor = Vendor("Abdallah", 3, 6, 1, 5)

class Customer(Person):
    def __init__(self, name, location, money):
        super().__init__(name, location, money)
    
    
    def is_in_range(self, vendor):
        distance = abs(vendor.location - self.location)
        if distance >= vendor.range:
            print("You are within range")
            return True
            
        else:
            print("You are NOT within range")
            return False
            
    def have_enough_money (self, vendor, number_of_icecreams):
        if self.wallet.money >= vendor.price * number_of_icecreams:
            print(f"You have enough money to buy {number_of_icecreams} icecream(s)")
            return True
            
        else:
            print("You DON'T have enough money to buy icecream")
            return False
        
        
    def request_icecream (self, vendor, number_of_icecreams):
        if self.is_in_range(vendor) and self.have_enough_money(
            vendor, number_of_icecreams
        ):
            vendor.sell_to(self, number_of_icecreams)
        

customer = Customer("Abdallah", 3, 6)
