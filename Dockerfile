FROM ubuntu:18.04

MAINTAINER JSK invalidid56@snu.ac.kr

RUN apt-get update
RUN apt-get update
RUN apt-get install -y --no-install-recommends python3.8 python3.8-dev python3-pip
RUN apt-get install -y git
RUN apt install -y nginx

COPY fastapi_nginx /etc/nginx/sites-available/fastapi_nginx
RUN ln -s /etc/nginx/sites-available/fastapi_nginx /etc/nginx/sites-enabled/fastapi_nginx

RUN python3.8 -m pip install pip --upgrade

COPY requirements.txt ./
RUN pip install -r requirements.txt


COPY ./app .

EXPOSE 8000

CMD ["nginx"]
CMD ["nginx", "-t"]
CMD ["uvicorn", "run", "main:app", "--reload"]
