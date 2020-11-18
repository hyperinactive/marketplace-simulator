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
            self.__resident_orders = []
        except InstanceError:
            pass

    # getter for private variables
    # serves no real purpose for now
    # testing stuff
    def get_order_count(self):
        return len(self.__resident_orders)
