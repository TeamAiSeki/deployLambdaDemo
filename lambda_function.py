"""後日、コード綺麗にします。ちょっと本業に想定の5倍くらい時間取られた"""
import json
import urllib.request
import re
import os
import re
import boto3
#各種機械学習モジュールのimport、使うなら
# import keras
# import numpy as np

dynamo_db = boto3.resource('dynamodb')
table= dynamo_db.Table('AIsekiya')

#User情報を引数に受け取り、診断結果を返す関数。オバソン記述予定。
def matching(user_id):
    #DBから相手先の情報を取得
    # partner_info = table.get_item(
    #     Key={
    #         'user_id': user_id
    #         }
    #     )
    
    #機械学習処理
    model_output = "96%"
    return model_output
 
def lambda_handler(event, context):
    read_flag = True
    url = "https://api.line.me/v2/bot/message/reply"
    method = "POST"
    headers = {
        'Authorization': 'Bearer ' + os.environ['DEV_CHANNEL_ACCESS_TOKEN'],
        'Content-Type': 'application/json'
    }
    message_dist = json.loads(event["body"])

    #UserIDを取得
    user_id = message_dist["events"][0]["source"]["userId"]
    #LineでのUser_IDは文字列を含むため、数値のみを抽出する。ちょっとこのままだと長すぎる。
    user_num = re.sub("\\D", "", user_id)

    # 友達登録時
    if message_dist["events"][0]["type"] == "follow":
        json_open = open('json/Height.json', 'r')

    elif message_dist["events"][0]["type"] == "postback":
        postback = message_dist["events"][0]["postback"]["data"] 
        postback_action = postback.split("&")[0].split("=")[1]
        if postback_action == "height":
            table.put_item(
                Item = {
                    "user_id" : user_num,
                    postback_action : postback.split("&")[1].split("=")[1]
                })
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
            # QRコードを生成しクエリパラメータとしてuser_idを与える、一旦正田氏のqrをそのまま利用する。
            # qr = qrcode.make('https://comingout.tokyo/1806'+ '/?user_id='+ user_id)
            # json_open = open('json/Aicode.json', 'r')
            json_load = {
                    "type": "text",
                    "text": "回答ありがとうございました。あなたのIDは" + user_num +  "です。"
                    }
            read_flag = False
            
    
    #ユーザーがBotに何らかを送信した場合
    elif message_dist["events"][0]["type"] == "message":
        # #ユーザーの画像送信をキャッチ
        if message_dist["events"][0]["message"]["type"] == "image":
            pass
        #ユーザーのID送信をキャッチ
        if re.match(r"^[0-9]{6}", message_dist["events"][0]["message"]["text"]) :
            try :
                json_load = {
                    "type": "text",
                    "text": "相性は"+ matching(user_id) + "です。すごーい"
                    }
                read_flag = False
            except :
                json_load = {
                    "type": "text",
                    "text": "相性診断に失敗しました。IDを確認してください。"
                    }
        else :
            json_open = open('json/Error.json', 'r')
    else:
        json_open = open('json/Error.json', 'r')

    if read_flag :
        json_load = json.load(json_open)

    params = {
        "replyToken": message_dist["events"][0]["replyToken"],
        "messages": [json_load]
    }
    request = urllib.request.Request(url, json.dumps(params).encode("utf-8"), method=method, headers=headers)
    with urllib.request.urlopen(request) as res:
        body = res.read()
        print("入力", body)
            
    return 0