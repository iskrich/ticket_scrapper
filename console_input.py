import argparse

from route_store import ConsoleStore
from sql_lite_store import SQLLiteStore
from ts import Input


class ConsoleInput(Input):
    def __init__(self):
        parser = argparse.ArgumentParser(description='Ticket parser')
        parser.add_argument('-c', '--cities', nargs='+', help='<Required> Input cities', required=True)
        parser.add_argument('-d', '--dates', nargs='+', help='<Required> Input dates', required=True)
        parser.add_argument('-m', '--mode', type=str, help='<Required> Input mode type', required=True)
        parser.add_argument('-w', '--workers', type=int, default=1, help='Input count of workers')
        self.args = parser.parse_args()

    def get_cities(self):
        return self.args.cities

    def get_dates(self):
        return self.args.dates

    def get_store(self):
        mode_input = self.args.mode
        if mode_input == 'Console':
            return ConsoleStore()
        elif mode_input == 'Db':
            return SQLLiteStore()

    def get_workers(self):
        return self.args.workers