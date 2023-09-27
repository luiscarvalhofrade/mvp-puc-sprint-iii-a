# syntax=docker/dockerfile:1
FROM python:3.11.5-slim
WORKDIR /mvp-puc-sprint-iii/mvp-puc-sprint-iii-a
COPY . /mvp-puc-sprint-iii-a
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 90
CMD ["flask", "--app" , "service", "run"]