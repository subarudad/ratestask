FROM python:3.9-slim as rates-api

WORKDIR /ratestask

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ratestask/. .

CMD ["flask", "run", "--host=0.0.0.0"]