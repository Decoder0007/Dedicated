from git import Repo
from tqdm import tqdm

PATH_OF_GIT_REPO = r'/Users/decoder0007/Desktop/Dedicated/.git'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'Stay Focused. Be Committed'

def dedicate():
    print("Getting Repository...")
    repo = Repo(PATH_OF_GIT_REPO)
    print("Adding Files...")
    repo.git.add(update=True)
    print("Generating Commits...")
    for i in tqdm(range(900)):
        repo.index.commit(COMMIT_MESSAGE)
    print("Retrieving Remote...")
    origin = repo.remote(name='origin')
    print("Pushing...")
    origin.push()
    print("Finish")

dedicate()