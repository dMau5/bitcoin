FROM ubuntu:20.04

WORKDIR /opt
ENV FLASK_APP=app

RUN apt update && \
    apt install -y build-essential python3.8-dev git && \
    apt install -y python3-pip && \
    apt clean

LABEL "requirements"="25.11.2020"

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
RUN pip3 install app

EXPOSE 5000

CMD ["flask", "run", "-h", "0.0.0.0"]