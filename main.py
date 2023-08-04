from git import Repo
from tqdm import tqdm
import os

PATH_OF_GIT_REPO = r'C:/Users/decod/Desktop/Dedicated/.git'

def dedicate():
    os.system("cls")
    print("Getting Repository...")
    repo = Repo(PATH_OF_GIT_REPO)
    print("Adding Files...")
    repo.git.add(update=True)
    print("Generating Commits...")
    for i in tqdm(range((314159-285837)-100)):
        repo.index.commit('Stay Focused. Be Committed')
    print("Retrieving Remote...")
    origin = repo.remote(name='origin')
    print("Pushing...")
    origin.push()
    print("Finish")

dedicate()
