import requests, json

api_key= "INSERT API KEY HERE"
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
    

def smule():
    if api_key == "INSERT API KEY HERE":
        print("GET API KEY FROM LINE ID: hertot")
        raise Exception("Wrong API Key")
    search = input("Userid Smule: ") 
    result = json.loads(requests.get(failOverAPI()+"/smule?userid="+search+"&auth="+api_key).text)
    print("FirstName: "+result["result"]["user"]["first_name"])
    print("LastName: "+result["result"]["user"]["last_name"])
    print("Location: "+result["result"]["user"]["location"])
    print("Image Link: "+result["result"]["user"]["pic_url"])
    print("Followers: "+result["result"]["user"]["followers"])

smule()
