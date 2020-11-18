from core import Core
from model.app_states.states import Idle, Await, Handle

core = Core()
core.change(Await)
core.do_smth()
# core.change(Await)
# core.change(Handle)
# core.change(Await)
# core.change(Off)

# TODO: handle core states and enable instruction creation
#   - I guess we can turn it off and on, that'd be cool
#   but waiting and instruction handling must be automatic
#   - make a Marketplace Viewer, some GUI to show the current state of the market
#   optional: can be started as a standalone script from other sources?
