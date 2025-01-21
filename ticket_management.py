from notion import Notion

class TicketManagement():
    
    def __init__(self, database_id, user_id):
        self.database_id = database_id
        self.user_id = user_id
        self.ticket_free = 0
        self.ticket_30 = 0
        self.ticket_60 = 0

    #チケットの枚数を取得するメソッド
    def get_ticket_num(self):

        notion = Notion()
        filter_dict = {'ユーザーID': self.user_id}
        results_id = notion.select(self.database_id, filter_dict)

        if len(results_id) == 1:
            if results_id[0]["properties"]["30分無料相談チケット"]["number"] is None:
                self.ticket_free = 0
            else:
                self.ticket_free = results_id[0]["properties"]["30分無料相談チケット"]["number"]
            
            if results_id[0]["properties"]["30分有料相談チケット"]["number"] is None:
                self.ticket_30 = 0
            else:
                self.ticket_30 = results_id[0]["properties"]["30分有料相談チケット"]["number"]

            if results_id[0]["properties"]["60分有料相談チケット"]["number"] is None:
                self.ticket_60 = 0
            else:
                self.ticket_60 = results_id[0]["properties"]["60分有料相談チケット"]["number"]

        elif len(results_id) == 0:
            reply = f'ignore\n'\
                    f"該当するユーザが見つかりませんでした。"
            print(reply)
        else:
            reply = f'ignore\n'\
                    f"該当するユーザが複数人いるため特定できませんでした。"
            print(reply)