FROM python:alpine3.17 
WORKDIR /usr/src/app/ 
COPY . .  
RUN pip install -r requirements.txt
COPY tokener . 
ENTRYPOINT ["./tokener"]
