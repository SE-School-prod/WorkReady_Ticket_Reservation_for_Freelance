"""
@file guild_id_dict.py
@date 2023/07/31(月)
@author 藤原光基
@brief DiscordのID関連
@details 処理に必要な各種ID,トークン情報をまとめた辞書型変数。
@note 「NOTION_TOKEN」、「DISCORD_TOKEN」について、変更時は逐次用変更。
@bar 編集日時 編集者 編集内容
@bar 2023/07/31(月) 藤原光基 新規作成
@bar 2023/09/18(月) 藤原光基 使用用途に応じてキー変更
"""

import os

settings_dict = {
    "DEBUG_FLG": False,
    "TOKEN": {
        "NOTION":
        #'secret_013tQKTmEmdOOWcBgcPBTKNN3wAOzgQhTSkN2t63M2U',
        os.environ['NOTION_TOKEN'],  # Notionのトークン
        "DISCORD":
        #'MTA5ODEwNDI1OTkyNjU3MzA3Ng.GV4SGN.VioIFVMRIsJ-PXlc45wecvdi-X2QPYSep-_e70',
        os.environ['DISCORD_TOKEN'],  # Discordのトークン
    },
    "GUILD_ID": {
        "GUILD": 1093886520324259920,  # DiscordのWorkReadyチャットグループID
        "BOT": 1098104259926573076,  # 「Discortion」BOTのメッセージID
        "CHANNEL_ID_DAILY_REPORT": 1098841750077968435,  # daily report
        "CHANNEL_ID_BOT_BOT": 1119239857751986227,  # bot_bot
        "CHANNEL_ID_BOT_TRAIN": 1098157558885273621,  # bot_train
        "CHANNEL_ID_BOT_RESERVE": 1149726805561974824,  # 相談会予約
        "CHANNEL_ID_DOC_COMPLETE": 1161660408457867345,  # Wiki読了報告
        "CHANNEL_ID_INIT_SETTING": 1116840784059183164,  # 初期設定
        "CHANNEL_ID_ENOROLLMENT_STATUS": 1165596826200711220, #ステータスチャンネル
        "CHANNEL_ID_CONSULTATION_SERVICE": 1175594169478160464, #相談会予約チャンネルver2
    },
    "DIR": {
        "LOG": {
            "ERROR": "log_error",  # ログ保存先(エラー)
            "INFO": "log_info",  # ログ保存先(各種処理実行内容)
            "SYS": "log_sys",  # ログ保存先(全部)
        },
        "LOG_SAVE_DIR": "notion_api_logs",  # ログ保存先
        "RESERVATION_CYCLE_FILE":
        os.path.join("settings", "reservation_cycle.txt")  # 相談会予約送信先
    },
    "CURRICULUM_NUMBER_RANGE": {
        "PROGATE": {
            "MIN": 1,
            "MAX": 20
        },
        "UDEMY": {
            "MIN": 21,
            "MAX": 326
        },
        "PORTOFOLIO": {
            "MIN": 327,
            "MAX": 335
        }
    },
    "CURRICULUM_GUIDELINE_DATE_RANGE": {
        "PROGATE": {
            "DATE_NUM": 14,
            "DESCRIPTION": "2週間",
            "PERCENTAGE": 5
        },
        "UDEMY": {
            "DATE_NUM": 42,
            "DESCRIPTION": "6週間",
            "PERCENTAGE": 45
        },
        "PORTOFOLIO": {
            "DATE_NUM": 56,
            "DESCRIPTION": "8週間",
            "PERCENTAGE": 50
        }
    },
    "AITEMASU_URL": {
        "0": {
            "name": "武藤みさき",
            "url": 'https://app.aitemasu.me/u/kakuiphone7/workreadyclass',
            "VC_NAME": '相談会-武藤',
        },
        "1": {
            "name": "林田翼",
            "url": 'https://app.aitemasu.me/u/tsubasa1121998/workreadyclass',
            "VC_NAME": '相談会-林田',
        },
        "2": {
            "name": "藤原光基",
            "url": 'https://app.aitemasu.me/u/ra0039ip/workreadyclass',
            "VC_NAME": '相談会-藤原',
        },
        "3": {
            "name": "菊池幸大",
            "url": 'https://app.aitemasu.me/u/koudai/workreadyclass',
            "VC_NAME": '相談会-菊池',
        },
        "4": {
            "name": "新家魁人",
            "url": 'https://app.aitemasu.me/u/kniinominodo/irupcurriculum',
            "VC_NAME": '相談会-新家',
        },
    }
}
