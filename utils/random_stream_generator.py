import random


def generate():
    order_type = ['lpo', 'mpo']
    order_action = ['bid', 'ask']

    o_type = random.choice(order_type)
    o_action = random.choice(order_action)
    o_quantity = random.randint(1, 7)

    if o_type == 'lpo':
        o_price = random.randint(50, 400)
        return f'{o_type} {o_action} {o_price} {o_quantity}'
    else:
        return f'{o_type} {o_action} {o_quantity}'
