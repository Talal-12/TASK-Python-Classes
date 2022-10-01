from logging.config import _LoggerConfiguration


class Wallet:
    def __init__(self, money):
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
        self.customer = customer
        self.number_of_icecreams = number_of_icecreams
        Vendor.location = Customer.location
        Customer.debit(number_of_icecreams * Vendor.price)
        Vendor.credit(number_of_icecreams * Vendor.price)
        print(f"{number_of_icecreams} ice creams were sold")


vendor = Vendor("Abdallah", 3, 6, 1, 5)

class Customer(Person):
    def __init__(self, name, location, money):
        super().__init__(name, location, money)
    
    
    def is_in_range(self, vendor):
        self.vendor = vendor
        if abs(self.location - Vendor.location) >= Vendor.range:
            True
            print("You are within range")
        else:
            print("You are NOT within range")

    def have_enough_money (self, vendor, number_of_icecreams):
        self.vendor = vendor
        self.number_of_icecreams = number_of_icecreams
        number_of_icecreams = self.wallet / Vendor.price
        if number_of_icecreams >= 1:
            True
            print(f"You have enough money to buy {number_of_icecreams} icecream(s)")
        else:
            print("You DON'T have enough money to buy icecream")
        
    def request_icecream (self, vendor, number_of_icecreams):
        self.number_of_icecreams = number_of_icecreams
        self.vendor = vendor
        number_of_icecreams = input("How many icecreams would you like to buy?: ")
        if Customer.is_in_range and Customer.have_enough_money is True:
            Vendor.sell_to(customer, number_of_icecreams)
            print(f"A request to buy {number_of_icecreams} has been made")
        else:
            print("Your request cannot be made")


customer = Customer("Abdallah", 3, 6)
