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

    # 友達登録時
    if message_dist["events"][0]["type"] == "follow":
        json_open = open('json/Height.json', 'r')

    elif message_dist["events"][0]["type"] == "postback":
        postback = message_dist["events"][0]["postback"]["data"] 
        postback_action = postback.split("&")[0].split("=")[1]
        if postback_action == "height":
            json_open = open('json/Style.json', 'r')
        if postback_action == "style":
            json_open = open('json/Age.json', 'r')
        if postback_action == "age":
            json_open = open('json/Subject.json', 'r')
        if postback_action == "subject":
            json_open = open('json/Club.json', 'r')
        if postback_action == "club":
            json_open = open('json/Job.json', 'r')
        if postback_action == "job":
            json_open = open('json/Alcohol.json', 'r')
        if postback_action == "alcohol":
            json_open = open('json/Smoke.json', 'r')
        if postback_action == "smoke":
            json_open = open('json/Fashion.json', 'r')
        if postback_action == "fashion":
            json_open = open('json/Social1.json', 'r')
        if postback_action == "social1":
            json_open = open('json/Social2.json', 'r')
        if postback_action == "social2":
            json_load = {
                    "type": "text",
                    "text": "回答ありがとうございました。あなたのIDは" + user_num +  "です。"
                    }
    
    #ユーザーがBotに何らかを送信した場合
    # elif message_dist["events"][0]["type"] == "message":
    #     # #ユーザーの画像送信をキャッチ
    #     if message_dist["events"][0]["message"]["type"] == "image":
    #         pass
    #     #ユーザーのID送信をキャッチ
    #     if re.match(r"^[0-9]{6}", message_dist["events"][0]["message"]["text"]) :
    #         try :
    #             json_load = {
    #                 "type": "text",
    #                 "text": "相性は"+ matching(user_id) + "です。すごーい"
    #                 }
    #             read_flag = False
    #         except :
    #             json_load = {
    #                 "type": "text",
    #                 "text": "相性診断に失敗しました。IDを確認してください。"
    #                 }
    #     else :
    #         json_open = open('json/Error.json', 'r')
    else:
        json_open = open('json/Error.json', 'r')

    params = {
        "replyToken": message_dist["events"][0]["replyToken"],
        "messages": [json_load]
    }
    request = urllib.request.Request(url, json.dumps(params).encode("utf-8"), method=method, headers=headers)
    with urllib.request.urlopen(request) as res:
        body = res.read()
        print("入力", body)
            
    return 0