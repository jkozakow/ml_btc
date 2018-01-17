import tensorflow
import pandas as pd
from db import connect, DB_USER, DB_PASSWORD, DB_NAME
from sqlalchemy.sql import select


def get_data():
    engine, meta = connect(DB_USER, DB_PASSWORD, DB_NAME)
    rates = meta.tables['rates']
    conn = engine.connect()
    s = select([rates])
    result = conn.execute(s)
    return result.fetchall()


def make_dataframe(data):
    print(data)
    df = pd.DataFrame(data)
    return df.pivot(index=0, columns=1, values=2)


if __name__ == "__main__":
    data = get_data()
    print(make_dataframe(data=data))
