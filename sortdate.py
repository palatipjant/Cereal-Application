from datetime import datetime
my_dates = ['2022-04-20', '2022-02-10', '2022-01-01', '2022-04-13']
my_dates.sort(key=lambda date: datetime.strptime(date, "%Y-%m-%d"))
print(my_dates)
