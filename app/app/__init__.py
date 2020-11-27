import datetime
import os
import socket
from flask import Flask
from flask_restful import Api, Resource
from json import dumps
from sqlalchemy import Column, create_engine, DateTime, Integer, Float, MetaData, Table

SOCKET_FILE = '/usr/share/bitcoin/socket'
client = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
if os.path.exists(SOCKET_FILE):
    print(os.listdir('/usr/share/bitcoin/'))
    client.connect(SOCKET_FILE)

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

app = Flask(__name__)
api = Api(app)


class Quote(Resource):
    @staticmethod
    def get(endpoint=False):
        if endpoint == 'latest':
            client.send(b'give')
            record = dict(next(engine.execute(table.select().order_by(table.c.id.desc()))))
            dt = record['date']
            if isinstance(dt, (datetime.date, datetime.datetime)):
                record['date'] = dt.isoformat()
            return dumps(record), 200
        else:
            output = []
            for record in engine.execute(table.select()):
                record = dict(record)
                dt = record['date']
                if isinstance(dt, (datetime.date, datetime.datetime)):
                    record['date'] = dt.isoformat()
                output.append(dumps(record))
            return '\n'.join(output), 200


api.add_resource(Quote, "/quotes", "/quotes/<string:endpoint>")
