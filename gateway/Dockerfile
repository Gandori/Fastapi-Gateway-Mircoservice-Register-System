FROM python:3.12-alpine

WORKDIR /microservice

COPY . .

RUN pip install --upgrade pip && pip install .

CMD ["python3.12", "." ]