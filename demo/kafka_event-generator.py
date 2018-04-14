import time
import json
import uuid
from kafka import KafkaProducer
from random import randint
import random
countryList = []
countryList.append("Sweden")
countryList.append("Norway")
countryList.append("Brazil")

producer = KafkaProducer(bootstrap_servers='localhost:9092')
while 1==1:
	#message = {'id':str(uuid.uuid4()), 'country': countryList[randint(0,2)],'amount':randint(0,3000), 'timestamp':str(int(round(time.time() * 1000))), 'approved': bool(random.getrandbits(1))} 
	message = {'guid':str(uuid.uuid4()), 'timestamp':str(int(round(time.time() * 1000))), 'customerId':1, 'firstName':'asd', 'lastName':'Lundsten','socialSecurityNumber':'198808159999', 'type':'CustomerCreatedEvent'}
	producer.send('kafka.summit.events', key='123', value=json.dumps(message).encode('utf-8'))
	print json.dumps(message)
