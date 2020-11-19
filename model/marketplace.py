import csv


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

    def loader(self):
        # TODO: load items from the marketplace_orders.csv
        pass
