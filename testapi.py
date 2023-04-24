import requests
import json

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/Blog_Post_API/'

# GET METHOD To Get Resources From The SERVER

myToken = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxNCwidXNlcm5hbWUiOiJhYmhpbGFzaCIsImV4cCI6MTcxMjM1MDYwOCwiZW1haWwiOiJhYmhpbGFzaDI4QGdtYWlsLmNvbSIsIm9yaWdfaWF0IjoxNjgyMzUwNjA4fQ.0bqiPvwWXg5i1DVaLXp2kX_T-4bRnFz4Q-5OM5JStBA'

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/Blog_Post_API/'
def get_resource(id=None):

  if id is None:
    head = {'Authorization': 'JWT {}'.format(myToken)}    
    headers = {'content-type': 'application/json'}
    response = requests.get(url = BASE_URL+ENDPOINT,headers=head)
    print(response.json())  

  head = {'Authorization': 'JWT {}'.format(myToken)}  
  headers = {'content-type': 'application/json'}
  response = requests.get(url = BASE_URL+ENDPOINT+str(id),headers=head)
  print(response.json())

get_resource()



















# # POST METHOD To Create Resource Into The SERVER

# def create_resource():  
#   emp_data = {
#       'eno': 400,
#       'ename': 'Ritesh',
#       'esal': 4000,
#       'eaddr': 'Visapur'
#     }
#   resp = requests.post(BASE_URL+ENDPOINT,data=json.dumps(emp_data))
#   print('Status_Code : {}'.format(resp.status_code))
#   print(resp.json())

# # PUT METHOD To Update Resource Into The SERVER

# def update_resource(id):  
#   emp_data = {
#       'id':id,
#       'ename':'Rohan',     
#       'esal': 10000,      
#     }
#   resp = requests.put(BASE_URL+ENDPOINT,data=json.dumps(emp_data))
#   print('Status_Code : {}'.format(resp.status_code))
#   print(resp.json())

# # DELETE METHOD To Update Resource Into The SERVER

# def delete_resource(id):  
#   data = {
#       'id':id      
#     }
#   resp = requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data))
#   print('Status_Code : {}'.format(resp.status_code))
#   print(resp.json())

# # create_resource()
# update_resource(3)
# # delete_resource(3)