from model.app_states import states
from model import marketplace
from sys import exit
from controller.core_logic import idle


# core tracks states and controls the Trader and Order Matcher
class Core(object):

    def __init__(self):
        # set the default state and start the default function
        self.state = states.Idle()
        # self.idle()
        idle(self)

        # init the marketplace
        print('Initializing the marketplace instance')
        market = marketplace.Marketplace()
        print(f'Instance: {market.get_instance()}')

    # function to change states
    def change(self, state):
        # change state
        self.state.switch(state)

