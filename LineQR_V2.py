import requests, json

### QR ROTATE LOGIN EXAMPLE ###

token_key= ""
## GET API KEY FROM https://api.boteater.us/get_token ###

header_list= ["android_lite", "chrome", "ios_ipad", "desktopmac", "desktopwin"]

print(header_list)

def login():
    header = input("Insert header: ")
    if header not in header_list:
        raise Exception("Wrong header input")
    result = json.loads(requests.get("https://api.boteater.us/line_qr_v2?header="+header+"&auth="+token_key).text)
    print("QR Link: "+result["result"]["qr_link"])
    print("Login IP: "+result["result"]["login_ip"])
    print("QR Active For 30 Seconds")
    result = json.loads(requests.get(result["result"]["callback"]+"&auth="+token_key).text)
    if result["status"] != 200:
        raise Exception("Timeout!!!")
    print("Pincode: "+result["result"]["pin_code"])
    result = json.loads(requests.get(result["result"]["callback"]+"&auth="+token_key).text)
    if result["status"] != 200:
        raise Exception("Timeout!!!")
    print("Cert: "+result["result"]["cert"])
    print("AuthToken: "+result["result"]["token"])


def loginWithCert():
    header = input("Insert header: ")
    if header not in header_list:
        raise Exception("Wrong header input")
    cert = input("Insert cert: ")
    result = json.loads(requests.get("https://api.boteater.us/line_qr_v2?header="+header+"&cert="+cert+"&auth="+token_key).text)
    print("QR Link: "+result["result"]["qr_link"])
    print("Login IP: "+result["result"]["login_ip"])
    print("QR Active For 30 Seconds")
    result = json.loads(requests.get(result["result"]["callback"]+"&auth="+token_key).text)
    if result["status"] != 200:
        raise Exception("Timeout!!!")
    print("Cert: "+result["result"]["cert"])
    print("AuthToken: "+result["result"]["token"])
    
def loginPushNotifSMS():
    ### INDONESIA REGIONAL ONLY ###
    header = input("Insert header: ")
    number = input("Insert your active phone: ")
    if header not in header_list:
        raise Exception("Wrong header input")
    result = json.loads(requests.get("https://api.boteater.us/line_qr_v2?header="+header+"&number="+number+"&auth="+token_key).text)
    print("QR Link: "+result["result"]["qr_link"])
    print("Login IP: "+result["result"]["login_ip"])
    print("QR Active For 30 Seconds")
    result = json.loads(requests.get(result["result"]["callback"]+"&auth="+token_key).text)
    if result["status"] != 200:
        raise Exception("Timeout!!!")
    print("Pincode code have send to your number")
    result = json.loads(requests.get(result["result"]["callback"]+"&auth="+token_key).text)
    if result["status"] != 200:
        raise Exception("Timeout!!!")
    print("Cert: "+result["result"]["cert"])
    print("AuthToken: "+result["result"]["token"])
    

login()
