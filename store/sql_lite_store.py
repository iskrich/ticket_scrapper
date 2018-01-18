from store.route_store import RouteStore
import sqlite3


class SQLLiteStore(RouteStore):
    """Sql storage with tickets"""

    def __init__(self):
        self.conn = sqlite3.connect('/Users/iskrich/tickets.db')
        self.cursor = self.conn.cursor()

    def put_route(self, route):
        for ticket in route.tickets:
            self.cursor.execute("INSERT INTO tickets"
                                "(start_city, finish_city, date,"
                                "start_time, finish_time, price)"
                                " VALUES ('%s','%s','%s', '%s', '%s', '%s')" % (route.start, route.finish,
                                                                                route.date, ticket.start_time,
                                                                                ticket.end_time, ticket.price))
            self.conn.commit()
    def get_all_routes(self):
        self.cursor.execute("SELECT * from tickets")


store = SQLLiteStore()
