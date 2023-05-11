FROM python:3.7-alphine

ENV PYTHONUNBUFFURED 1
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir app