from multiprocessing import Pool, Lock
from functools import partial

lock = Lock()


def process_route(route, store, shop):
    route.tickets = shop.get_all_tickets(route=route)
    lock.acquire()
    store.append(route=route)
    lock.release()


def put_tickets(routes, store, shop, workers):
    """Simple functionality for finding and storing tickets"""
    pool = Pool(processes=workers)
    r = pool.map_async(func=partial(process_route, store=store, shop=shop), iterable=routes)
    r.wait()
