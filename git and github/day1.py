#Git and Github:

"""
Git is a VCS that keeps the track of our project code.
An online platform to store our project code."""

#Steps to follow:
"""
1. Initialize the git : git init (only one time for a project)
2. Connect system folder with github repository : git remote add origin {ssh_key} (only one time for a project)
# U stands for UNtracked...  # A stands for added in git   
# M stands for M
3. Add files to github : git add {file_name}}  (to add all files we use git add . )
4. Commit the files : git commit -m "Message"
5. Push the git to github : git push -u origin {branch_name} // git push origin {branch_name}
# -u : Upstream that saves the repository
# At first push, it is recommended to use : git push -u origin {branch_name} 
6. To pull the code from github : git pull origin {branch_name}
"""

#To create a new branch : git branch {branch_name}
"""
TO view all the branches : git branch // git branch -a
To switch between the branches : git switch {branch_name}
"""