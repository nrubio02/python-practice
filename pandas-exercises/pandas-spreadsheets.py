import pandas as pd

survey_data = pd.read_excel("../data/fcc-new-coder-survey.xlsx")

# read_excel() uses the following same arguments as read_csv: nrows, skiprows, dtype, usecols. For Excel files though, usecols
# also accepts column letters, e.g: "A:D, F"

# sheet_name
#   Used to select which sheet is loaded. Pass an integer to indicate sheet index, or a string to indicate
#   the sheet name. Pass None to indicate all sheets, but in this case the functino will return a Dictionary
#   with key = sheetname and value = a DataFrame

# Boolean values
# If we set a column's type to bool, any missing/unrecognized value will be defaulted to True

# true_values
#   List of values to be considered boolean True

# false_values
#   List of values to be considered boolean False

# parse_dates
#   Interpret the specified columns as dates. Accepted values for this arguments are:
#       - list of column name/number
#       - list of lists, indicating columns that should be combined in the parse
#       - dictionary, with key = new column name, and value = list of columns to be parsed together

# Non-standard datetimes
# parse_dates can't convert non-standard formats, so we need this function to deal with that data post-import:

# format_string = "%m%d%Y %H:%M:%S"  # e.g 03292022 13:42:23
# survey["column_name"] = pd.to_datetime(survey["column_name"], format=format_string)

# Appending DataFrames - For files that contain multiple sheets
all_responses = pd.DataFrame()

survey = pd.read_excel("../data/fcc-new-coder-survey.xlsx", sheet_name=None)

for sheet_name, frame in survey.items():
    frame["Year"] = sheet_name
    all_responses = all_responses.append(frame)

all_responses.Year.unique()

