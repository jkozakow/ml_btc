import requests, time
from db import *


def get_rate():
    response = requests.get(API_URL)
    json = response.json()
    return json['bpi']['USD']['rate_float'], json['time']['updatedISO']


if __name__ == "__main__":
    engine, meta = connect(DB_USER, DB_PASSWORD, DB_NAME)
    if not engine.dialect.has_table(engine, 'rates'):
        create_models(meta)
    rates = meta.tables['rates']
    conn = engine.connect()

    while True:
        rate, datetime = get_rate()
        s = rates.insert()
        conn.execute(s, rate=rate, datetime=datetime)
        time.sleep(60)
