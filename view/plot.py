from matplotlib import pyplot as plt


def make_plot(marketplace):
    plt.style.use('seaborn')
    # TODO: have bins represent the data from the marketplace better
    bins = [50, 100, 150, 200, 250, 300]

    bids = order_to_int(marketplace.bids)
    asks = order_to_int(marketplace.asks)
    orders = bids + asks

    plt.hist(orders, bins=bins, edgecolor='black', label='Limit price orders')

    plt.legend()
    plt.title('Marketplace')
    plt.xlabel('Order prices')
    plt.ylabel('Number of orders')

    plt.tight_layout()

    plt.show()


def order_to_int(marketplace_orders):
    order_list = []
    for bid in marketplace_orders:
        order_list.append(bid.limit_price)
    return order_list
