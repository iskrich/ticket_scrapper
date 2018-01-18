from shop import TicketShop
import urllib2
from bs4 import BeautifulSoup
from combiner.city_combiner import Ticket


class LuxShop(TicketShop):
    def get_all_tickets(self, route):
        """Make request to ticket.luxexpress.eu"""
        request = "https://ticket.luxexpress.eu/en/trips-timetable/%s/%s?" \
                  "Date=%s&ReturnDate=&MultiHopSearchSortOrder=StartTimeAndDuration" \
                  "&CampaignCode=&Currency=CURRENCY.EUR" % (route.start, route.finish, route.date.strftime('%m-%d-%Y'))
        req = urllib2.urlopen(request)
        return self.__parse_response(req.read())


    def __parse_response(self, resp):
        """
        :param resp: html response from lux
        :return: list of tickets
        """
        tickets = []
        soup = BeautifulSoup(resp, 'html.parser')
        timetable = soup.findAll(True, {'class':['trips', 'trip-table', 'go-there']})[0]
        for ticket in timetable.select('div.row.trip-row.with-mar-0'):
            start_time = ticket.select('div.col-xs-6.disp-cell.text-left')[0].select('span')[0].contents[0]
            end_time = ticket.select('div.col-xs-6.disp-cell.text-left')[0].select('span')[1].contents[0]
            price = ticket.select('span.amount')[0].contents[0]
            tickets.append(Ticket(price, start_time, end_time))

        return tickets

