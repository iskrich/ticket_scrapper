import logging
from ts import RouteStore

class ConsoleStore(RouteStore):
    def __init__(self):
        logging.getLogger().setLevel(logging.INFO)
        self.routes = []

    def append(self, route):
        """Put route on console window
        and store in temp list
        """
        self.routes.append(route)
        self.print_route(route=route)

    def get_all_routes(self):
        """Get all stored routes"""
        for route in self.routes:
            self.print_route(route)

    @staticmethod
    def print_route(route):
        for ticket in route.tickets:
            logging.info("Route from %s to %s at %s with price %s"
                         "\n Start at %s and finish %s" % (route.start, route.finish, route.date,
                                                           ticket.price, ticket.start_time, ticket.end_time))
