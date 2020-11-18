from model.app_states import states
from model import marketplace


# core tracks states and controls the Trader and Order Matcher
class Core(object):

    def __init__(self):
        # default state
        self.state = states.Idle()

        # init the marketplace upon creation
        print('Initializing the marketplace instance')
        m = marketplace.Marketplace()
        print(f'Instance: {m.get_instance()}')
        print(f'Current marketplace item count {m.get_instance().get_order_count()}')

    def change(self, state):
        # change state
        self.state.switch(state)

        # TODO: handle the Await state
        #   create an Instruction class, (optional) perhaps <- a super class and Resident/Incoming sub classes?

        # TODO: maybe have this in a separate function, make it cleaner
        #   handle idle in the same way? - core currently shuts down after the loop ends
        if self.state.name == states.Await.name:
            print('Now, I wait on instructions')
            print('To stop me, switch to idle')
            while self.state.name == states.Await.name:
                response = input('Make an instruction or put the core to idle by typing \'idle\'\n')

                if response == 'idle':
                    self.change(states.Idle)

    def do_smth(self):
        # probably wrong to compare names, but I don't know better atm
        if self.state.name == states.Idle.name:
            print('I am doing something while being ON')

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
