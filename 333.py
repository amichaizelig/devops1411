from datetime import datetime
import requests
response = requests.get("https://github.com")
if response.status_code == 200:
    print("github is ok")
#from time import sleep
print(datetime.now())
#sleep(10)
print(datetime.now())