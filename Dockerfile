FROM ubuntu:18.04

MAINTAINER junseo invalidid56@snu.ac.kr

RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:fkrull/deadsnakes
RUN apt-get update
RUN apt-get install -y --no-install-recommends python3.8 python3.8-dev python3-pip python3-setuptools python3-wheel gcc
RUN apt-get install -y git

RUN python3.8 -m pip install pip --upgrade

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY ./app .

EXPOSE 8000

CMD ["uvicorn", "run", "main:app", "--reload"]
