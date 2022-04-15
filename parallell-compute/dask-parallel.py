import dask.dataframe as dd
import pandas as pd

# Dask is a library to provide parallelism to python pool
athlete_events_dask = dd.from_pandas(pd.read_csv("../data/athlete_events.csv"), npartitions=4)

result_df = athlete_events_dask.groupby("Year").Age.mean().compute()

print(result_df.head())
