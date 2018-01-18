from combiner import city_combiner
from input_instances.console_input import ConsoleInput
from input_instances.test_input import TestInput
from ticket_shop.lux_shop import LuxShop
from output_constants import STORES

def start(input_obj):
    """Start point of program.
    User input list of cities, dates and output mode
    """
    input_data = {}

    input_data['cities'] = input_obj.get_cities()
    input_data['dates'] = input_obj.get_dates()
    mode = input_obj.get_output_mode()

    store = STORES[mode]
    lux = LuxShop()
    routes = city_combiner.route_list(input_data['cities'], input_data['dates'])

    for route in routes:
        route.tickets = lux.get_all_tickets(route)
        store.put_route(route)

test = TestInput()
start(test)
