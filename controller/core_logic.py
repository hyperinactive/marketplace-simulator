from model.app_states.states import Idle, Await, Handle
from model.marketplace import Marketplace
from model.order import LimitPriceOrder, MarketPriceOrder
from view.plot import make_plot
from datetime import datetime
from sys import exit
import csv


# obviously Core should've been a singleton class, rather than Marketplace...
# well, no going back now

# quick fix to the logic in order to use it's functions for random_stream_generator -> import Marketplace()

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
            make_plot()
            core.change(Await)
        else:
            core.change(Handle)
            handle_operation(response)
            core.change(Await)


def handle_operation(response):
    # TODO: handle input errors
    handle_input_orders(response)


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


def handle_input_orders(response):
    decompose = response.split(' ')
    o = None

    if decompose[0] == 'lpo':
        print('Limit Price Order')
        o = LimitPriceOrder(action=decompose[1],
                            limit_price=int(decompose[2]),
                            timestamp=str(datetime.now()),
                            quantity=1)
        print(o)

    elif decompose[0] == 'mpo':
        print('Market Price Order')
        o = MarketPriceOrder(action=decompose[1],
                             timestamp=datetime.now(),
                             quantity=1)
        print(o)
    handle_underlying_orders(o)


def handle_underlying_orders(u_order):
    if isinstance(u_order, LimitPriceOrder) or isinstance(u_order, MarketPriceOrder):
        sorted_asks = sorted(Marketplace.get_instance().asks)
        sorted_bids = sorted(Marketplace.get_instance().bids)

        # handle lpo or mpo
        handle_lpo(u_order, sorted_asks, sorted_bids) \
            if isinstance(u_order, LimitPriceOrder) \
            else handle_mpo(u_order, sorted_asks, sorted_bids)


def handle_lpo(u_order, asks, bids):
    # could these two blocks have been written just once? -probably
    # should I have done so? -yeah
    if u_order.action == 'bid':
        for item in asks:
            if item.limit_price <= u_order.limit_price:
                print(f'Bought {item}')
                asks.pop(Marketplace.get_instance().asks.index(item))
                return
        print(f'Added {u_order}')
        Marketplace.get_instance().bids.append(u_order)

    if u_order.action == 'ask':
        for item in bids:
            if item.limit_price >= u_order.limit_price:
                print(f'Bought {item}')
                bids.pop(Marketplace.get_instance().bids.index(item))
                return
        print(f'Added {u_order}')
        Marketplace.get_instance().asks.append(u_order)


def handle_mpo(u_order, asks, bids):
    if u_order.action == 'bid':
        if len(asks) == 0:
            print('No sellers on the marketplace, marketplace price non existent')
        else:
            matching_order = Marketplace.get_instance().asks.pop(0)
            print(f'Bought {matching_order}')
    if u_order.action == 'ask':
        if len(bids) == 0:
            print('No buyers on the marketplace, marketplace price non existent')
        else:
            matching_order = Marketplace.get_instance().bids.pop()
            print(f'Bought {matching_order}')
