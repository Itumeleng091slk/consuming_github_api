from datetime import datetime
from datetime import timedelta, date
import api


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


start_date = date(2019, 12, 1)
end_date = date(2020, 3, 5)

for single_date in daterange(start_date,end_date):
    date_obj = datetime.combine(single_date,datetime.min.time())
    print(single_date.strftime('%Y-%m-%d:'))