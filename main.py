from task_manager.task_manager import TaskManager
from pq import RMQConsumer, RMQProducer
import logging
import sys
import os


def make_config(host, queue, login, password):
    config = dict()
    config['host'] = host
    config['queue'] = queue
    config['login'] = login
    config['password'] = password
    return config

def load_config():
    host = os.environ['MQ_HOST']
    wr_queue = os.environ['MQ_WR_QUEUE']
    rd_queue = os.environ['MQ_RD_QUEUE']
    login = os.environ['MQ_LOGIN']
    password = os.environ['MQ_PASSWORD']
    return host, wr_queue, rd_queue, login, password


# LOGGING SETTINGS
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
log = logging.getLogger()
log.handlers.clear()
log.addHandler(ch)
log.info("Start application")

# RABBIT MQ PRODUCER-CONSUMER SETTINGS
host, wr_queue, rd_queue, login, password = load_config()
producer_config = make_config(host, wr_queue, login, password)
consumer_config = make_config(host, rd_queue, login, password)
producer = RMQProducer(producer_config)
task_manager = TaskManager(producer)
consumer = RMQConsumer(consumer_config, task_manager)
consumer.start_consuming()
