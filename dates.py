import github

pull_requests = requests.get("https://api.github.com/repos/Umuzi-org/tech-department/pulls?id=434")

print(pull_requests.json())

def pull_requests(owner, repo_name, start_date, end_date):

  pull_requests = requests.get(f"https://api.github.com/repos/{owner}/{repo_name}/pulls?id=434")

  return pull_requests

print(dir(pull_requests("Umuzi-org","tech-department",18-3-2019,18-4-2020)))

x = {
  'created_at': 2018,
  'updated_at': 2020,
  'pushed_at': 2020,
  'closed_at': 2021 


 }

for key, value in x.items():
  if value < 2020 :
    print(value)
