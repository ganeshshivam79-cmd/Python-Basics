from dateutil.relativedelta import relativedelta
import pandas as pd

start_date = pd.to_datetime("2020-01-15")
print(start_date)
end_date = pd.to_datetime("2023-07-03")

date_range = pd.date_range(start=start_date, end=end_date, freq='D')
print(date_range)

diff = relativedelta(end_date, start_date)
years = diff.years
months = diff.months
days_left =
print(diff, years, months, days_left)
