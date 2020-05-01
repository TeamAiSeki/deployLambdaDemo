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
        message = [
          {
            "type": "template",
            "altText": "this is a buttons template",
            "quickReply": {
              "items": [
                {
                  "type": "action",
                  "action": {
                    "type": "camera",
                    "label": "普通のCamera"
                  }
                }
              ]
            },
            "template": {
              "type": "buttons",
              "actions": [
                {
                  "type": "postback",
                  "label": "男",
                  "displayText": "男",
                  "data": "male"
                },
                {
                  "type": "postback",
                  "label": "女",
                  "displayText": "女",
                  "data": "female"
                },
                {
                  "type": "postback",
                  "label": "両方",
                  "displayText": "両方",
                  "data": "both"
                },
                {
                  "type": "uri",
                  "label": "(Debug)QRコードカメラ",
                  "uri": "https://line.me/R/nv/QRCodeReader"
                }
              ],
              "thumbnailImageUrl": "https://sho-d-blog.com/wp-content/uploads/2020/04/two_people_walking.jpg",
              "title": "あなたの恋愛対象",
              "text": "恋愛対象を教えて下さい",
            }
          }
        ]
    
        params = {
            "replyToken": message_dist["events"][0]["replyToken"],
            "messages": message
        }
        request = urllib.request.Request(url, json.dumps(params).encode("utf-8"), method=method, headers=headers)
        with urllib.request.urlopen(request) as res:
            body = res.read()
            
    return 0
