from fbchat import Client
from fbchat.models import *
import configparser

def initialize():
	config = configparser.ConfigParser()
	config.readfp(open('../config/credentials.cfg'))
	client = Client(config['DYNASLOPE-AIS']['email'], config['DYNASLOPE-AIS']['password'])

def send_messenger():
	initialize()
	message_id = client.send(Message(text='Sample Message via Python-AIS'), thread_id='2199956213379612', thread_type=ThreadType.GROUP)

if __name__ == "__main__":
    send_messenger()
