import city_combiner
from console_input import ConsoleInput
from lux_shop import LuxShop


def put_tickets(routes, store, shop):
    for route in routes:
        route.tickets = shop.get_all_tickets(route=route)
        store.append(route=route)


def start(input_obj):
    """Start point of program.
    User input list of cities, dates and output mode
    """

    store = input_obj.get_store()
    lux = LuxShop()
    routes = city_combiner.route_list(cities=input_obj.get_cities(), dates=input_obj.get_dates())
    put_tickets(routes=routes, store=store, shop=lux)

if __name__ == '__main__':
    test = ConsoleInput()
    start(test)
