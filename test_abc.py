import requests
import json
import jsonpath

#Test_case1
def test_register1():
    URL = ("https://secure-oasis-12806.herokuapp.com/api/register")
    f = open('/home/shivam/Documents/Flolabs/file1.json','r')
    
    request_json = json.loads(f.read())
    print(request_json)
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", URL, headers=headers, data=json.dumps(request_json))
    print(response)
    assert response.status_code == 201,"test pass"
    print(response.text)

#Test_Case2
def test_register2():
    URL = ("https://secure-oasis-12806.herokuapp.com/api/register")
    f = open('/home/shivam/Documents/Flolabs/file2.json','r')
    
    request_json = json.loads(f.read())
    print(request_json)
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", URL, headers=headers, data=json.dumps(request_json))
    print(response)
    assert response.status_code == 400,"test pass"
    print(response.text)

#Test_Case3
def test_register3():
    URL = ("https://secure-oasis-12806.herokuapp.com/api/register")
    f = open('/home/shivam/Documents/Flolabs/file3.json','r')
    
    request_json = json.loads(f.read())
    print(request_json)
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", URL, headers=headers, data=json.dumps(request_json))
    print(response)
    assert response.status_code == 201,"test fail"                #Bad_request
    print(response.text)

#Test_Case4
def test_register4():
    URL = ("https://secure-oasis-12806.herokuapp.com/api/register")
    f = open('/home/shivam/Documents/Flolabs/file4.json','r')
    
    request_json = json.loads(f.read())
    print(request_json)
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", URL, headers=headers, data=json.dumps(request_json))
    print(response)
    assert response.status_code == 201,"test fail"
    print(response.text)

#Test_Case5
def test_register5():
    URL = ("https://secure-oasis-12806.herokuapp.com/api/register")
    f = open('/home/shivam/Documents/Flolabs/file5.json','r')
    
    request_json = json.loads(f.read())
    print(request_json)
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", URL, headers=headers, data=json.dumps(request_json))
    print(response)
    assert response.status_code == 400,"test fail" 
    print(response.text)

#Test_Case6
def test_register6():
    URL = ("https://secure-oasis-12806.herokuapp.com//api/register")
    f = open('/home/shivam/Documents/Flolabs/file3.json','r')
    
    request_json = json.loads(f.read())
    print(request_json)
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", URL, headers=headers, data=json.dumps(request_json))
    print(response)
    assert response.status_code == 500,"test fail internal server error"       #500_internal_server_error
    print(response.text)


#Test_Case7
def test_register7():
    URL = ("https://secure-oasis-12806.herokuapp.com/api/register")
    f = open('/home/shivam/Documents/Flolabs/file3.json','r')
    
    request_json = json.loads(f.read())
    print(request_json)
    headers = {'Content-Type': 'application/json'}
    response = requests.request("GET", URL, headers=headers, data=json.dumps(request_json))
    print(response)
    assert response.status_code == 200,"test fail"                 #405_error_should_be_come
    print(response.text)