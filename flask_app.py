# coding: utf-8
'''
2SMPD-02Eでセンシングした情報をブラウザでグラフ化するサンプル

Raspberry PiにFlaskでWebサーバーを立ち上げて、
同じネットワーク内にあるPCやスマホから見れるようにする。
'''

from __future__ import print_function

import time
import datetime
from flask import Flask
from flask import render_template
from flask import jsonify

import grove_2smpb_02e

# オムロン公式ライブラリを使ってセンサーのインスタンス作成
sensor = grove_2smpb_02e.Grove2smpd02e()
# Flaskインスタンス作成
app = Flask(__name__)

# グラフ描画用のJSONデータのエンドポイント
@app.route('/sensor')
def cpu():
    press, temp = sensor.readData()
    # ダミーデータを返す
    return jsonify(temperature=1, pressure=1)
    # 実際のデータを返す
    # return jsonify(temperature=round(temp,2), pressure=round(press,2))

# ウェブページのエンドポイント
@app.route('/')
def home():
    # ブラウザのキャッシュ回避用にタイムスタンプを受け渡し
    s = datetime.datetime.now().strftime("%s")
    return render_template('index.html', timestamp=s)


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)


