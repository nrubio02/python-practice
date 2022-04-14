import pandas as pd

# read_csv returns a pandas DataFrame
# Accepts another parameter 'sep' to indicate separator: sep="\t"
tax_data = pd.read_csv("../data/vt_tax_data_2016.csv")

# We can also pass different arguments to the read_csv() function:

# usecols=cols_names
# 	Pass a list of values to specify the columns to read from the DataFrame, like: cols_names = ['STATE', 'zipcode']

# nrows=500,
# 	Specify how many rows to read from the file

# skiprows=500,
# 	Specify how many rows to skip from the file

# header=None,
#	Indicate that the resulting DataFrame doesn't have a header row

# names=list(vt_data_first500)
#	Pass a list to set new column names for the DataFrame

# dtype={ "zipcode": str }
#	Specify the data type for the colums by passing a single value, list or dictionary. If only setting the data type
#	for some of the columns, pandas will infer the rest

# na_values={ "zipcode": 0 }
#	Specify which values will be considered missing/NA for columns

# error_bad_lines=False
#	Setting this to False will make the function to skip unparseable records
#	(a record with more values than there are columns)

# warn_bad_lines=True
# 	Shown messages when records are skipped

# head(n) returns the first n rows from the DataFrame as a DataFrame
# It also has tail(n)
tax_data.head(4)

# Returns a pandas.core.indexes.base.Index with the DataFrame's column names
tax_data.columns

# Tuple with the dimension of the DataFrame: (rows, columns)
tax_data.shape

# Get a Series with the datatypes of each column of the DataFrame
tax_data.dtypes

# We can apply isna() to any column in a DataFrame, and it will return a Series representing that column,
# with every row showing True or False if the value is NA or not
tax_data.zipcode.isna()
