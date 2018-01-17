from sqlalchemy import Table, Column, Float, DateTime, create_engine, MetaData

DB_USER = 'btc_user'
DB_PASSWORD = 'password1'
DB_NAME = 'btc'
API_URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'


def connect(user, password, db, host='localhost', port=5432):
    '''Returns a connection and a metadata object'''
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)

    # The return value of create_engine() is our connection object
    con = create_engine(url, client_encoding='utf8')

    # We then bind the connection to MetaData()
    meta = MetaData(bind=con, reflect=True)

    return con, meta


def create_models(db_meta):
    rates = Table(
        'rates', db_meta,
        Column('rate', Float),
        Column('datetime', DateTime)
    )

    db_meta.create_all(con)
    return rates
