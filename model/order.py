from datetime import datetime


# order super class
# TODO: cannot instantiate an Order object without providing it with all the args
#   default args in python work strangely :(
class Order:
    def __init__(self, action, timestamp, quantity):
        self.action = action
        self.quantity = quantity
        self.timestamp = timestamp


# to buy/sell at the exact price
class LimitPriceOrder(Order):
    def __init__(self, action, timestamp, quantity, limit_price):
        super().__init__(action, timestamp, quantity)
        self.limit_price = limit_price

    # •The sort routines are guaranteed to use __lt__() when making comparisons between two objects
    # sorted()
    def __eq__(self, other):
        return self.limit_price == other.limit_price \
               and self.timestamp == other.timestamp \
               and self.action == other.action

    # rich comparisons
    # if prices match, compare timestamps
    def __lt__(self, other):
        if isinstance(other, LimitPriceOrder):
            if self.limit_price == other.limit_price:
                return self.timestamp < other.timestamp
            else:
                return self.limit_price < other.limit_price

    # repr an str combo to define what gets printed once called in the print method
    def __repr__(self):
        return f'{self.action.upper()}: Limit: {self.limit_price}, Time: {self.timestamp}, Quantity: {self.quantity}'

    def __str__(self):
        return f'{self.action.upper()}: Limit: {self.limit_price}, Time: {self.timestamp}, Quantity: {self.quantity}'


# to buy/sell at the current market price
class MarketPriceOrder(Order):
    def __init__(self, action, timestamp, quantity):
        super().__init__(action, timestamp, quantity)

    def __repr__(self):
        return f'{self.action.upper()}: Limit: {self.timestamp}, Time: {self.timestamp} Quantity: {self.quantity}'

    def __str__(self):
        return f'{self.action.upper()}: {self.timestamp}, {self.quantity}'
