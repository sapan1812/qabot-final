# A) Run on local system via git hub clone. https://github.com/sapan1812/qabot-final.git
1) Go to project directory & open command prompt/terminal
2) To train model (Skip if model is trained)
   "rasa train"
   
3) Once model training is completed
   "rasa shell"
   Please observe if rasa server on localhost running with 5005 port with an input prompt
   
4) Open another command prompt or terminal instance
   execute "rasa run actions"
   Please observe if all actions are loaded and localhost server with 5055 port is running.
   
5) Kickoff rasa bot with typing HI in Rasa shell terminal/command prompt
6) Select questions language as Python

# B ) Run on local system with Docker commands
-- Prerequisite is Docker on windows or linux need to be installed. It will create a virtual container environment in system with dedicated memory

1) Download project via github :https://github.com/sapan1812/qabot-final.git
2) Go to project directory & open command prompt/terminal
3) docker build . --no-cache -t sapan1812/qabot
4) go to project directory -> actions folder -> execute below command
   docker build . --no-cache -t sapan1812/qabotactions:1.1
   
5) Once step 3 & 4 is completed then execute training command
docker run #--user 1001 -v %cd%:/app sapan1812/qabot train

6) Create connection to be used 
docker network create qabot-connect

7) run action server first with default port 5055 & newly created connections 
# run actions
docker run -d -v %cd%:/app/actions --net qabot_connect --name qabot-action sapan1812/qabotactions:1.1

8) Run rasa shell with 5005 port with user ( replace %cd% with $(pwd) in case of linux system)
docker run #user 1001 -it -v %cd%:/app -p 5005:5005 #net qabot_connect  sapan1812/qabot shell


# C) Execute with docker compose commands
1. install docker on Windows
2. go to cloned repository folder
3. open command line & execute  : "docker-compose up"
4. once all 3 services are started then click on Rasa-X : localhost:5002/login or any same url shown on console.

#Once Rasa-x opened
1. go to left panel
2. open Training menu
3. Update Model -> Train model
