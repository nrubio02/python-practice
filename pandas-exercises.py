import pandas as pd

# read_csv returns a pandas DataFrame
# Accepts another parameter 'sep' to indicate separator: sep="\t"
tax_data = pd.read_csv("data/vt_tax_data_2016.csv")

# Specify which columns to read with an array of column names or indexes, and pass it to the 'usecols' argument
cols_names = ['STATE', 'zipcode']
tax_data_v2 = pd.read_csv("data/vt_tax_data_2016.csv", usecols=cols_names)

# Specify number of rows to read
tax_data_v3 = pd.read_csv("data/vt_tax_data_2016.csv", nrows=10)

# Specify how many rows to read, how many rows to skip, indicate that there'll be no header, and set the column names
vt_data_next500 = pd.read_csv("data/vt_tax_data_2016.csv",
                       		  nrows=500,
                       		  skiprows=500,
                       		  header=None,
                       		  names=list(vt_data_first500))

# head(n) returns the first n rows from the DataFrame as a DataFrame.
# It also has tail(n)
tax_data.head(4)

# Returns a pandas.core.indexes.base.Index with the DataFrame's column names
tax_data.columns

# Tuple with the dimension of the DataFrame: (rows, columns)
tax_data.shape

