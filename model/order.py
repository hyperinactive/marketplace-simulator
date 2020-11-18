from datetime import datetime


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


# to buy/sell at the current market price
class MarketPriceOrder(Order):
    def __init__(self, action):
        super().__init__(action)

