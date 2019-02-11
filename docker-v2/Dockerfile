FROM python:3.6-alpine

ADD server /srv/src/server
ADD setup.py /srv/src/setup.py

RUN \
 apk add --update build-base openssl-dev libffi-dev && \
 pip install -U pip wheel && \
 pip wheel --wheel-dir=/srv/wheels /srv/src/ && \
 pip install /srv/wheels/* && rm -rf /srv/wheels && rm -rf /srv/src/*

EXPOSE 8080

ENTRYPOINT ["/usr/local/bin/python3", "-m", "server"]