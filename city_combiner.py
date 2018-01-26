from datetime import datetime
from itertools import product


class Ticket(object):
    """Object for storing price, time"""

    def __init__(self, price, start_time, end_time):
        """
        :param price: Price for ticket in EUR
        :param start_time: start time of route
        :param end_time:  end time of route
        """
        self.price = price
        self.start_time = start_time
        self.end_time = end_time


class Route(object):
    """Object for storing and processing route info"""

    def __init__(self, start, finish, date):
        self.start = start
        self.finish = finish
        self.date = date

        self.tickets = []


def route_list(cities, dates):
    """
    Generator provide all possible routes
    :param cities: list of cities
    :param dates: list of dates
    :return: yields item: {startCity, finishCity, date}
    """

    # Parse and sort dates
    dates = map(lambda x: datetime.strptime(x, '%m-%d-%Y'), dates)

    # Delete duplicates
    cities = list(set(cities))
    for item in filter(lambda x: x[0] != x[1], product(cities, repeat=2)):
        for date in dates:
            yield Route(start=item[0], finish=item[1], date=date)
