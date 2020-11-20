from matplotlib import pyplot as plt
import numpy as np


def make_plot(marketplace):
    plt.style.use('seaborn')

    gap = marketplace.lowest_ask().limit_price - marketplace.highest_bid().limit_price

    # TODO: have bins represent the data from the marketplace better
    bins = [x for x in range(0, 350, 5)]
    # bins.insert(len(bins)//2, round(bins[len(bins)//2] + gap))

    bids = order_to_int(marketplace.bids)
    asks = order_to_int(marketplace.asks)

    bids_t = order_to_timestamp(marketplace.bids)

    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)

    ax1.hist(bids, bins=bins, edgecolor='orange', label='BIDS', log=True)
    ax1.hist(asks, bins=bins, edgecolor='yellow', label='ASKS', log=True)

    ax2.plot(bids, bids_t, color='#444444', linestyle='--', label='All Devs')

    ax1.legend()
    plt.title('Marketplace info')

    ax1.set_xlabel('Order prices')
    ax1.set_ylabel('Number of orders')

    ax2.legend()
    ax2.set_xlabel('Ages')
    ax2.set_ylabel('Median Salary (USD)')

    plt.tight_layout()

    plt.show()


def order_to_int(marketplace_orders):
    order_list = []
    for order in marketplace_orders:
        order_list.append(order.limit_price)
    return order_list


def order_to_timestamp(marketplace_orders):
    timestamp_list = []
    for order in marketplace_orders:
        timestamp_list.append(order.timestamp)
    return timestamp_list
