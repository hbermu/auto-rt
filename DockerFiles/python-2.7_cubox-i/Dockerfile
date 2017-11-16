FROM resin/cubox-i-python:2.7-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./auto-rt.py" ]