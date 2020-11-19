from datetime import datetime
import enum


# order super class
class Order:
    def __init__(self, action, timestamp, quantity):
        self.action = action
        self.quantity = quantity or 1
        self.timestamp = timestamp or datetime.now()


# to buy/sell at the exact price
class LimitPriceOrder(Order):
    def __init__(self, action, timestamp, quantity, limit_price):
        super().__init__(action, timestamp, quantity)
        self.limit_price = limit_price

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
