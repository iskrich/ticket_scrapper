import requests
from bs4 import BeautifulSoup

from city_combiner import Ticket
from shop import TicketShop


class LuxShop(TicketShop):
    def get_all_tickets(self, route):
        """Make request to ticket.luxexpress.eu"""
        request = "https://ticket.luxexpress.eu/en/trips-timetable/%s/%s?" \
                  "Date=%s&ReturnDate=&MultiHopSearchSortOrder=StartTimeAndDuration" \
                  "&CampaignCode=&Currency=CURRENCY.EUR" % (route.start, route.finish, route.date.strftime('%m-%d-%Y'))
        req = requests.get(request)
        return self._parse_response(req.content)


    def _parse_response(self, resp):
        """
        :param resp: html response from lux
        :return: list of tickets
        """
        tickets = []
        soup = BeautifulSoup(resp, 'html.parser')
        timetable = soup.find(True, {'class':['trips', 'trip-table', 'go-there']})
        for ticket in timetable.select('div.row.trip-row.with-mar-0'):
            start_time = ticket.select_one('div.col-xs-6.disp-cell.text-left').select('span')[0].contents[0]
            end_time = ticket.select_one('div.col-xs-6.disp-cell.text-left').select('span')[1].contents[0]
            price = ticket.select_one('span.amount').contents[0]
            tickets.append(Ticket(price=price, start_time=start_time, end_time=end_time))
        return tickets

