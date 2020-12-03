FROM python:3.7-alpine
WORKDIR /project
ADD . /project
RUN pip install -r backend/requirements.txt
COPY backend /project
COPY static /static
CMD ["python", "/project/server.py"]

