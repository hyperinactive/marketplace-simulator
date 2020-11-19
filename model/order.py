from datetime import datetime
import enum


# order super class
class Order:
    def __init__(self, action):
        self.action = action
        self.timestamp = datetime.now()
        self.quantity = 1


# to buy/sell at the exact price
class LimitPriceOrder(Order):
    def __init__(self, action, limit_price):
        super().__init__(action)
        self.limit_price = limit_price

    # repr an str combo to define what gets printed once called in the print method
    def __repr__(self):
        return f'{self.action.upper()}: Limit: {self.limit_price}, Time: {self.timestamp}, Quantity: {self.quantity}'

    def __str__(self):
        return f'{self.action.upper()}: Limit: {self.limit_price}, Time: {self.timestamp}, Quantity: {self.quantity}'


# to buy/sell at the current market price
class MarketPriceOrder(Order):
    def __init__(self, action):
        super().__init__(action)

    def __repr__(self):
        return f'{self.action.upper()}: Limit: {self.timestamp}, Time: {self.timestamp} Quantity: {self.quantity}'

    def __str__(self):
        return f'{self.action.upper()}: {self.timestamp}, {self.quantity}'
