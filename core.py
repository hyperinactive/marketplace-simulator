from model.app_states import states
from model import marketplace
from sys import exit


# core tracks states and controls the Trader and Order Matcher
class Core(object):

    def __init__(self):
        # set the default state and start the default function
        self.state = states.Idle()
        self.idle()

        # init the marketplace
        print('Initializing the marketplace instance')
        market = marketplace.Marketplace()
        print(f'Instance: {market.get_instance()}')

    # function to change states
    def change(self, state):
        # change state
        self.state.switch(state)

    def idle(self):
        while isinstance(self.state, states.Idle):
            response = input('Engine idling, type await to start or close to exit\n')

            # change states if the user wants to
            if response == 'await':
                self.change(states.Await)
                self.await_for_orders()
            # terminate the app
            if response == 'close':
                exit()

    # function to handle incoming orders
    def await_for_orders(self):
        while isinstance(self.state, states.Await):
            response = input('Make an instruction or put the core to idle by typing \'idle\'\n')

            if response == 'idle':
                self.change(states.Idle)

    def invoke_order_matching_engine(self):
        # TODO: create an Order Matching Engine
        #   Engine should take in an instruction and determine it's type
        #   based on the type find the appropriate match
        #   matching priority: price/time
        pass

    def invoke_trader(self):
        # TODO: create a Trader
        #   Trader should take in matches and handle the data accordingly
        pass
