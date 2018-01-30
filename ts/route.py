class Route(object):
    """Object for storing and processing route info"""

    def __init__(self, start, finish, date):
        self.start = start
        self.finish = finish
        self.date = date

        self.tickets = []