#!/usr/bin/python3
import configparser
from datetime import datetime
import os
import sys
import subprocess

todo = []


def set_up_location():
    """The central location for git repos."""
    config_file = os.path.join(os.path.expanduser("~"), ".gitstat.ini")

    def read_loc():
        """Read config file"""
        config = configparser.ConfigParser()
        config.read(config_file)
        location = config["DEFAULT"]["LOCATION"]
        return location

    if os.path.exists(config_file):
        location = read_loc()
    else:
        cwd = os.getcwd()
        answ = input(
            f"If this isn't the root level of your git repos run program again from that location:\n{cwd}\nTo continue write yes.\n> "
        )
        if answ.upper().strip() != "YES":
            sys.exit(0)
        config = configparser.ConfigParser()
        config["DEFAULT"] = {
            "LOCATION": cwd,
        }
        with open(config_file, "w") as f:
            config.write(f)
        location = read_loc()
    return location


# TODO git status --porcelain=v1
def get_stat(path):
    os.chdir(path)
    status = subprocess.run(["git", "status", "-sb"], capture_output=True, text=True)
    if len(status.stdout.replace("\n", "").split(" ")) > 2:  # 2 = nothing to commit
        todo.append("42")
        print("\n" + os.getcwd())
        status = subprocess.run(["git", "status", "-sb"])


def get_info(location):
    user_name = subprocess.run(
        ["git", "config", "user.name"], capture_output=True, text=True
    )
    user_name = user_name.stdout.replace("\n", "")
    time_stamp = datetime.now()
    print(
        f"{time_stamp}\nStatus overview of local git repositories from: {location}\nOwned by {user_name}."
    )


def main(location):
    """No matter how deep in the directory structure are repos placed, unlike the earlier bash version, this will easily scan all, without too verbose output. """
    if location:
        get_info(location)
        for (root, dirs, files) in os.walk(location):
            if ".git" in os.listdir(root):
                get_stat(root)
                #continue
    if not todo:
        print("There is nothing to do.")


if __name__ == "__main__":
    main(set_up_location())

