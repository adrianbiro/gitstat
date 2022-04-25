#!/usr/bin/python3
import subprocess
import os
from datetime import datetime

LOCATION = "/home/adrian/gits"
#os.chdir("/home/adrian/gits/learn/")
def get_stat():
    status = subprocess.run(["git", "status", "-sb"], capture_output=True, text=True)
    if len(status.stdout.replace("\n", "").split(" ")) > 2:  # 2 = nothing to commit
        print(os.getcwd())
        status = subprocess.run(["git", "status", "-sb"])
get_stat()

def get_info():
    user_name = subprocess.run(["git", "config", "user.name"], capture_output=True, text=True)
    user_name = user_name.stdout.replace("\n", "")
    time_stamp = datetime.now()
    print(f'{time_stamp}\nStatus overview of local git repositories from {LOCATION} owned by {user_name}.')



