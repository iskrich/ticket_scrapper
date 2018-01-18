from input_instances.input import Input
from output_constants import OutputMode

class TestInput(Input):
    def get_cities(self):
        return ['johvi', 'stpetersburg-coach-station', 'helsinki-coach-station-kamppi']

    def get_dates(self):
        return ['01-18-2018', '02-14-2018', '01-17-2018']

    def get_output_mode(self):
        return OutputMode.SQLLite