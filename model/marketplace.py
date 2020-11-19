import csv
import pandas as pd
import os
from model.order import LimitPriceOrder


# custom error to catch instancing errors
class InstanceError:
    print('Only one instance of Marketplace can exist')


# singleton pattern
class Marketplace:
    __instance = None

    @staticmethod
    def get_instance():
        if Marketplace.__instance is None:
            Marketplace()
        return Marketplace.__instance

    def __init__(self):
        try:
            Marketplace.__instance = self
            # init the lists
            # TODO: maybe add a loader to get pre startup data(?)
            self.asks = list()
            self.bids = list()
        except InstanceError:
            pass

    # def load_starting_data(self):
    #     # order_type,order_action,limit_price,timestamp,quantity
    #
    #     data = pd.read_csv('../utils/marketplace_orders.csv')
    #     order_action = data['order_action']
    #     limit_price = data['limit_price']
    #     timestamp = data['timestamp']
    #     quantity = data['quantity']
    #
    #     for i in range(0, len(data)):
    #         limit_price_order = LimitPriceOrder(order_action[i], timestamp[i], quantity[i], limit_price[i])
    #         if order_action[i] == 'ask':
    #             self.asks.append(limit_price_order)
    #         else:
    #             self.bids.append(limit_price_order)

# m = Marketplace()
# m.get_instance().load_starting_data()
# for i in range(0, 5):
#     print(m.get_instance().asks[i])
