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
