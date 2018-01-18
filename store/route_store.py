class RouteStore(object):
    def put_route(self, route):
        """Put route info"""
        raise NotImplementedError

    def get_all_routes(self):
        """Get stored routes"""
        raise NotImplementedError


class ConsoleStore(RouteStore):
    routes = []

    def put_route(self, route):
        """Put route on console window
        and store in temp list
        """
        self.routes.append(route)
        self.print_route(route)

    def get_all_routes(self):
        """Get all stored routes"""
        for route in self.routes:
            self.print_route(route)

    @staticmethod
    def print_route(route):
        date = route.date
        start = route.start
        finish = route.finish

        for ticket in route.tickets:
            print("Route from %s to %s at %s with price %s"
                  "\n Start at %s and finish %s" % (start, finish, date,
                                                    ticket.price, ticket.start_time, ticket.end_time))