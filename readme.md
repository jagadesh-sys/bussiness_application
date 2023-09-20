## Installation
1. python3 -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. Run this command "uvicorn main:app"


## Dockerization
1. docker build -t bussiness .
2. docker ps -a
3. if container name main exists then stop it and delete it.
if it doesn't exist then go to step 6
4. docker container stop [CONTAINERID]
5. docker container rm [CONTAINERID]
6. docker run --name bussiness -d -p 5000:5000 main:v1