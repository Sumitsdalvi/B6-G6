
from pydoc import resolve
import requests

# abs_url = "http://127.0.0.1:8000/create/"
# abs_url = "http://127.0.0.1:8000/retrieve/"
# abs_url = "http://127.0.0.1:8000/retrieve/2/"
# abs_url = "http://127.0.0.1:8000/update/2/"
# abs_url = "http://127.0.0.1:8000/delete/2/"
abs_url = "http://127.0.0.1:8000/create/"
data = None   
#data = {"name":"sumit"}
resp_get = requests.get(abs_url,data=data)   
resp_dict = dict(resp_get.__dict__)
i = 1
print("All details are :- ")
for key,value in resp_dict.items():
    if i == 1:
        i = 0
        continue
    if key == 'headers':
        new_dict = dict(value)
        for k,val in new_dict.items():
            print(k,"--",val)
        continue
    print(key,"--",value)
