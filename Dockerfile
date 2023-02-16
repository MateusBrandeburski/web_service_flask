FROM python:3.9.0-alpine
LABEL maintainer "Mateus Brandeburski Ramos <mateus.brandeburski92@gmail.com>"
COPY . /var/www
WORKDIR /var/www
RUN apk update && pip install -r requirements.txt && pip install --upgrade pip
ENTRYPOINT python app.py runserver 0.0.0.0:8000
EXPOSE 8000

