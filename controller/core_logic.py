from model.app_states.states import Idle, Await, Handle
from datetime import datetime
from model import order
from sys import exit
from view.plot import make_plot
import csv


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
        # terminate the app and save the changes
        if response == 'close':
            save(core)
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
            make_plot(core.market.get_instance())
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
        o = order.LimitPriceOrder(action=decompose[1],
                                  limit_price=int(decompose[2]),
                                  timestamp=str(datetime.now()),
                                  quantity=1)
        print(o)

        if decompose[1] == 'bid':
            # core.market.get_instance().bids.append(o)
            # for x in core.market.get_instance().bids:
            #     print(f'{x} and type: {type(x)}')

            handle_underlying_orders(core, o)
        elif decompose[1] == 'ask':
            # core.market.asks.append(o)
            # for x in core.market.get_instance().asks:
            #     print(f'{x} and type: {type(x)}')
            handle_underlying_orders(core, o)

    elif decompose[0] == 'mpo':
        print('MPO')
        o = order.MarketPriceOrder(action=decompose[1],
                                   timestamp=datetime.now(),
                                   quantity=1)
        print(o)

    core.change(Await)
    await_for_orders(core)


def save(core):
    # don't do this
    path = 'C:/Users/aleks/PycharmProjects/marketplace/utils/marketplace_orders.csv'
    fieldnames = ['order_type', 'order_action', 'limit_price', 'timestamp', 'quantity']

    # get the newly added order to the csv
    # importing os module? never heard of it
    with open(path, 'w') as csv_file:
        # lpo,ask,113,2020-08-24 13:49:18.692822,1
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()

    write_items(core.market.get_instance().bids,
                'C:/Users/aleks/PycharmProjects/marketplace/utils/marketplace_orders.csv',
                fieldnames)
    write_items(core.market.get_instance().asks,
                'C:/Users/aleks/PycharmProjects/marketplace/utils/marketplace_orders.csv',
                fieldnames)


def write_items(item_list, path, fieldnames):
    for item in item_list:
        with open(path, 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            info = {
                'order_type': 'lpo',
                'order_action': item.action,
                'limit_price': item.limit_price,
                'timestamp': item.timestamp,
                'quantity': item.quantity
            }
            csv_writer.writerow(info)


def handle_underlying_orders(core, u_order):
    core.market.get_instance().asks = sorted(core.market.get_instance().asks)
    core.market.get_instance().bids = sorted(core.market.get_instance().bids)

    # could these two blocks have been written just once? -probably
    # should I have done so? -yeah
    if u_order.action == 'bid':
        for item in core.market.get_instance().asks:
            if item.limit_price <= u_order.limit_price:
                print(f'Bought {item}')
                core.market.get_instance().asks.pop(core.market.get_instance().asks.index(item))
                return
        print(f'Added {u_order}')
        core.market.get_instance().bids.append(u_order)

    if u_order.action == 'ask':
        for item in core.market.get_instance().bids:
            if item.limit_price <= u_order.limit_price:
                print(f'Bought {item}')
                core.market.get_instance().bids.pop(core.market.get_instance().bids.index(item))
                return
        print(f'Added {u_order}')
        core.market.get_instance().asks.append(u_order)
