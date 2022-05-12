FROM python:3.10.4-slim-buster

LABEL maintainer="Ivan Nedomerkov <test@gmail.com>"

COPY . /

RUN pip install -r requirements.txt && pip install gunicorn

ENTRYPOINT ["/runserver.sh"]
