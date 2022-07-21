# Project3110

# FirstMLProject

# Start Machine learning project

### Software and account requirement

1. Github account  https://github.com/
2. Heroku account  https://dashboard.heroku.com/login
3. VS Code IDE     https://code.visualstudio.com/download
4. GIT cli         https://git-scm.com/downloads


```
conda create -p venv python==3.7 -y

```
conda activate venv/

```
To install requirements folder
 pip install -r requirements.txt

 git status

 git log

 git add .

 git commit -m message

 git origin push main 

 git remote -v

 git branch

 to setup CI/CD in heroku
 heroku_email = madhurya3110@gmail.com
 heroku_api_key = <>
 heroku_app_name = ml-regression-app-3110

 BUILD DOCKER IMAGE

 docker build -t <image_name>:<tag_name> .

 To list docker images

docker images

Run docker image
docker run -p 5000:5000 -e PORT =5000 image id

To check running container in docker
docker ps

To stop docker container

docker stop <container_id>