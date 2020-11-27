FROM ubuntu:20.04

WORKDIR /opt

RUN apt update && \
    apt install -y build-essential python3.8-dev git && \
    apt install -y python3-pip && \
    apt clean

LABEL "requirements"="25.11.2020"

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
RUN pip3 install worker

CMD ["python3", "-m", "worker"]