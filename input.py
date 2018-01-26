class Input(object):
    def get_cities(self):
        """
        return: list of cities
        """
        raise NotImplementedError

    def get_dates(self):
        """
        return: list of dates
        """
        raise NotImplementedError

    def get_store(self):
        """
        return: output mode
        """
        raise NotImplementedError