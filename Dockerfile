FROM python:3.9.13-alpine

RUN apk --update add bash nano
WORKDIR /var/www/

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]