FROM ubuntu:18.10

# Install python and flask.
RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-pip nginx
RUN pip3 install uwsgi flask

# Add static content and entry point to container.
ADD server /recommender/server
ADD static /recommender/static
ADD entry.sh /recommender/entry.sh

# Make sure entry point script is runnable.
RUN chmod +x /recommender/entry.sh

# Expose port 5000 since that is the port server.py listens to.
EXPOSE 5000

# Run entry script once the container is ready to go.
ENTRYPOINT exec /recommender/entry.sh
