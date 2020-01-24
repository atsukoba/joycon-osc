import argparse
import random
import time
import sys
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


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1",
                        help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=5005,
                        help="The port the OSC server is listening on")
    parser.add_argument("--freq", type=float, default=0.1,
                        help="sleep time (seconds)")
    parser.add_argument("--flush", type=bool, default=True,
                        help="osc log flush or not")
    args = parser.parse_args()

    print("Getting Joy-Con device info...")
    ids = device.get_device_ids()
    R_JOYCON = JoyCon(ids["R"]["vendor"], ids["R"]["product"]) if None not in ids["R"].values() else None
    L_JOYCON = JoyCon(ids["L"]["vendor"], ids["L"]["product"]) if None not in ids["L"].values() else None

    print(
        f"Building Open Sound Control Client, ip address={args.ip}, port={args.port}")
    client = udp_client.SimpleUDPClient(args.ip, args.port)

    while(True):
        if R_JOYCON is not None:
            status_r = R_JOYCON.get_status()
            msg = ""
            for k, v in dict_flatten(status_r).items():
                # ex) send osc message to ("buttons/right/x", 10)
                client.send_message("/R/" + k, v)
                msg += f"sent osc message to {'/R/' + k} : {v}\n"
            print(msg)
            if args.flush: sys.stdout.flush()

        if L_JOYCON is not None:
            status_l = L_JOYCON.get_status()
            msg = ""
            for k, v in dict_flatten(status_l).items():
                # ex) send osc message to ("buttons/right/x", 10)
                client.send_message("/L/" + k, v)
                msg += f"sent osc message to {'/L/' + k} : {v}\n"
            print(msg)
            if args.flush: sys.stdout.flush()

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
