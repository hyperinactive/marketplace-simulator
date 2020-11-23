from matplotlib import pyplot as plt
from model.marketplace import Marketplace
from itertools import count
from matplotlib.animation import FuncAnimation
from utils.random_stream_generator import generate


def make_plot():
    plt.style.use('seaborn')
    m = Marketplace.get_instance()
    # TODO: have bins represent the data from the marketplace better
    bins = [x for x in range(0, 400, 5)]

    bids = sorted(order_to_int(Marketplace.get_instance().bids))
    asks = sorted(order_to_int(Marketplace.get_instance().asks))

    bids_t = order_to_timestamp(sorted(m.bids, key=lambda x: x.timestamp))
    asks_t = order_to_timestamp(sorted(m.asks, key=lambda x: x.timestamp))

    fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1)

    ax1.hist(bids, bins=bins, edgecolor='orange', label='BIDS', log=True)
    ax1.hist(asks, bins=bins, edgecolor='yellow', label='ASKS', log=True)

    ax2.plot(bids_t, order_to_int(m.bids), color='#444444', linestyle='--', label='BIDS')
    ax3.plot(asks_t, order_to_int(m.asks), color='#888444', linestyle='--', label='ASKS')

    ax1.legend()
    plt.title('Marketplace info')

    ax1.set_xlabel('Order prices')
    ax1.set_ylabel('Number of orders')

    ax2.legend()
    ax2.set_xlabel('BIDS')
    ax2.set_ylabel('Timestamp')

    ax3.legend()
    ax3.set_xlabel('ASKS')
    ax3.set_ylabel('Timestamp')

    plt.tight_layout()

    plt.show()


def simulate(handle_func):
    m = Marketplace.get_instance()

    plt.style.use('fivethirtyeight')
    index = count()

    def animate(i):
        handle_func(generate())

        bins = [x for x in range(0, 400, 5)]

        bids = sorted(order_to_int(Marketplace.get_instance().bids))
        asks = sorted(order_to_int(Marketplace.get_instance().asks))

        plt.cla()

        plt.hist(bids, bins=bins, edgecolor='orange', label='BIDS')
        plt.hist(asks, bins=bins, edgecolor='yellow', label='ASKS')

        plt.legend()
        plt.title('Marketplace info')

        plt.xlabel('Order prices')
        plt.ylabel('Number of orders')

    ani = FuncAnimation(plt.gcf(), animate, interval=2000)

    plt.tight_layout()
    plt.show()


def order_to_int(marketplace_orders):
    order_list = list()
    for order in marketplace_orders:
        order_list.append(order.limit_price)
    return order_list


def order_to_timestamp(marketplace_orders):
    timestamp_list = []
    for order in marketplace_orders:
        timestamp_list.append(order.timestamp)
    return timestamp_list
