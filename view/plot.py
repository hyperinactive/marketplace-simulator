from matplotlib import pyplot as plt
import numpy as np


def make_plot(marketplace):
    plt.style.use('seaborn')

    # gap = marketplace.lowest_ask().limit_price - marketplace.highest_bid().limit_price

    # TODO: have bins represent the data from the marketplace better
    bins = [x for x in range(0, 400, 5)]
    # bins.insert(len(bins)//2, round(bins[len(bins)//2] + gap))

    # bids_pre = sorted(marketplace.bids, key=lambda x: x.limit_price)
    # bids = order_to_int(bids_pre)
    # asks_pre = sorted(marketplace.asks, key=lambda x: x.limit_price)
    # asks = order_to_int(asks_pre)

    bids = sorted(order_to_int(marketplace.bids))
    asks = sorted(order_to_int(marketplace.asks))

    bids_t = order_to_timestamp(sorted(marketplace.bids, key=lambda x: x.timestamp))
    asks_t = order_to_timestamp(sorted(marketplace.asks, key=lambda x: x.timestamp))

    fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1)

    ax1.hist(bids, bins=bins, edgecolor='orange', label='BIDS', log=True)
    ax1.hist(asks, bins=bins, edgecolor='yellow', label='ASKS', log=True)

    ax2.plot(bids_t, order_to_int(marketplace.bids), color='#444444', linestyle='--', label='BIDS')
    ax3.plot(asks_t, order_to_int(marketplace.asks), color='#888444', linestyle='--', label='ASKS')

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
