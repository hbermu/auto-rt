FROM python:2.7-alpine3.6

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./auto-rt.py" ]