FROM python:3.6-alpine

ADD main.py /srv/src/main.py
ADD setup.py /srv/src/setup.py

RUN \
 pip install --upgrade pip && \
 pip install /srv/src && \
 rm -rf /srv/src/*

EXPOSE 8080

ENTRYPOINT ["/usr/local/bin/python3", "-m", "main"]
