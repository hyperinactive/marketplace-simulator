from model.app_states import states
from model.marketplace import Marketplace
from model.order import LimitPriceOrder
from controller.core_logic import idle
import pandas as pd


# core tracks states and controls the Trader and Order Matcher
class Core(object):

    def __init__(self):
        # set the default state and start the default function
        self.state = states.Idle()
        # init the marketplace
        print('Initializing the marketplace instance')
        self.market = Marketplace()

        idle(self)

    # function to change states
    def change(self, state):
        # change state
        self.state.switch(state)

    # NOTE: originally from marketplace module
    # pandas path problems
    # works within the directory, but not when invoked outside, minus the root directory
    def load(self):
        # order_type,order_action,limit_price,timestamp,quantity

        data = pd.read_csv('utils/marketplace_orders.csv')
        order_action = data['order_action']
        limit_price = data['limit_price']
        timestamp = data['timestamp']
        quantity = data['quantity']

        for i in range(0, len(data)):
            limit_price_order = LimitPriceOrder(order_action[i], timestamp[i], quantity[i], limit_price[i])
            if order_action[i] == 'ask':
                self.market.get_instance().asks.append(limit_price_order)
            else:
                self.market.get_instance().bids.append(limit_price_order)
