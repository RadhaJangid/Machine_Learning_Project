# Machine_Learning_Project
This is my First Machine Learning Project
## Start Machine  Learning Project.

### Software and account Requirement.
1. [Github account](https://github.com/)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT CLI](https://git-scm.com/downloads)
5. [GIT DOCUMANTATION](https://git-scm.com/docs/gittutorial)

### creating conda environment
conda create -p <environment_name> python==3.7 -y
conda create -p radhe python==3.7 -y 

'''
## for activating virtual environment
conda activate radhe/

or

conda activate radhe

'''
pip install -r requirements.txt

'''
To add files git

'''
git add .

or

git add filename

'''

To ignore file/folder from git we can write name of file / folder in git.gitignore file
To check git status

'''
git status
'''

To check all version maintained by git

'''
git log
'''

To create version/commit all changes by git 

'''
git commit -m 'message'
eg- git commit -m "simple flask app"
'''


To send changes/version to github

'''
git push origin main
'''

To check remote url

'''
git remote -v
'''

## To setup CI/CD pipeline in heroku we need 3 information
   1.HEROKU_EMAIL = jangidradha1299@gamil.com
   2.HEROKU_API_KEY = 8a042077-c20d-4ea7-a084-0642d6ca95a5
   3.HEROKU_APP_NAME = mlregreapp

## Build docker image
   '''
   docker build -t <image_name>:<tagname> .  
   NOTE: IMAGE NAME FOR DOCKER MUST BE LOWERCASE

   (. = location of the doctor file )
   '''

## To list docker images
   '''
   docker images
 
   '''
## RUN docker images
'''
    docker run -p 5000:5000 -e PORT=5000 <image_id>

'''

## To check running cointainer in docker
'''
docker ps
'''


## To stop docker cointainer 
'''
docker stop <cointainer_id>
'''




 