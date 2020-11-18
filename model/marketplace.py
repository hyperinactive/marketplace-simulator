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
            self.resident_orders = list()
        except InstanceError:
            pass
