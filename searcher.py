import requests
import json


def truecaller_search(token, num):
    g = "https://account-asia-south1.truecaller.com/v2.1/credentials/check?encoding=json"
    h = {
        "Host": "account-asia-south1.truecaller.com",
        "authorization": token,
        "content-type": "application/json; charset=UTF-8",
        "content-length": "42",
        "accept-encoding": "gzip",
        "user-agent": "Truecaller/11.5.7 (Android;10)"
    }
    requests.post(g, headers=h, timeout=5, data={"reason": "restored_from_account_manager"})

    turl = "https://search5-noneu.truecaller.com/v2/search?q=" + num + "&countryCode=IN&type=4&locAddr=&placement=SEARCHRESULTS%2CHISTORY%2CDETAILS&encoding=json"
    theaders = {
        "user-agent": "Truecaller/11.5.7 (Android;10)",
        "Accept-Encoding": "gzip",
        "authorization": token,
        "Host": "search5-noneu.truecaller.com"
    }
    tresponse = requests.get(turl, headers=theaders, timeout=5)

    return tresponse

def search(auth,num):

    tresponse = truecaller_search(auth, num)

    if tresponse:
        restj = tresponse.json()
        trslt = json.dumps(restj)
        tjsonload = json.loads(trslt)
        if "name" in tjsonload['data'][0]:
            if tjsonload['data'][0]['internetAddresses']:
                pq = f"\n\n**----••Truecaller says----**\n\nName : `{tjsonload['data'][0]['name']}`\nCarrier : `{tjsonload['data'][0]['phones'][0]['carrier']}` \nE-mail : {tjsonload['data'][0]['internetAddresses'][0]['id']}"
                frbsetrname = tjsonload['data'][0]['name']
                frbsetrmail = tjsonload['data'][0]['internetAddresses'][0]['id']
            elif not tjsonload['data'][0]['internetAddresses']:
                pq = f"\n\n**----••Truecaller says----**\n\nName : `{tjsonload['data'][0]['name']}`\nCarrier : `{tjsonload['data'][0]['phones'][0]['carrier']}`"
                frbsetrname = tjsonload['data'][0]['name']
        else:
            pq = "\n\n**----••Truecaller says----**\n\nNo results found 🤦🏻‍♂️"
    if tresponse.status_code == 429:
        pq = "\n\n**----••Truecaller says----**\n\nLimit exceeded ,try again tomorrow 🤦🏻‍♂️"
    return pq