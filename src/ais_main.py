from fbchat import Client
from fbchat.models import *
import configparser

def send_messenger(email, password, thread_id):
	client = Client('%s', '%s') %(email, password)
	message_id = client.send(Message(text='Sample Message via Python-AIS'), thread_id='%s', thread_type=ThreadType.GROUP) % thread_id

if __name__ == "__main__":
	config = configparser.ConfigParser()
	config.readfp(open('../config/credentials.cfg'))
	send_messenger(config['DYNASLOPE-AIS']['email'], config['DYNASLOPE-AIS']['password'], config['DYNASLOPE-THREAD']['thread_id'])