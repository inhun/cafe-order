import requests
import polling

a = polling.poll(
    lambda: requests.get('http://google.com').status_code == 200,
    step=60,
    poll_forever=True
)

print(a)