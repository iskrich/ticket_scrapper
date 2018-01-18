class TicketShop(object):
    def get_all_tickets(self, route):
        """Get all possible tickets for route
        route: target Route object
        """
        raise NotImplementedError

    def buy_ticket(self, ticket):
        """Post buy request
        ticket: target Ticket object
        """
        raise