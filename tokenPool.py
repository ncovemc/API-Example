import requests, json



def getNewToken(user):
    while True:
        result = json.loads(requests.get("https://pool.boteater.xyz/getToken?user="+user).text)
        if result["status"] == 200:
            print("[ New Token ] "+result["result"])
            return result["result"]
        else:
            if "please wait" in result["reason"]:
                sleeping = int(result["reason"].split(" ")[2])
                print("[ Limitation ] Waiting {} seconds...".format(sleeping))
                time.sleep(sleeping)
            else:
                raise Exception("[ Token Pool ] Unknown error")
        time.sleep(1)

def getCurentToken(user):
    result = json.loads(requests.get("https://pool.boteater.xyz/myToken?user="+user).text)
    if result["status"] == 200:
        return result["result"]
    else:
        raise Exception("[ Token Pool ] Unknown error")

#example login (linepy)
client = LINE(getNewToken("usernya"), appName='IOS\t10.1.1\tiPhone 8\t11.2.5')



#NOTE: Token will change every restart bot ( so if bot ban/limit just restart bot to get new fresh token )
#LIMITATION: 1 get per 5 minutes
#ONE USER API FOR 1 ACCOUNT ( SO IF HAVE 3 BOT TOTAL U NEED 3 USER API )
