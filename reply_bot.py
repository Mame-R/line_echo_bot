import os
import sys

from flask import Flask, request, abort

from linebot.v3 import WebhookHandler

from linebot.v3.webhooks import MessageEvent, TextMessageContent, UserSource
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi, TextMessage, ReplyMessageRequest
from linebot.v3.exceptions import InvalidSignatureError

channel_access_token = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
channel_secret = os.environ["LINE_CHANNEL_SECRET"]

if channel_access_token is None or channel_secret is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN and LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)

handler = WebhookHandler(channel_secret)
configuration = Configuration(access_token=channel_access_token)

app = Flask(__name__)


# LINEボットからのリクエストを受け取るエンドポイント
@app.route("/callback", methods=["POST"])
def callback():
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError as e:
        abort(400, e)

    return "OK"


import random
# import datetime


# # 　返信メッセージを生成する関数
# def generate_response(from_user, text):
#     res = [TextMessage(text=f"やあ、{from_user}さん")]
#     if "こん" == text[:2] or "こん" == text[1:4]:
#         res.append(TextMessage(text="こんちは"))
#     elif "おは" in text:
#         res.append(TextMessage(text="おはよーさん"))
#     elif "何時" in text or "なんじ" in text:
#         now = datetime.datetime.now()
#         res.append(TextMessage(text=f"今は{now.hour}時{now.minute}分ですよ"))
#     elif "ねむ" in text or "眠" in text:
#         res.append(TextMessage(text="耐えるんだ…"))
#     elif "サイコロ" in text or "さいころ" in text:
#         n = random.randrange(6)
#         res.append(TextMessage(text=f"サイコロを振りました。結果は{n+1}でした。"))
#     elif "ねむ" in text or "眠" in text:
#         res.append(TextMessage(text="耐えるんだ…"))
#
#     else:
#         msg_templates = ["ホゲホゲ", "そうねぇ", f"「{text}」って言ったね？"]
#         msg_num = len(msg_templates)  # メッセージの数
#         idx = random.randrange(msg_num)  # 0からmsg_num-1までの乱数を生成
#         res.append(TextMessage(text=msg_templates[idx]))
#     return res

