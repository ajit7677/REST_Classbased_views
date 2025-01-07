import requests
import json

def get_data(url):
    response = requests.get(url)
    data = response.json()
    print(data)

def insert_data(url):
    data = {
        'roll_no':22,
        'name': 'Diesel Carry',
        'mobile' : 3329023,
        'country' : 'UK',
        'email' :'diesel.carry@gmail.com'
    }
    json_data = json.dumps(data)
    resp = requests.post(url=url, data=json_data)
    d = resp.json()
    print(d)
def crud_data(url, id=None):
    data = dict()
    if id is not None:
        data = {"id":id}
    json_data = json.dumps(data)
    response = requests.get(url=url, data= json_data)
    crud = response.json()
    print(crud)
def update_data(url):
    data = {
        'roll_no': 23,
        'mobile': 24234234,
    }
    json_data = json.dumps(data)
    res = requests.put(url=url, data=json_data)
    dd= res.json()
    print(dd)
def Delete(url):
    data = {
        'roll_no':22,
    }
    json_data = json.dumps(data)
    resp = requests.delete(url=url, data=json_data)
    d = resp.json()
    print(d)
# get_data(url="http://127.0.0.1:8000/info/2")
# crud_data("http://127.0.0.1:8000/crud/")
# insert_data("http://127.0.0.1:8000/crud/")
update_data("http://127.0.0.1:8000/crud/")
# Delete("http://127.0.0.1:8000/crud/")


