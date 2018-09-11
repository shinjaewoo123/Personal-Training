import requests

url = 'http://127.0.0.1:5000/user'
param_dict = {"my_str_input": "shinjaewoo", "my_int_input": 10}
response = requests.post(url=url, data=param_dict)
# response = requests.post(url=url, data=params)
print(response.status_code)
print(response.json())