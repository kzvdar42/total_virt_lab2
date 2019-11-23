FROM python:3
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
COPY ./wait-for-it.sh .
CMD ./wait-for-it.sh ${MQ_HOST}:${MQ_PORT} -t 20 && \
    python ./main.py