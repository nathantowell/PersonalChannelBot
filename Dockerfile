FROM python:slim

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY src/ .

CMD [ "python", "./run.py" ]