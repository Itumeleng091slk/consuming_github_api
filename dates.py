from github import Github
import urllib3
import requests
import json
from datetime import datetime
from datetime import timedelta, date
from api import repos

from secrets import username
from secrets import password
from secrets import token

r = requests.get("https://api.github.com/repos/Itumeleng091slk/pulls")
len(r.json()) == 13
print(r)

# g = Github("username","password")
# repo = g.get_repo('repo')
# date = repo.updated_at
# date = int(2020-5-2)
# print(date)
# for pull in r.get_pulls('all'):
#     print(get_pull)
# parameters = {"sort": 'pushed'}

# for item in resp['updated_at']:
#     print(item['updated_at'])
# def daterange(start_date, end_date):
#     for n in range(int((end_date - start_date).days)):
#         yield start_date + timedelta(n)


# start_date = date(2020, 1, 12)
# end_date = date(2020, 3, 5)

# for single_date in daterange(start_date,end_date):
#     date_obj = datetime.combine(single_date,datetime.min.time())
#     print(single_date.strftime('%Y-%m-%d:'), 'repos')

# def get_author(author, repo,start_date,end_date):
#     author_prs = "username:{}/{} type:pr author:{} is merged:{}..{}" .format(repo,start_date,end_start)
#     return author_prs
