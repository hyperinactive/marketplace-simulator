# class state handler
class AppState(object):
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
class On(AppState):
    name = 'on'
    allowed = ['await', 'off']


class Await(AppState):
    name = 'await'
    allowed = ['handle', 'on', 'off']


class Handle(AppState):
    name = 'handle'
    allowed = ['await']


class Off(AppState):
    name = 'off'
    allowed = ['on']
