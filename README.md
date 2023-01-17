# RUFUS
This is project for specific fact about local repo.

task is to create a program that prints specific facts about a local git repository. You can use any language, and you are welcome to import existing packages.
# Your program should take in one argument:
git_dir: directory in which to assess git status
Your program should print the following things:

active branch (boolean)
whether repository files have been modified (boolean)
whether the current head commit was authored in the last week (boolean)
whether the current head commit was authored by Rufus (boolean)


# Sample Output Format
The program should print something like

active branch: master

local changes: False

recent commit: True

blame Rufus: True

#To Run the application you have to follow these steps:

1-install following library after installing python3

gitpython (pip install gitpython)

2-if you want to clone repo from github first do "git init" then "git clone (path to repository)"

3-run the command below

python3 app.py "path to local repository"

for example :python3 app.py /home/alirezamahinparvar/new/Python-projects
