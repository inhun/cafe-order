import requests
import time
import paho.mqtt.client as mqtt
import json



order = dict()

while(1):
    res = requests.get('http://localhost:5000/order')
    data = res.json()
    has_item = bool(data)

    if (has_item):
        order = data
        break
        
    time.sleep(1)


send = dict()
send['command'] = 'order'
send['msg'] = order

client = mqtt.Client()

client.connect('192.168.43.7', 1883)
client.loop_start()
client.publish('/supervisor', json.dumps(send), 1)

client.loop_stop()
client.disconnect()