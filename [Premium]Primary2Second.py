import requests, json

api_key= "INSERT API KEY HERE"
## GET API KEY FROM LINE ID: hertot ##
## PREMIUM APIKEY 1$ PER MONTH ##

header_list= ["chrome", "ios_ipad", "desktopmac", "desktopwin"]

    
def convert():
    if api_key == "INSERT API KEY HERE":
        print("GET API KEY FROM LINE ID: hertot")
        raise Exception("Wrong API Key")
    token = input("Your Primary Token: ")
    print(header_list)
    header = input("Insert header: ")
    if header not in header_list:
        raise Exception("Wrong header input")
    result = json.loads(requests.get("https://api.be-team.me/primary2second?token="+token+"&header="+header+"&auth="+api_key).text)
    print("AuthToken: "+ result["result"]["token"])
    print("Cert: "+ result["result"]["cert"])
        

convert()
