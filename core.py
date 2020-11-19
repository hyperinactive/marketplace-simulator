from model.app_states import states
from model.marketplace import Marketplace
from sys import exit
from controller.core_logic import idle


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
