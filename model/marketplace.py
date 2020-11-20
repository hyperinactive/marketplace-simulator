import csv
import pandas as pd
import os
from model.order import LimitPriceOrder


# custom error to catch instancing errors
class InstanceError:
    print('Only one instance of Marketplace can exist')


# singleton pattern
class Marketplace:
    __instance = None

    @staticmethod
    def get_instance():
        if Marketplace.__instance is None:
            Marketplace()
        return Marketplace.__instance

    def __init__(self):
        try:
            Marketplace.__instance = self
            # init the lists
            # TODO: maybe add a loader to get pre startup data(?)
            self.asks = list()
            self.bids = list()
        except InstanceError:
            pass

    def highest_bid(self):
        return self.bids[len(self.bids) - 1]

    def lowest_ask(self):
        return self.asks[0]
