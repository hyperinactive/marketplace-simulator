# class state super class
class CoreState(object):
    name = "state"
    allowed = []

    def switch(self, state):
        """ Switch to new state """
        if state.name in self.allowed:
            print('Current:', self, ' => switched to new state', state.name)
            self.__class__ = state
        else:
            print('Current:', self, ' => switching to', state.name, 'not possible.')

    def __str__(self):
        return self.name


# states
class Idle(CoreState):
    name = 'idle'
    allowed = ['await']


class Await(CoreState):
    name = 'await'
    allowed = ['handle', 'idle']


class Handle(CoreState):
    name = 'handle'
    allowed = ['await']

