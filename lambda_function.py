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
        json_open = open('Romance.json', 'r')
        json_load = json.load(json_open)
    
        params = {
            "replyToken": message_dist["events"][0]["replyToken"],
            "messages": [json_load]
        }
        request = urllib.request.Request(url, json.dumps(params).encode("utf-8"), method=method, headers=headers)
        with urllib.request.urlopen(request) as res:
            body = res.read()
            
    return 0
