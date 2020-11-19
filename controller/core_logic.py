from model.app_states.states import Idle, Await
from model import order
from sys import exit


# class specific functions outside of it?
# pretty sure this isn't even remotely close to being a decent piece of code
# did it anyway as to not to clog the core.py file
def idle(core):
    while isinstance(core.state, Idle):
        response = input('Engine idling, type \'await\' to start or \'close\' to exit\n')

        # change states if the user wants to
        if response == 'await':
            core.change(Await)
            await_for_orders(core)
        # terminate the app
        if response == 'close':
            exit()


def await_for_orders(core):
    while isinstance(core.state, Await):
        print('put the core to idle by typing \'idle\'\n')
        response = input('Or make an order: lpo action price OR mpo action\n')

        if response == 'idle':
            core.change(Idle)
        else:
            # TODO: handle input errors
            # TODO: handle proper order creation handling and handle marketplace changes
            decompose = response.split(' ')
            if decompose[0] == 'lpo':
                print('LPO')
                o = order.LimitPriceOrder(decompose[1], decompose[2])
                print(o)
            elif decompose[0] == 'mpo':
                print('MPO')
                o = order.MarketPriceOrder(decompose[1])
                print(o)

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
