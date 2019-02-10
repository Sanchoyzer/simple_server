docker container prune
docker rmi image

docker build -f docker-v1/Dockerfile -t image:tag .
docker run -p 8080:8080 -v ~/work/simple_server/log:/usr/local/etc/simple_server/log image:tag