import requests, json

api_key= "INSERT API KEY HERE"

header_list= ["chrome", "ios_ipad", "desktopmac", "desktopwin"]

## GET API KEY FROM LINE ID: hertot ###
def failOverAPI():
    try:
        result = requests.get("https://api.boteater.xyz",timeout=0.5)
        if result.status_code == 200:
            return "https://api.boteater.xyz"
        else:
            return "https://api.boteater.us"
    except:
        return "https://api.boteater.us"
    
def convert():
    if api_key == "INSERT API KEY HERE":
        print("GET API KEY FROM LINE ID: hertot")
        raise Exception("Wrong API Key")
    token = input("Your Primary Token: ")
    print(header_list)
    header = input("Insert header: ")
    if header not in header_list:
        raise Exception("Wrong header input")
    result = json.loads(requests.get(failOverAPI()+"/primary2second?token="+token+"&header="+header+"&auth="+api_key).text)
    print("AuthToken: "+ result["result"]["token"])
    print("Cert: "+ result["result"]["cert"])
        

convert()
