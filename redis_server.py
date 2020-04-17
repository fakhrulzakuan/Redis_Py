import redis
import time
import traceback

r = redis.StrictRedis(host='localhost', port=6379)                          
p = r.pubsub()                                                              
p.subscribe('redistTest')                                                 

while True:                                                                
    message = p.get_message() 

    if message:                                                           
        command = message['data']                                           
        print command

    time.sleep(0.1)


