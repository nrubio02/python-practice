from multiprocessing import Pool
import pandas as pd


def take_mean_age(year_and_group):
    year, group = year_and_group
    return pd.DataFrame({"Age": group["Age"].mean()}, index=[year])


athlete_events = pd.read_csv("../data/athlete_events.csv")
# Pool works as a Process pool, we define how many processes are available
with Pool(4) as p:
    # map() takes a function which will be applied to the items in the second argument
    # Returns a list of the results
    results = p.map(take_mean_age, athlete_events.groupby("Year"))

result_df = pd.concat(results)

print(result_df.head())
