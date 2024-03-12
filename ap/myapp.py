import requests
import json
URL ="http://127.0.0.1:8000/"
def data_post():
   
    data={
        'name':'son',
        'roll':8,
        'city':'khandwa'

    }

    jdata=json.dumps(data)

    r=requests.post( url = URL , data = jdata)
    data=r.json()
    # data = json.loads(r.text)
    print(data)


def dataget(id = None):
    dataa = {}
    if id is not None:
        
        dataa={'id':id}
    jsondata=json.dumps(dataa)
    r=requests.get(url=URL,data=jsondata)
    data=r.json()
    print(data)



# dataget()

def data_update():
       
    data={
        'id':4,
        'name':'soname',
        
        'city':'indore'

    }

    jdata=json.dumps(data)

    r=requests.put( url = URL , data = jdata)
    data=r.json()
    # data = json.loads(r.text)
    print(data)


# data_update()
def data_update():
       
    data={'id':4,}

    jdata=json.dumps(data)
    r=requests.put( url = URL , data = jdata)
    data=r.json()
    # data = json.loads(r.text)
    print(data)