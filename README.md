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
python joycon-osc.py --side R
```

then start sending osc message, values are taken from Joy-Con stick, buttons, gyroscope and battery property.

```text
sent osc message to /battery/charging : 0
sent osc message to /battery/level : 2
sent osc message to /buttons/right/y : 0
sent osc message to /buttons/right/x : 0
sent osc message to /buttons/right/b : 0
sent osc message to /buttons/right/a : 0
sent osc message to /buttons/right/sr : 0
sent osc message to /buttons/right/sl : 0
sent osc message to /buttons/right/r : 0
sent osc message to /buttons/right/zr : 0
sent osc message to /buttons/shared/minus : 0
sent osc message to /buttons/shared/plus : 0
sent osc message to /buttons/shared/r-stick : 0
sent osc message to /buttons/shared/l-stick : 0
sent osc message to /buttons/shared/home : 0
sent osc message to /buttons/shared/capture : 0
sent osc message to /buttons/shared/charging-grip : 0
sent osc message to /buttons/left/down : 0
sent osc message to /buttons/left/up : 0
sent osc message to /buttons/left/right : 0
sent osc message to /buttons/left/left : 0
sent osc message to /buttons/left/sr : 0
sent osc message to /buttons/left/sl : 0
sent osc message to /buttons/left/l : 0
sent osc message to /buttons/left/zl : 0
sent osc message to /analog-sticks/left/horizontal : 0
sent osc message to /analog-sticks/left/vertical : 0
sent osc message to /analog-sticks/right/horizontal : 2037
sent osc message to /analog-sticks/right/vertical : 1657
sent osc message to /accel/x : 8
sent osc message to /accel/y : 9
sent osc message to /accel/z : 67
sent osc message to /gyro/x : 33
sent osc message to /gyro/y : -27
sent osc message to /gyro/z : -39
```

## options

```shell
optional arguments:
  -h, --help         show this help message and exit
  --side SIDE        'L' or 'R'
  --ip IP            The ip of the OSC server
  --port PORT        The port the OSC server is listening on
  --freq FREQ        sleep time (seconds)
  --verbose VERBOSE  osc log verbose
```

## environments

tested in the following environments

- macOS Catalina 10.15.2
- Python 3.6.8
- python-osc 1.7.0
