import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

# Replace 'sqlite:///mydatabase.db' with your database connection string
engine = create_engine(
    'postgresql://postgres:Agtm2486@localhost:5432/my_database')


# Replace 'mydata.json' with your JSON file path
df = pd.read_json('data.json')

# print(df)


# Replace 'my_table' with the name of your database table
df.to_sql('superMart_product', engine, if_exists='replace',
          dtype={"rating": sqlalchemy.types.JSON},)

# print(df)

engine.connect().close()
