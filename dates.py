import requests
from datetime import date
# pull_requests = requests.get("https://api.github.com/repos/Umuzi-org/tech-department/pulls?id=1")

# print(pull_requests.json())

<<<<<<< HEAD
def pull_requests(owner, repo_name, start_date, end_date):


  pull_requests = requests.get(f"https://api.github.com/repos/{owner}/{repo_name}/pulls?id=1")

  return pull_requests
=======
r = requests.get("https://api.github.com/repos/Itumeleng091slk/pulls")
len(r.json()) == 13
print(r)

g = Github("username","password")
repo = g.get_repo('repo')
date = repo.updated_at
date = int(2020-5-2)
print(date)


# def daterange(start_date, end_date):
#     for n in range(int((end_date - start_date).days)):
#         yield start_date + timedelta(n)

# start_date = date(2020, 1, 12)
# end_date = date(2020, 3, 5)

# for single_date in daterange(start_date,end_date):
#     date_obj = datetime.combine(single_date,datetime.min.time())
#     print(single_date.strftime('%Y-%m-%d:'), 'repo.name')

# def created_at(self):
#     self._completedIfNotSet(self.created_at)
#     return self.created_at.value
  

# for pull in r.get_pulls('all'):
#     print(get_pull)
# parameters = {"sort": 'pushed'}

# for item in resp['updated_at']:
#     print(item['updated_at'])
# def daterange(start_date, end_date):
#     for n in range(int((end_date - start_date).days)):
#         yield start_date + timedelta(n)
>>>>>>> cfa18a94ec560acd84849bcdf94c9072e55f3fa8

print(dir(pull_requests("Umuzi-org","tech-department",18-3-2020,18-4-2020)))

x = {
  "id" : 1,
  'created_at':2019-2-4,
  'updated_at': 2020-4-27,
  'pushed_at': 2020-4-21,

}

<<<<<<< HEAD
# for key, value in x.items():
#   if value < 2018:
#     print(value)
f_date = date(2020, 3, 18)
l_date = date(2020, 4, 18)
pull_requests = l_date - f_date
print(pull_requests.days)
=======
# def get_author(author, repo,start_date,end_date):
#     author_prs = "username:{}/{} type:pr author:{} is merged:{}..{}" .format(repo,start_date,end_start)
#     return author_prs
>>>>>>> cfa18a94ec560acd84849bcdf94c9072e55f3fa8
