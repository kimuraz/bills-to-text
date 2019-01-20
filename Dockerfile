FROM python:3.6-alpine

WORKDIR /opt/bills-to-text

RUN apk update && apk add make

COPY . .

RUN make install

VOLUME ./imgs:/opt/bills-to-text/imgs

EXPOSE "5000:5000"

CMD FLASK_APP=api.py flask run
