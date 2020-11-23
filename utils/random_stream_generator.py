import random


def generate():
    order_type = ['lpo', 'mpo']
    order_action = ['bid', 'ask']

    while True:
        o_type = random.choice(order_type)
        o_action = random.choice(order_action)

        if o_type == 'lpo':
            l_price = random.randint(50, 400)
            return f'{o_type} {o_action} {l_price}'
        else:
            return f'{o_type} {o_action}'
