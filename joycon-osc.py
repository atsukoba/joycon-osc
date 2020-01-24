import atexit
import argparse
import random
import time
import sys
import hid
from pythonosc import udp_client
from pyjoycon import device
from pyjoycon.joycon import JoyCon


def dict_flatten(d, sep="/"):
    if not isinstance(d, dict):
        raise ValueError

    if not any(filter(lambda x: isinstance(x, dict), d.values())):
        return d

    dct = {}
    for key, value in d.items():
        if isinstance(value, dict):
            for k, v in dict_flatten(value, sep).items():
                dct[key + sep + k] = v
        else:
            dct[key] = value

    return dct


def check_device_status():
    print(hid.enumerate(0, 0))


def all_done():
    print('\n' * len(status) + "stopped osc sending")


if __name__ == "__main__":

    atexit.register(all_done)

    parser = argparse.ArgumentParser()
    parser.add_argument('--side', required=True, help="'L' or 'R'")
    parser.add_argument("--ip", default="127.0.0.1",
                        help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=5005,
                        help="The port the OSC server is listening on")
    parser.add_argument("--freq", type=float, default=0.1,
                        help="sleep time (seconds)")
    parser.add_argument("--verbose", type=bool, default=False,
                        help="osc log verbose")
    args = parser.parse_args()

    assert args.side in ["L", "R"], "option --side should be either 'R' or 'L'"

    print("Getting Joy-Con device info...")
    ids = device.get_ids(args.side)
    joycon = JoyCon(*ids) if None not in ids else None

    print(
        f"Building Open Sound Control Client, ip address={args.ip}, port={args.port}")
    client = udp_client.SimpleUDPClient(args.ip, args.port)

    print("Start Sending OSC ============================")
    while(True):
        if joycon is not None:
            status = dict_flatten(joycon.get_status())
            msg = ""
            for k, v in status.items():
                # ex) send osc message to ("buttons/right/x", 10)
                client.send_message("/" + k, v)
                msg += f"sent osc message to /{k} : {v}\n"
            if args.verbose:
              print(msg)
            else:
              print(f"{msg}\033[{len(status) + 1}A", end="")
        time.sleep(args.freq)
        print()


"""dictionary structure of Joy-Con Status data
{
  'battery': {
        'charging': 0,
        'level': 2
  }, 
  'buttons': {
    'right': {
        'y': 0,
        'x': 0,
        'b': 0,
        'a': 0,
        'sr': 0,
        'sl': 0,
        'r': 0,
        'zr': 0
    },
    'shared':{
        'minus': 0,
        'plus': 0,
        'r-stick': 0,
        'l-stick': 0,
        'home': 0,
        'capture': 0,
        'charging-grip': 0
    },
    'left': {
      'down': 0,
      'up': 0,
      'right': 0,
      'left': 0,
      'sr': 0,
      'sl': 0,
      'l': 0,
      'zl': 0
    }
  },
  'analog-sticks': {
    'left': {
      'horizontal': 0,
      'vertical': 0
    },
    'right': {
      'horizontal': 2170,
      'vertical': 1644
    }
  },
  'accel': {
    'x': 879,
    'y': 1272,d.keys()
    'z': 549
  },
  'gyro': {
    'x': -354,
    'y': -7,
    'z': 281
  }
}
"""
