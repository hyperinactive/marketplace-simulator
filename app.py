from model.app_states import states


class App(object):

    def __init__(self):
        # default state
        self.state = states.Off()

    def change(self, state):
        # change state
        self.state.switch(state)
