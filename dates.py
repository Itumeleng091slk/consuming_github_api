import github

user = "Umuzi-org"
repo = "tech-department"

def pull_request(owner, repo_name, start_date, end_date):
    return pull_requests.json()
pull_requests = requests.get(f"https://api.github.com/repos/{user}/{repo}/pulls/338/commits")
print(pull_requests.json())

x = {
  'created_at': 2018,
  'updated_at': 2020,
  'pushed_at': 2020,
  'closed_at': 2021 


 }

for key, value in x.items():
  if value < 2020 :
    print(value)
