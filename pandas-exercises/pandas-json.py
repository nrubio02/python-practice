import pandas as pd

dhs = pd.read_json("../data/dhs_daily_report.json")

# read_json() arguments
# orient
#   Indicates how the json is structured. Check pandas documentation to see possible values

# How to make a call to an API
import requests

api_url = "http://api.yelp.com/v3/businesses/search"
params = {
    "term": "bookstore",
    "location": "San Francisco"
}
headers = {
    "Authorization": "Bearer {}".format("")  # api_key
}

response = requests.get(api_url, params=params, headers=headers)
data = response.json()  # This returns a dictionary, so we cannot use read_json, we have to use pd.DataFrame()
bookstores = pd.DataFrame(data["businesses"])

# How to deal with nested JSON
from pandas.io.json import json_normalize

bookstores_normalized = json_normalize(bookstores, sep="_")
# sep
#   Indicates separator for the new column name of normalized column. Name format is <property>.<nested_property>
#   with dot (.) as default separator

# TODO Research the following arguments: record_path, meta, meta_prefix

# TODO Add DataFrame.merge()