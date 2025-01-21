"""
@file database_id_list.py
@date 2023/07/31(月)
@author 藤原光基
@brief 進捗登録先ID集
@details 進捗登録先のIDについてまとめた辞書型変数。
@note ID参照方法・・・
@note 1.notionの一般代理店様ページに飛ぶ
@note 2.「...」から「Copy link to View」をクリックする
@note 3.コピーしたリンクから下記を抽出する
@note   https://www.notion.so/[database_id](ここ！！))?v=[view_id]&...
@note
@note 参考URL
@note https://stackoverflow.com/questions/73045760/how-do-i-find-the-database-id-of-an-inline-notion-database
@bar 編集日時 編集者 編集内容
@bar 2023/07/31(月) 藤原光基 新規作成
@bar 2023/08/20(日) 藤原光基 00006(D-GATE様)追加
@bar 2023/09/08(金) 藤原光基 00007(UooD株式会社様)追加
@bar 2023/09/19(火) 藤原光基 00008(合同会社Trust me様)追加
@bar 2023/09/18(月) 藤原光基 00008(Trust me様)追加
@bar 2023/09/21(木) 藤原光基 00009(CHEER ONE様)追加
@bar 2023/09/25(月) 藤原光基 99999(Test DB)追加
@bar 2023/10/20(金) 藤原光基 00010(北岡謙信様)追加
@bar 2023/10/20(金) 藤原光基 00011(株式会社リンクシア様)追加
@bar 2023/10/20(金) 藤原光基 00012(株式会社エスフリー様)追加
@bar 2023/11/14(火) 藤原光基 00013(株式会社ピロリズム様)追加
@bar 2023/11/14(火) 藤原光基 00014(株式会社Leaps様)追加
@bar 2023/11/16(木) 藤原光基 00015(佐土原奨様)追加
"""

database_id_list = {
    "00000": "0ad4e40097ae4ed589e454bef7cc1109",  # iConnect様
    "00001": "2decda34fa914958a61bd5e23842b29b",  # PMエージェント様
    "00002": "ab61771e3931426eadcbf8e363d3d3d8",  # 板尾大輔様
    "00003": "3dedcc2dc7e949218aa81eed568692dc",  # 黒木彩名様
    "00004": "fa5c4f1947fe430096d52dd99be4230e",  # 株式会社リード様
    "00005": "f2cb4ada0b4c4bde818398f94eabbf0d",  # 丹内光太郎様
    "00006": "61a2a6136ad64c87a8f46efed5988ba9",  # D-GATE様
    "00007": "1f201e1363cc4be2a0fe2fffb323ab5b",  # UooD株式会社様
    "00008": "67b1cdbdbbae4d23bbe8b8d962629981",  # 合同会社Trust me様
    "00009": "aac18bb3dc6e435b9351c3ab70f48074",  # 株式会社CHEER ONE様
    "00010": "ccbf0a53c80543d096550dd7f649d04c",  # 北岡謙信様
    "00011": "53934568499842be8ed1648071cd81b9",  # 株式会社リンクシア様
    "00012": "d1c3d850e76d49b69ece74e146219529",  # 株式会社エスフリー様
    "00013": "770d141a57ff4dbaa03baf226ef2df45",  # 株式会社ピロリズム様 
    "00014": "ac9f939f2fee4cd3bc12a3431e6ddca9",  # 株式会社Leaps様
    "00015": "8120cb36695a469a850ad737e4523ecf",  # 佐土原奨様
    "99999": "bee6832fb35c4c2c8ac829b3338c5a96",  # テストDB(共有)
    # "test": "0235ca24d99a4fb49f0b1a30d54601f8", # テストDB(メール送信)
}

