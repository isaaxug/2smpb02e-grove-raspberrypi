# coding: utf-8
'''
2SMPD-02EでセンシングしたデータをAmbientで可視化するサンプル
'''

from __future__ import print_function

import os
import time
import datetime

import ambient
import grove_2smpb_02e

# ambient instance
try:
    # 環境変数からAmbient接続に必要な変数を取得
    AMBIENT_CHANNEL_ID = int(os.environ['AMBIENT_CHANNEL_ID'])
    AMBIENT_WRITE_KEY = os.environ['AMBIENT_WRITE_KEY']
    am = ambient.Ambient(AMBIENT_CHANNEL_ID, AMBIENT_WRITE_KEY)
except KeyError:
    print(KeyError)
    exit(1)

# sensor instance
sensor = grove_2smpb_02e.Grove2smpd02e()

def main():
    
    print ("start")
    
    while True:
        press, temp = sensor.readData()
        now = datetime.datetime.today()
        # Ambientに送信するデータの作成
        payload = {
          "d1": press,
          "d2": temp,
          "created": now.strftime("%Y/%m/%d %H:%M:%S")
        }
        try:
          # 送信
          am.send(payload)
        except Exception as e:
          print(e)

        # API制限にかからないように十分な間隔を空ける
        time.sleep(10)

if __name__ == '__main__':
    main()
