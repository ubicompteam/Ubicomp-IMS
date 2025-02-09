import os
from datetime import timedelta

from dotenv import load_dotenv

from base_observer.pipeline import Pipeline
from broadcaster.client import Client
from mobius_observer.mobius import Mobius
from server_observer.server import ServerObserver
from web_observer.web import WebObserver

load_dotenv()

def main():
    mo = Mobius(os.getenv('MOBIUS_SERVER_ADDRESS'), int(os.getenv('MOBIUS_SERVER_PORT')), {
        'Accept': 'application/json',
        'X-M2M-Origin': 'S20170717074825768bp2l',
        'X-M2M-RI': 'sdaf343545',
    })

    mobiusPipeline = Pipeline({
        'ping': mo.get_observer('ping', timeout=5),
        'interval': mo.get_observer('interval', resource=os.getenv('MOBIUS_RESOURCE_DIRECTORY'), interval=timedelta(minutes=1, seconds=30))
    })

    ubicomp = Pipeline({
        'mobius': mobiusPipeline,
        'dashboard': WebObserver(os.getenv('DASHBOARD_SERVER_ADDRESS'), int(os.getenv('DASHBOARD_SERVER_PORT'))),
        'server': ServerObserver(os.getenv('MOBIUS_SERVER_ADDRESS')),
        'test': WebObserver('localhost', 3000)
    })


    # print(ubicomp.check())

    while True:
        print(f'Connecting to {os.getenv("FLASK_SERVER_ADDRESS")}:{os.getenv("FLASK_SERVER_PORT")}')
        c = Client(os.getenv('FLASK_SERVER_ADDRESS'), int(os.getenv('FLASK_SERVER_PORT')))
        c.set_observer(ubicomp, 10)
        c.start()

if __name__ == '__main__':
    main()