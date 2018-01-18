from input_instances.input import Input
from output_constants import OutputMode

class ConsoleInput(Input):
    def __get_list_from_console(self):
        """
        Get massive user input
        Stop if user input '.'
        return: list of strings
        """
        lines = []
        while True:
            line = raw_input()
            if line.strip() == '.':
                break
            lines.append(line)
        return lines

    def get_cities(self):
        print('Input list of cities, separated by new line. Type "." when you finish')
        return self.__get_list_from_console()

    def get_dates(self):
        print('Input list of dates (MM-DD-YYYY), separated by new line. Type "." when you finish')
        return self.__get_list_from_console()

    def get_output_mode(self):
        while True:
            print('Input "Console" or "SQLLite"')
            mode_input = raw_input().strip()
            if mode_input == 'Console':
                return OutputMode.Console
            elif mode_input == 'SQLLite':
                return OutputMode.SQLLite
