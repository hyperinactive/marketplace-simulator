from model.app_states.states import Idle, Await, Handle
from model.marketplace import Marketplace
from model.order import LimitPriceOrder, MarketPriceOrder
from view.plot import make_plot, simulate
from datetime import datetime
from sys import exit
from utils.random_stream_generator import generate
from utils.resident_order_generator import generate_staring_data
from time import sleep
import pandas as pd
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
            save()
            exit()


def await_for_orders(core):
    while isinstance(core.state, Await):
        # print('Put the core to idle by typing \'idle\'')
        # print('Load starting data by typing \'load\'')
        # print('Plot the data by typing \'plot\'')
        print('Engine awaiting - option list: \'idle\', \'init\' \'load\', \'plot\', \'sim\', \'sim v2\'')
        response = input('Make an order: lpo_action_price_quantity OR mpo_action_quantity\n')

        if response == 'idle':
            core.change(Idle)
        else:
            core.change(Handle)
            handle(core, response)


def handle(core, response):
    # never heard of switch?
    while isinstance(core.state, Handle):
        if response == 'load':
            load()
        elif response == 'init':
            generate_staring_data()
        elif response == 'plot':
            make_plot()
        elif response == 'sim':
            x = int(input('Number of simulations?\n'))
            for i in range(0, x):
                handle_input_orders(generate())
                sleep(2)
        elif response == 'sim v2':
            simulate(handle_func=handle_operation)
        else:
            handle_operation(response)

        core.change(Await)


def handle_operation(response):
    # TODO: handle input errors
    handle_input_orders(response)


def load():
    # order_type,order_action,limit_price,timestamp,quantity

    path = 'C:/Users/aleks/PycharmProjects/marketplace/utils/marketplace_orders.csv'

    data = pd.read_csv(path)
    order_action = data['order_action']
    limit_price = data['limit_price']
    timestamp = data['timestamp']
    quantity = data['quantity']

    for i in range(0, len(data)):
        limit_price_order = LimitPriceOrder(order_action[i],
                                            timestamp[i],
                                            quantity[i],
                                            limit_price[i])
        if order_action[i] == 'ask':
            Marketplace.get_instance().asks.append(limit_price_order)
        else:
            Marketplace.get_instance().bids.append(limit_price_order)

    # sort loaded data
    # for easier plotting down the line

    # pre-sort the ask and bids
    # self.market.get_instance().asks = sorted(self.market.get_instance().asks)
    # self.market.get_instance().bids = sorted(self.market.get_instance().bids)

    print('BIDS')
    for item in Marketplace.get_instance().bids:
        print(item)

    print('ASKS')
    for item in Marketplace.get_instance().asks:
        print(item)
    print(f'Lowest ask: {Marketplace.get_instance().lowest_ask()}')
    print(f'Highest bid: {Marketplace.get_instance().highest_bid()}')


def save():
    # don't do this
    path = 'C:/Users/aleks/PycharmProjects/marketplace/utils/marketplace_orders.csv'
    fieldnames = ['order_type', 'order_action', 'limit_price', 'timestamp', 'quantity']

    # get the newly added order to the csv
    # importing os module? never heard of it
    with open(path, 'w') as csv_file:
        # lpo,ask,113,2020-08-24 13:49:18.692822,1
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()

    write_items(Marketplace.get_instance().bids,
                'C:/Users/aleks/PycharmProjects/marketplace/utils/marketplace_orders.csv',
                fieldnames)
    write_items(Marketplace.get_instance().asks,
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
                            quantity=int(decompose[3]))
        print(o)

    elif decompose[0] == 'mpo':
        print('Market Price Order')
        o = MarketPriceOrder(action=decompose[1],
                             timestamp=datetime.now(),
                             quantity=int(decompose[2]))
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
            if u_order.quantity == 0:
                return
            if item.limit_price <= u_order.limit_price:
                # item.quantity < order quantity
                if item.quantity < u_order.quantity:
                    u_order.quantity -= item.quantity
                    print(f'Bought {item.quantity} of {item}')
                    Marketplace.get_instance().asks.remove(item)
                # item.quantity >= order quantity
                else:
                    item.quantity -= u_order.quantity
                    print(f'Bought {u_order.quantity} of {item}')
                    if item.quantity == 0:
                        Marketplace.get_instance().asks.remove(item)
                    return
        print(f'Added {u_order}')
        Marketplace.get_instance().bids.append(u_order)

    if u_order.action == 'ask':
        for item in bids:
            if u_order.quantity == 0:
                return
            if item.limit_price >= u_order.limit_price:
                if item.quantity < u_order.quantity:
                    u_order.quantity -= item.quantity
                    print(f'Sold {item.quantity} of {item}')
                    Marketplace.get_instance().bids.remove(item)
                else:
                    item.quantity -= u_order.quantity
                    print(f'Sold {u_order.quantity} of {item}')
                    if item.quantity == 0:
                        Marketplace.get_instance().bids.remove(item)
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
