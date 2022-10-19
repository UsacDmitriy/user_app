FROM python:3.10-alpine

RUN pip install --upgrade pip
RUN pip install pipenv
RUN mkdir -p /usr/scr/app/app
WORKDIR /usr/src/app
COPY Pipfile Pipfile.lock main.py ./
COPY app ./app

RUN pipenv install --system

CMD ["uvicorn", "main:app"]


