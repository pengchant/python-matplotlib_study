import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=starts"
r = requests.get(url)
print("status_code:" + str(r.status_code))

response_dict = r.json()  
print(response_dict.keys())

print("total counts" + str(response_dict['total_count']))

# 有关仓库的信息
repo_dicts = response_dict['items']
print("repositories returned:", len(repo_dicts))

# 第一个item
repo_dict = repo_dicts[0]
print("len of key:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)


print("\n the selected information about repository:")
for repo_dict in repo_dicts:
    print("Name:", repo_dict['name'])
    print("Owner:", repo_dict['owner']['login'])
    print("Starts:", repo_dict['stargazers_count'])
    print("Repository:", repo_dict['html_url'])
    print("Created:", repo_dict["created_at"])
    print("Updated:", repo_dict['updated_at'])
    print("Discription:", repo_dict['description'])