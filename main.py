from app import App
from model.app_states.states import Off, On, Await, Handle
from model import marketplace

app = App()
app.change(On)
app.change(Await)
app.change(Handle)
app.change(Await)
app.change(Off)

# init the marketplace instance
m = marketplace.Marketplace()
print(m.get_instance().data)
print('end')
