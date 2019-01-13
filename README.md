# robosys2018 ROS課題 

[ロボットシステム学2018第13回](https://github.com/ryuichiueda/robosys2018/blob/master/13.md)の内容より  
  
キーボード入力によってLEDを点灯させる．入力したキーはブラウザにて確認できる．


### 動作環境

|||
|:--:|:--:|
| Raspberry Pi | Raspberry Pi Model 3B+ |
| OS | Ubuntu16.04 |
| kernel | Linux ubuntu 4.14.58-v7+ |
| ROS | ROS kinetic |

### 実行方法

```
$ git clone https://github.com/KentaKawamata/robosys2018_usingROS.git
$ cd LED
$ roslaunch LED LED.launch
```
1を入力することで赤色のLED，2を入力することで青色のLEDを点灯させる．  
その他のキーボード入力で全てのLEDを消灯させる．

#### ブラウザで入力キーを確認する方法．

ブラウザにて`http://<Raspberry PiのIPアドレス>:8000`と入力.

### 必要ライブラリ

- ros-kinetic-rosbridge-suite

# デモ動画 

