FROM python:alpine

WORKDIR /app

COPY requirements.txt

RUN pip install -r requirements.txt

COPY src/.

CMD [ "python", "./run.py" ]