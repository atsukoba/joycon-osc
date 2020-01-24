# joycon-osc

send osc (open sound control) by Nintendo Switch Joy-Con

## install

copy scripts of submodule and install python libraries.

```shell
cd joycon-osc
cp joycon-python/pyjoycon/* pyjoycon/
pip install -r requirements.txt
```

## run

![ss](https://i.gyazo.com/4b4d8029af39cf1be956aba14409d4d3.png)

After connecting Joy-Con via Bluetooth (`System Preferences` > `Bluetooth`), run this command.

```shell
python joycon-osc.py
```

then start sending osc message, values are taken from Joy-Con stick, buttons, gyroscope and battery property.

```text
sent osc message to /R/battery/charging : 0
sent osc message to /R/battery/level : 2
sent osc message to /R/buttons/right/y : 0
sent osc message to /R/buttons/right/x : 0
sent osc message to /R/buttons/right/b : 0
sent osc message to /R/buttons/right/a : 0
sent osc message to /R/buttons/right/sr : 0
sent osc message to /R/buttons/right/sl : 0
sent osc message to /R/buttons/right/r : 0
sent osc message to /R/buttons/right/zr : 0
sent osc message to /R/buttons/shared/minus : 0
sent osc message to /R/buttons/shared/plus : 0
sent osc message to /R/buttons/shared/r-stick : 0
sent osc message to /R/buttons/shared/l-stick : 0
sent osc message to /R/buttons/shared/home : 0
sent osc message to /R/buttons/shared/capture : 0
sent osc message to /R/buttons/shared/charging-grip : 0
sent osc message to /R/buttons/left/down : 0
sent osc message to /R/buttons/left/up : 0
sent osc message to /R/buttons/left/right : 0
sent osc message to /R/buttons/left/left : 0
sent osc message to /R/buttons/left/sr : 0
sent osc message to /R/buttons/left/sl : 0
sent osc message to /R/buttons/left/l : 0
sent osc message to /R/buttons/left/zl : 0
sent osc message to /R/analog-sticks/left/horizontal : 0
sent osc message to /R/analog-sticks/left/vertical : 0
sent osc message to /R/analog-sticks/right/horizontal : 2037
sent osc message to /R/analog-sticks/right/vertical : 1657
sent osc message to /R/accel/x : 8
sent osc message to /R/accel/y : 9
sent osc message to /R/accel/z : 67
sent osc message to /R/gyro/x : 33
sent osc message to /R/gyro/y : -27
sent osc message to /R/gyro/z : -39
```

## options

```shell
python joycon-osc.py --port 5005 --ip "127.0.0.1" --freq 0.1 --flush True
```

## environments

tested in the following environments

- macOS Catalina 10.15.2
- Python 3.6.8
- python-osc 1.7.0
