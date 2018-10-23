from fbchat import Client
from fbchat.models import *
client = Client('dynaslope.swat@gmail.com', 'asdfjkl;1234')

message_id = client.send(Message(text='Sample acknowledgement using reaction emoji sent via Python-AIS'), thread_id='2199956213379612', thread_type=ThreadType.GROUP)
client.reactToMessage(message_id, MessageReaction.LOVE)