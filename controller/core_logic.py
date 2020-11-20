from model.app_states.states import Idle, Await, Handle
from datetime import datetime
from model import order
from sys import exit
from view import plot


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
        print('Put the core to idle by typing \'idle\'')
        response = input('Make an order: lpo_action_price OR mpo_action\n')

        if response == 'idle':
            core.change(Idle)
        elif response == 'load':
            core.change(Handle)
            core.load()
            core.change(Await)
        elif response == 'plot':
            core.change(Handle)
            plot.make_plot(core.market.get_instance())
            core.change(Await)
        else:
            core.change(Handle)
            handle_operation(core, response)


def handle_operation(core, response):
    # TODO: handle input errors
    # TODO: handle proper order creation handling and handle marketplace changes
    decompose = response.split(' ')
    if decompose[0] == 'lpo':
        print('Limit Price Order')
        o = order.LimitPriceOrder(action=decompose[1], limit_price=decompose[2], timestamp=datetime.now(), quantity=1)
        print(o)

        if decompose[1] == 'bid':
            core.market.get_instance().bids.append(o)
            # print(*core.market.get_instance().bids)

        elif decompose[1] == 'ask':
            core.market.asks.append(o)
            # print(*core.market.get_instance().asks)

    elif decompose[0] == 'mpo':
        print('MPO')
        o = order.MarketPriceOrder(action=decompose[1], timestamp=datetime.now(), quantity=1)
        print(o)

    core.change(Await)
    await_for_orders(core)


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
