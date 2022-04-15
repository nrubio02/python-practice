import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import inspect

engine = create_engine("sqlite:///../data/data.db")

# We can inspect the database to, for example, get the list of tables
ins = inspect(engine)
print(ins.get_table_names())

# read_sql() takes either the table name or a SQL query as its first argument
weather = pd.read_sql("weather", engine)
print(weather.head())
