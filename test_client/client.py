import requests
from datetime import datetime
url = "https://container-2k9juao.containers.anotherwebservice.com:5003/api/test"
# url = "https://container-2k9juao.containers.anotherwebservice.com:5003/api/echo1"
# url = "https://container-2k9juao.containers.anotherwebservice.com:5003/api/echo2"
# url = "http://server-container:5003/api/test"
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
data = {"send-time": now}
response = requests.post(url, json=data, verify=False)
print('client.received=', response.text, 'at', now)
