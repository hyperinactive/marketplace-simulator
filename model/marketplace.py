class InstanceError:
    print('Only one instance of Marketplace can exist')


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
            self.data = 10
        except InstanceError:
            pass
