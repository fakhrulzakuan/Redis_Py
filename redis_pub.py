import redis
import random

r = redis.StrictRedis(host='localhost', port=6379)               

p = r.pubsub()                                                    

print("Starting main scripts...")
while 1:
    rand = random.randint(0, 10)
    r.publish('redistTest', [1,rand])                                  

print("Done")

