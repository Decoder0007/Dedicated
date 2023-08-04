from git import Repo
from tqdm import tqdm

# MacOS: r'/Users/decoder0007/Desktop/Dedicated/.git'
# Windows: r'C:/Users/decod/Desktop/Dedicated/.git'

PATH_OF_GIT_REPO = r'C:/Users/decod/Desktop/Dedicated/.git'

def dedicate():
    commits = int(input("Enter number of commits to push:  "))
    print("Getting Repository...")
    repo = Repo(PATH_OF_GIT_REPO)
    print("Adding Files...")
    repo.git.add(update=True)
    print("Generating Commits...")
    for i in tqdm(range(commits)):
        repo.index.commit('Stay Focused. Be Committed')
    print("Retrieving Remote...")
    origin = repo.remote(name='origin')
    print("Pushing...")
    origin.push()
    print("Finish")

dedicate()
