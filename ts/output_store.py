from multiprocessing import Pool, Lock
from functools import partial

def process_route(route, store, shop):
    route.tickets = shop.get_all_tickets(route=route)
    store.append(route=route)

def put_tickets(routes, store, shop, workers):
    """Simple functionality for finding and storing tickets"""
    pool = Pool(processes=workers)
    r = pool.map_async(func=partial(process_route, store=store, shop=shop), iterable=routes)
    r.wait()
