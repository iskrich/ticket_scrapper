import sqlite3

from route_store import RouteStore


class SQLLiteStore(RouteStore):
    """Sql storage with tickets"""

    def __init__(self):
        self.connection = sqlite3.connect('db/tickets.db')
        self.cursor = self.connection.cursor()

    def append(self, route):
        for ticket in route.tickets:
            self.cursor.execute("INSERT INTO tickets"
                                "(start_city, finish_city, date,"
                                "start_time, finish_time, price)"
                                " VALUES ?", (route.start, route.finish, route.date, ticket.start_time,
                                              ticket.end_time, ticket.price))
            self.connection.commit()

    def get_all_routes(self):
        self.cursor.execute("SELECT * from tickets")
