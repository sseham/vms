import json
import urllib
import requests

def query(make, model, year):
    url = 'https://parseapi.back4app.com/classes/Car_Model_List'
    headers = {
      'X-Parse-Application-Id': 'hlhoNKjOvEhqzcVAJ1lxjicJLZNVv36GdbboZj3Z', # This is the fake app's application id
      'X-Parse-Master-Key': 'SNMJJF0CZZhTPhLDIqGhTlUNV9r60M2Z5spyWfXW' # This is the fake app's readonly master key
    }
    data = json.loads(requests.get(url, headers=headers).content.decode('utf-8')) # Here you have the data that you need
    print (json.dumps(data, indent=2))
