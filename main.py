from console_input import ConsoleInput
from lux_shop import LuxShop
from ts import city_combiner, put_tickets

def start(input_obj):
    """Start point of program.
    User input list of cities, dates and output mode
    """
    store = input_obj.get_store()
    lux = LuxShop()
    routes = city_combiner.route_list(cities=input_obj.get_cities(), dates=input_obj.get_dates())
    put_tickets(routes=routes, store=store, shop=lux, workers=input_obj.get_workers())

if __name__ == '__main__':
    test = ConsoleInput()
    start(test)