# 　高めの国産車をおすすめする返信メッセージを生成する関数
def generate_response(from_user, text):
    res = [TextMessage(text=f"{from_user}さん、\n以下のようなお車はいかがでしょうか。")]
    if "大き"  in text or "でか" in text:
        res.append(TextMessage(text="・トヨタ アルファード/ヴェルファイア\n・トヨタ ノア/ヴォクシー\n・ホンダ　ステップワゴン\n・日産　セレナ\n"
                                    "・トヨタ ランドクルーザー300\n・トヨタ ランドクルーザー250\n・スバル フォレスター\n・マツダ　CX-80"
                                    "\n・トヨタ　ハイエース\n・日産　キャラバン"
                                    "\n・トヨタ タンドラ\n・三菱　トライトン"))

    elif "広" in text or "ミニバン" in text or "室内" in text or "空間" in text:
        res.append(TextMessage(text="・トヨタ アルファード/ヴェルファイア\n・トヨタ ノア/ヴォクシー\n・ホンダ　ステップワゴン\n・日産　セレナ"))
    elif "オフロード" in text or "駆" in text or "雪" in text or "SUV" in text:
        res.append(TextMessage(text="・トヨタ ランドクルーザー300\n・トヨタ ランドクルーザー250\n・スバル フォレスター\n・マツダ　CX-80"))
    elif "荷物" in text or "バン" in text or "載" in text:
        res.append(TextMessage(text="・トヨタ　ハイエース\n・日産　キャラバン"))
    elif "アメリカ" in text or "トラック" in text or "ピックアップ" in text:
        res.append(TextMessage(text="・トヨタ タンドラ\n・三菱　トライトン"))

    elif "速い" in text or "スポーツ" in text or "かっこいい" in text:
        res.append(TextMessage(text="・トヨタ GR86/スバル　BRZ\n・マツダ　ロードスター\n・スズキ　スイフトスポーツ\n・日産　フェアレディZ\n・ホンダ　シビック"))
    elif "ラグジュアリー" in text or "高級" in text or "贅沢" in text or "広" in text:
        res.append(TextMessage(text="・トヨタ クラウン\n・レクサス　LS, ES, LM, LX\n・トヨタ　アルファード\n・トヨタ　ハリアー"))
    elif "コンパクト" in text or "使いやす" in text or "乗りやす" in text or "日常" in text or "足" in text or "街乗り" in text or "初心者" in text:
        res.append(TextMessage(text="・トヨタ ヤリス/ヤリスクロス\n・ホンダ　フィット\n・ホンダ　ヴェゼル\n・マツダ　MAZDA 2\n・日産　ノート\n・トヨタ　アクア\n・レクサス　LBX"))
    elif "シンプル" in text or "安定感" in text or "運転しやす" in text or "コスパ" in text or "社用" in text or "営業" in text or "セダン" in text:
        res.append(TextMessage(text="・トヨタ カローラ シリーズ\n・ホンダ　アコード\n・マツダ　MAZDA 3"))
    # elif "軽" in text:
    #     res.append(TextMessage(text="・ダイハツ　タント\n・ホンダ　NBOX\n・三菱　デリカミニ\n"
    #                                 "・ホンダ N-BOX\n・日産　サクラ\n・スズキ　ラパン"))
    elif "軽" in text and "たくさん" in text or "広" in text:
        res.append(TextMessage(text="・ダイハツ　タント\n・ホンダ　NBOX"))
    elif "軽" in text and "アウトドア" in text or "4駆" in text or "雪" in text:
        res.append(TextMessage(text="・三菱　デリカミニ\nはいかがでしょうか。"))
    elif "軽" in text and "おしゃれ" in text or "スマート" in text or "デザイン" in text or "かわいい" in text or "可愛い" in text:
        res.append(TextMessage(text="・ホンダ N-BOX\n・日産　サクラ\n・スズキ　ラパン"))


    elif "電気" in text or "BEV" in text or "電動" in text or "バッテリー" in text:
        res.append(TextMessage(text="・日産　リーフ\n・日産　サクラ\n・トヨタ　BZ4X\n・レクサス　RZ"))
    elif "水素" in text or "環境" in text or "燃料電池" in text or "FCEV" in text:
        res.append(TextMessage(text="・トヨタ　ミライ"))
    elif "安" in text or "学生" in text or "小" in text:
        res.append(TextMessage(text="・スズキ　アルト"
                                    "\n\n予算が限られている場合は中古車もお勧めです。最近ではセダンの中古価格が下がりがちですが、排気量が大きなモデルはその後の税金が高くなります。"
                                    "車検の時期や劣化具合に加えてそのあたりも考慮することをお勧めします"))
    elif "ハイブリッド" in text or "燃費" in text or "経済的" in text or "距離" in text or "HEV" in text:
        res.append(TextMessage(text="ハイブリッド車、おすすめです！\n・トヨタ　プリウス\n・日産　ノート/オーラ\n・トヨタ　アクア\n\n等が有名ですが、"
                                    "各社ラインナップが豊富ですので、ご自身のお好みのお車に設定があるかご確認いただくのもよいかもしれません。"))

    elif "トヨタ" in text or "TOYOTA" in text:
        res.append(TextMessage(text="トヨタ自動車のラインナップはこちらからご覧いただけます▽\nhttps://toyota.jp/carlineup/"))
    elif "日産" in text or "Nissan" in text or "ニッサン" in text:
        res.append(TextMessage(text="日産自動車のラインナップはこちらからご覧いただけます▽\nhttps://www.nissan.co.jp/CARLINEUP/"))
    elif "ホンダ" in text or "Honda" in text or "本田技研" in text:
        res.append(TextMessage(text="Hondaのラインナップはこちらからご覧いただけます▽\nhttps://www.honda.co.jp/auto-lineup/"))
    elif "マツダ" in text or "Mazda" in text:
        res.append(TextMessage(text="マツダのラインナップはこちらからご覧いただけます▽\nhttps://www.mazda.co.jp/cars/"))
    elif "スバル" in text or "SUBARU" in text:
        res.append(TextMessage(text="スバルのラインナップはこちらからご覧いただけます▽\nhttps://www.subaru.jp/carlineup/"))
    elif "ダイハツ" in text or "Daihatsu" in text:
        res.append(TextMessage(text="ダイハツ工業のラインナップはこちらからご覧いただけます▽\nhttps://www.daihatsu.co.jp/lineup/"))
    elif "レクサス" in text or "Lexus" in text:
        res.append(TextMessage(text="レクサスのラインナップはこちらからご覧いただけます▽\nhttps://lexus.jp/models/"))
    elif "スズキ" in text or "Suzuki" in text:
        res.append(TextMessage(text="スズキのラインナップはこちらからご覧いただけます▽\nhttps://www.suzuki.co.jp/car/lineup/"))
    elif "三菱" in text or "Mitsubishi" in text:
        res.append(TextMessage(text="三菱自動車の車種ラインナップはこちらからご覧いただけます▽\nhttps://www.mitsubishi-motors.co.jp/lineup/"))

    elif "サイコロ" in text or "さいころ" in text:
        n = random.randrange(6)
        res.append(TextMessage(text=f"サイコロを振りました。結果は{n+1}でした。"))
    # else:
    #     msg_templates = ["ちょっと何言ってるかわからない", "そうねぇ", f"「{text}」って言ったね？"]
    #     msg_num = len(msg_templates)  # メッセージの数
    #     idx = random.randrange(msg_num)  # 0からmsg_num-1までの乱数を生成
    #     res.append(TextMessage(text=msg_templates[idx]))
    return res

# メッセージを受け取った時の処理
@handler.add(MessageEvent, message=TextMessageContent)
def handle_text_message(event):
    # 送られてきたメッセージを取得
    text = event.message.text

    # 返信メッセージの送信
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)

        res = []
        if isinstance(event.source, UserSource):
            # ユーザー情報が取得できた場合
            profile = line_bot_api.get_profile(event.source.user_id)
            # 返信メッセージを生成
            res = generate_response(profile.display_name, text)

        else:
            # ユーザー情報が取得できなかった場合
            # fmt: off
            # 定型文の返信メッセージ
            res = [
                TextMessage(text="ユーザー情報を取得できませんでした。"),
                TextMessage(text=f"メッセージ：{text}")
            ]
            # fmt: on

        # メッセージを送信
        line_bot_api.reply_message_with_http_info(ReplyMessageRequest(reply_token=event.reply_token, messages=res))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
