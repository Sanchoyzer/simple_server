FROM python:3.6-alpine

RUN pip install -U pip python-dotenv
RUN mkdir -p /usr/local/etc/simple_server

WORKDIR /usr/local/etc/simple_server

ADD .env .
ADD main.py .

EXPOSE 8080

ENTRYPOINT ["/usr/local/bin/python3", "/usr/local/etc/simple_server/main.py"]