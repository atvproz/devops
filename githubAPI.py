import yaml
from github import Github

# Loading credentials.yml
data = yaml.safe_load(open('pica0104-credentials.yml'))

# Extract the user and the token from the object
user = data['username']
token = data['token']

try:
    # Creating a GitHub object using personal token
    g = Github(token)

    # Get the repo from the GitHub repo
    repo = g.get_repo(f"{user}/devops")  # we forgot the username  which is the reason for the error

    # Initialize counters for branches, pull requests, and commits
    branch_count = 0
    pull_request_count = 0
    commit_count = 0

    # Iterate through branches and count them
    for _ in repo.get_branches():
        branch_count += 1

    # Iterate through pull requests and count them
    for _ in repo.get_pulls(state='all'):
        pull_request_count += 1

    # Get the default branch's commit SHA and count commits
    default_branch = repo.get_branch(repo.default_branch)  # Get the default branch object
    for _ in repo.get_commits(default_branch.commit.sha):
        commit_count += 1

    # Show the number of branches, pull requests, and commits
    print('Branches: ', branch_count)
    print('Pull requests: ', pull_request_count)
    print('Commits: ', commit_count)
except Exception as e:
    print('Message was an error', e)






