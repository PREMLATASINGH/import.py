import math 
print(math.sqrt(64))
print(math.pi)
import random
print(random.randint(1,100))
print(random.choice(['banana','apple','cherry','kiwi']))
import json
data={'name':'prema','age':23}
json_str=json.dumps(data)
print(json_str)
print(type(json_str))
parsed_data=json.loads(json_str)
print(parsed_data)
print(type(parsed_data))
from datetime import datetime,timedelta
now=datetime.now()
print(now)
yesterday=now-timedelta(days=1)
print(yesterday)
import time
print(time.time())
time.sleep(2)
print(time.time())