from panopticon.base_observer.pipeline import Pipeline
from panopticon.mobius_observer.mobius import Mobius
from panopticon.web_observer.dashboard import WebObserver
from panopticon.server_observer.server import ServerObserver

from panopticon.broadcaster import server

from datetime import timedelta

def main():
    mo = Mobius('xxx.xxx.xxx.xxx', 2021, {
        'Accept': 'application/json',
        'X-M2M-Origin': 'Sxxxxxxxxxxxxxx',
        'X-M2M-RI': 'xxxxxxxxxxxx',
    })

    mobiusPipeline = Pipeline({
        'ping': mo.get_observer('ping', timeout=5),
        'interval': mo.get_observer('interval', resource='/Mobius/xxx/xxx', interval=timedelta(minutes=1, seconds=30))
    })

    ubicomp = Pipeline({
        'mobius': mobiusPipeline,
        'dashboard': WebObserver('xxx.xxx.xxx.xxx', 2020),
        'server': ServerObserver('xxx.xxx.xxx.xxx')
    })


    print(ubicomp.check())

    s = server.Server()
    s.set_observer(ubicomp, 10)
    s.start()

if __name__ == '__main__':
    main()