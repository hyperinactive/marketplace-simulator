import csv
import random
from datetime import datetime, timedelta


def random_timestamp(start):
    current = start
    curr = current + timedelta(minutes=random.randrange(60))
    return curr


startDate = datetime.now() - timedelta(hours=1)

# a util file to generate orders
order_action = ['bid', 'ask']

fieldnames = ['order_type', 'order_action', 'limit_price', 'timestamp', 'quantity']

# write headers
with open('marketplace_orders.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

# append rows
for i in range(0, 100):
    with open('marketplace_orders.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        oa = random.choice(order_action)
        if oa == 'bid':
            limit_price = random.randint(0, 100)
        else:
            limit_price = random.randint(110, 300)

        info = {
            'order_type': 'lpo',
            'order_action': oa,
            'limit_price': limit_price,
            'timestamp': random_timestamp(startDate),
            'quantity': 1
        }

        csv_writer.writerow(info)
