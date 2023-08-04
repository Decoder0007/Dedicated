from git import Repo

PATH_OF_GIT_REPO = r'/Users/decoder0007/Desktop/Dedicated/.git'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'Stay Focused. Be Committed'

def dedicate():
    repo = Repo(PATH_OF_GIT_REPO)
    repo.git.add(update=True)
    for i in range(99):
        repo.index.commit(COMMIT_MESSAGE)
    origin = repo.remote(name='origin')
    origin.push()

dedicate()