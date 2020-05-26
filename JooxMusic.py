import requests, json

### FROM https://danbooru.donmai.us/ ###

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
    

def search():
    if api_key == "INSERT API KEY HERE":
        print("GET API KEY FROM LINE ID: hertot")
        raise Exception("Wrong API Key")
    search = input("Search query: ") #example chainsmokers
    result = json.loads(requests.get(failOverAPI()+"/joox?search="+search+"&auth="+api_key).text)
    for num in range(len(result["result"])):
        data = result["result"][num]
        print("{}. {} || {}".format(num+1,data["title"],data["artist"]))
    select = int(input("Number of song: "))
    r = json.loads(requests.get(result["result"][select-1]["extractor"]+"&auth="+api_key).text)
    print("Title: "+result["result"][select-1]["title"])
    print("Artist: "+result["result"][select-1]["artist"])
    print("Album Name: "+r["result"]["album_name"])
    print("Genre: "+r["result"]["genre"])
    print("Language: "+r["result"]["language"])
    print("Link Image: "+r["result"]["images"][0]["url"])
    print("Link Stream: "+r["result"]["play_url"]["medium_play_url"])

search()
