import json
import os
import stripe
from notion import Notion
from flask import Flask, jsonify, request
from settings.database_id_list import database_id_list
from ticket_management import TicketManagement
import logging

# filename="test.log"を　追加
logging.basicConfig(level=logging.INFO,
format="%(asctime)s - %(levelname)s:%(name)s - %(message)s",
filename="webhook.log")

#テスト用
#stripe.api_key = "sk_test_51Mxrz4KYm8ieM9T1SGirOWKVyXI3rSWMg2DRA2awhcpIRymuBzES0lxMMFXb6JMiCFVggJhDgfMBYbju4fNDUKuw006DHg1xH4"
#endpoint_secret = 'whsec_8HOEGb1vtDPpgKQthoM0dlVwXDgPr4vM'

#本番用
stripe.api_key = os.environ['STRIPE_SEC_KEY']
endpoint_secret = os.environ['WEBHOOK_SEC_KEY']

app = Flask(__name__)

@app.route('/webhook/endpoint', methods=['POST'])
def webhook():
    event = None
    payload = request.get_data()

    try:
        event = json.loads(payload)
    except json.decoder.JSONDecodeError as e:
        logging.error('⚠️  基本的なリクエストの解析中に Webhook エラーが発生しました。' + str(e))
        print('⚠️  基本的なリクエストの解析中に Webhook エラーが発生しました。' + str(e))
        return jsonify(success=False)

    if endpoint_secret:
        sig_header = request.headers.get('stripe-signature')
        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, endpoint_secret
            )
        except stripe.error.SignatureVerificationError as e:
            logging.error('⚠️  Webhook 署名の検証に失敗しました。' + str(e))
            print('⚠️  Webhook 署名の検証に失敗しました。' + str(e))
            return jsonify(success=False)

    # イベントのタイプ別処理
    if event['type'] == 'checkout.session.completed':
      payment_link = event['data']['object']['payment_link']
      
      #試験用
      #link_30 = 'plink_1OnWs6KYm8ieM9T1xjPWt7WX'
      #link_60 = 'plink_1OnX5cKYm8ieM9T11dTHXg3M'
      #本番用
      link_30 = 'plink_1OmCWaKYm8ieM9T1J4J5SjTB'
      link_60 = 'plink_1OmCa3KYm8ieM9T1uoc8dnDi'

      #購入した商品が有料チケットの場合
      if payment_link == link_30 or payment_link == link_60:
            try:
              user_id = event['data']['object']['custom_fields'][0]['numeric']['value']
              agent_no = event['data']['object']['custom_fields'][1]['numeric']['value']
              logging.info(f'ユーザid: {user_id}')
              logging.info(f'エージェント番号: {agent_no}')

              if(agent_no in database_id_list) == True:
                  database_id = database_id_list[agent_no]
                  #チケットマネジメントクラスのインスタンス作成
                  ticket_manager = TicketManagement(database_id, user_id)
                  #現在の枚数確認
                  ticket_manager.get_ticket_num()
                    
                  #30分有料チケットを購入した場合
                  if payment_link == link_30:
                      print('30分有料')
                      #単価
                      price = 3000
                      #購入枚数確認
                      ticket_num = int(int(event['data']['object']['amount_total'])/price)

                      #更新処理
                      notion = Notion()
                      filter_dict = {'ユーザーID': user_id}
                      results_id = notion.select(database_id, filter_dict)
                      if len(results_id) == 1:
                          # 取得先のIDを取得する
                          page_id = results_id[0]["id"]
                          filter_dicts_list = [
                              {'30分有料相談チケット': ticket_manager.ticket_30 + ticket_num}
                          ]
                          notion.update(page_id=page_id, filter_dicts_list=filter_dicts_list)
                      else:
                          logging.error('DB上のユーザの特定に失敗しました。')
                          print('DB上のユーザの特定に失敗しました。')
                          return jsonify(success=False)
                  #60分有料チケットを購入した場合
                  elif payment_link == link_60:
                        print('60分有料')
                        #単価
                        price = 5000
                        #購入枚数確認
                        ticket_num = int(int(event['data']['object']['amount_total'])/price)
                            
                        #更新処理
                        notion = Notion()
                        filter_dict = {'ユーザーID': user_id}
                        results_id = notion.select(database_id, filter_dict)
                        if len(results_id) == 1:
                            # 取得先のIDを取得する
                            page_id = results_id[0]["id"]
                            filter_dicts_list = [
                                {'60分有料相談チケット': ticket_manager.ticket_60 + ticket_num}
                            ]
                            notion.update(page_id=page_id, filter_dicts_list=filter_dicts_list)
                        else:
                            logging.error('DB上のユーザの特定に失敗しました。')
                            print('DB上のユーザの特定に失敗しました。')
                            return jsonify(success=False)
              else:
                #エージェント番号が間違っていることを伝える画面に遷移する
                logging.error('エージェント番号が間違っています。')
                print('エージェント番号が間違っています。')
                return jsonify(success=False)
            except Exception as e:
                logging.error('⚠️  チケット別処理においてエラーが発生しました。' + str(e))
                print('⚠️  チケット別処理においてエラーが発生しました。' + str(e))

          
      #購入した商品がそれ以外の場合
      else:
          logging.info("その他商品です。")
          print("その他商品です。")

    else:
      logging.info(f'処理しないタイプのイベントです。 {event["type"]}')
      print(f'処理しないタイプのイベントです。 {event["type"]}')

    logging.info('チケット購入時のウェブフック処理が正常終了しました。')
    return jsonify(success=True)

#試験用
@app.route("/test")
def test():
   logging.info('テストページの表示')
   return "<p>テストページテスト</p>"


if __name__ == "__main__":
   app.run(debug=True, host="0.0.0.0", port=os.getenv("PORT", default=5000))

