import os
import socket
import threading
import time
from requests import get
from sqlalchemy import Column, DateTime, Integer, Float, create_engine, MetaData, Table

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
headers = {'X-CMC_PRO_API_KEY': 'd61bca4c-e9d3-40b9-8d82-abf9b057ffbd', 'Accept': 'application/json'}
SOCKET_FILE = '/usr/share/bitcoin/socket'

engine = create_engine('postgresql+psycopg2://postgres:pw1234@postgres:5432/postgres')
try:
    metadata = MetaData(bind=engine)
    table = Table('bitcoin', metadata, autoload=True)
except:
    metadata = MetaData()
    table = Table('bitcoin', metadata,
                  Column('id', Integer, primary_key=True, autoincrement=True),
                  Column('price', Float),
                  Column('percent_change_1h', Float),
                  Column('percent_change_24h', Float),
                  Column('percent_change_7d', Float),
                  Column('date', DateTime))
    table.create(engine)


def worker(e, timeout):
    while not e.is_set():
        response = get(url, params={'id': 1}, headers=headers).json()
        quote = response['data']['1']['quote']['USD']
        ins = table.insert().values(price=round(quote['price'], 4),
                                    percent_change_1h=round(quote['percent_change_1h'], 4),
                                    percent_change_24h=round(quote['percent_change_24h'], 4),
                                    percent_change_7d=round(quote['percent_change_7d'], 4),
                                    date=quote['last_updated'].split('.')[0])
        engine.execute(ins)
        time.sleep(timeout)


def event():
    if os.path.exists(SOCKET_FILE):
        os.remove(SOCKET_FILE)
    server = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    server.bind(SOCKET_FILE)
    while True:
        print('create event')
        e = threading.Event()
        thread = threading.Thread(target=worker, args=(e, 300))
        thread.start()
        datagram = server.recv(4)
        if datagram == b'done':
            break
        e.set()
    server.close()
    print('server close')
    os.remove(SOCKET_FILE)
