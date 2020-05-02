import json
import urllib.request
import re
import os

def lambda_handler(event, context):
    url = "https://api.line.me/v2/bot/message/reply"
    method = "POST"
    headers = {
        'Authorization': 'Bearer ' + os.environ['CHANNEL_ACCESS_TOKEN'],
        'Content-Type': 'application/json'
    }
    message_dist = json.loads(event["body"])
    
    print(message_dist["events"])
    
    # 友達登録時
    if message_dist["events"][0]["type"] == "follow":
        json_open = open('json/Romance.json', 'r')

    elif message_dist["events"][0]["type"] == "postback":
        postback = message_dist["events"][0]["postback"]["data"] 
        if postback == "male" or postback == "female" or postback =="both":
            json_open = open('json/Height.json', 'r')

    else:
        json_open = open('json/error.json', 'r')

    json_load = json.load(json_open)
    params = {
        "replyToken": message_dist["events"][0]["replyToken"],
        "messages": [json_load]
    }
    request = urllib.request.Request(url, json.dumps(params).encode("utf-8"), method=method, headers=headers)
    with urllib.request.urlopen(request) as res:
        body = res.read()
        print(body)
            
    return 0
