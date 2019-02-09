# 2smpb02e-with-isaax

[オムロン絶対圧センサ**2SMPB-02E**を搭載した評価用モジュール\(Groveコネクタ付き\)](https://www.switch-science.com/catalog/5329/)をRaspberry Pi+isaaxで動かすためのサンプルコードです。

ハンズオンを行うには[Isaax Camp](https://camp.isaax.io/ja/examples/2smpb-02e-raspberry-pi)の記事をご確認ください。

センサの仕様については以下のドキュメントをご確認ください。

* [英語](./README_en.md)
* [日本語](./README_ja.md)

## Dependency

* Raspberry Pi 3B/3B+
* Python 3.6 or higher
* GrovePi+

### Configure Software

Setup GrovePi+

```bash
$ sudo curl -kL dexterindustries.com/update_grovepi | bash
$ sudo raspi-config
Enable I2C and SPI
$ sudo reboot
```

Insatll Python Modules

```bash
pip3 install matplotlib
pip3 install smbus2
pip3 install git+https://github.com/AmbientDataInc/ambient-python-lib.git
```
