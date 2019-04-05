FROM ubuntu:18.10

RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-pip nginx
RUN pip3 install uwsgi flask


ADD server /recommender/server
ADD static /recommender/static
ADD entry.sh /recommender/entry.sh

RUN chmod +x /recommender/entry.sh

EXPOSE 5000

ENTRYPOINT exec /recommender/entry.sh

