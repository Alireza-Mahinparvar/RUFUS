import git
import datetime
import sys
def git_status(git_dir):
    repo = git.Repo(git_dir)
    active_branch = repo.active_branch.name
    local_changes = repo.is_dirty()
    head_commit = repo.head.commit
    authored_date = datetime.datetime.fromtimestamp(head_commit.authored_date)
    recent_commit = datetime.datetime.now() - authored_date < datetime.timedelta(days=7)
    blame_rufus = head_commit.author.name == "Rufus"
    print("active branch: ", active_branch)
    print("local changes: ", local_changes)
    print("recent commit: ", recent_commit)
    print("blame Rufus: ", blame_rufus)

if __name__ == "__main__":
    git_dir = sys.argv[1]
    git_status(git_dir)
