class RouteStore(object):
    """Basic class for creating route store objects"""
    def append(self, route):
        """Put route info"""
        raise NotImplementedError

    def get_all_routes(self):
        """Get stored routes"""
        raise NotImplementedError