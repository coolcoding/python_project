#create a new repository on the command line
touch README.md
git init
git remote add origin git@github.com:coolcoding/python_project.git
git add README.md
git commit -m "first commit"
git push -u origin master
git pull origin master
