import requests, json, time

api_key= "INSERT API KEY HERE"
## GET API KEY FROM LINE ID: hertot ##
## PREMIUM APIKEY 1$ PER MONTH ##

header_list= ["android_lite", "chrome", "ios_ipad", "desktopmac", "desktopwin"]

sysname = "BE-Team" ## YOU CAN USE CUSTOM SYSNAME


def login():
    if api_key == "INSERT API KEY HERE":
        print("GET API KEY FROM LINE ID: hertot")
        raise Exception("Wrong API Key")
    print(header_list)
    header = input("Insert header: ")
    if header not in header_list:
        raise Exception("Wrong header input")
    result = json.loads(requests.get("https://api.be-team.me/qrv2?header="+header+"&sysname="+sysname+"&auth="+api_key).text)
    print("Your QR Link: "+result["result"]["qr"])
    print("Your Callback Pincode: "+result["result"]["cb_pincode"])
    print("Your Callback Token: "+result["result"]["cb_token"])
    for num in range(120):
        r = json.loads(requests.get(result["result"]["cb_pincode"]).text)
        if r["result"] != "not ready":
            print("Your Pincode: "+r["result"])
            break
        time.sleep(0.5)
    for num in range(120):
        r = json.loads(requests.get(result["result"]["cb_token"]).text)
        if r["result"]["token"] != "not ready":
            print("Your Token: "+r["result"]["token"])
            print("Your Cert: "+r["result"]["cert"])
            break
        time.sleep(0.5)

def loginWithCert():
    if api_key == "INSERT API KEY HERE":
        print("GET API KEY FROM LINE ID: hertot")
        raise Exception("Wrong API Key")
    print(header_list)
    header = input("Insert header: ")
    if header not in header_list:
        raise Exception("Wrong header input")
    cert = input("Insert cert: ")
    result = json.loads(requests.get("https://api.be-team.me/qrv2?header="+header+"&sysname="+sysname+"&cert="+cert+"&auth="+api_key).text)
    print("Your QR Link: "+result["result"]["qr"])
    print("Your Callback Token: "+result["result"]["cb_token"])
    for num in range(120):
        r = json.loads(requests.get(result["result"]["cb_token"]).text)
        if r["result"]["token"] != "not ready":
            print("Your Token: "+r["result"]["token"])
            print("Your Cert: "+r["result"]["cert"])
            break
        time.sleep(0.5)


login()
