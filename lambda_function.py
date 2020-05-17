import json
import urllib.request
import re
import os
import re
# import boto3
 
def lambda_handler(event, context):
    url = "https://api.line.me/v2/bot/message/reply"
    method = "POST"
    headers = {
        'Authorization': 'Bearer ' + os.environ['DEV_CHANNEL_ACCESS_TOKEN'],
        'Content-Type': 'application/json'
    }
    message_dist = json.loads(event["body"])
    
    print(message_dist["events"])
    
    if not message_dist["events"][0]["type"] == "unfollow":
        # 友達登録時
        if message_dist["events"][0]["type"] == "follow":
            json_open = open('json/Age.json', 'r')

        elif message_dist["events"][0]["type"] == "postback":
            postback = message_dist["events"][0]["postback"]["data"] 
            postback_action = postback.split("&")[0].split("=")[1]
            # DB保存用
            # postback_value = postback.split("&")[1].split("=")[1]
            if postback_action == "age":
                json_open = open('json/Subject.json', 'r')
            if postback_action == "subject":
                json_open = open('json/Happy.json', 'r')
            if postback_action == "happy":
                json_open = open('json/Job.json', 'r')
            if postback_action == "job":
                json_open = open('json/Height.json', 'r')
            if postback_action == "height":
                json_open = open('json/Want.json', 'r')
            if postback_action == "want":
                json_open = open('json/Style.json', 'r')
            if postback_action == "style":
                json_open = open('json/Social1.json', 'r')
            if postback_action == "social1":
                json_open = open('json/Social3.json', 'r')
            if postback_action == "social3":
                json_open = open('json/Social2.json', 'r')
            if postback_action == "social2":
                json_open = open('json/Social4.json', 'r')
            if postback_action == "social4":
                json_open = open('json/Aicode.json', 'r')

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
            # print(body)
            
    return 0