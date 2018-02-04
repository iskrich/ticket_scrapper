from datetime import datetime
from itertools import product, permutations
from .route import Route

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
    for cities, date in product(permutations(cities, 2), dates):
        yield Route(start=cities[0], finish=cities[1], date=date)
