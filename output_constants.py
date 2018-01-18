from store.route_store import ConsoleStore
from store.sql_lite_store import SQLLiteStore

class OutputMode:
    SQLLite = 0
    Console = 1


STORES = {OutputMode.SQLLite: SQLLiteStore(),
          OutputMode.Console: ConsoleStore()}
