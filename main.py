import requests
import argparse
import re

parser = argparse.ArgumentParser(prog="MacFinder", description="A simple mac address vendor lookup.", )
parser.add_argument("-m", "--mac", help="str: mac address to lookup (i.e 00:11:22:33:44:55, 00-11-22-33-44-55, 001122334455)", required=True)

args = parser.parse_args()
regex_pattern = r'^([0-9A-Fa-f]{2}([-:])){5}[0-9A-Fa-f]{2}$|^([0-9A-Fa-f]{2}\.){5}[0-9A-Fa-f]{2}$|^[0-9A-Fa-f]{12}$|^([0-9A-Fa-f]{4}\.){2}[0-9A-Fa-f]{4}$'

def check_mac_format(mac):
    if not re.match(regex_pattern, mac):
        raise ValueError(f"invalid mac address: {mac}")

def main():
    # check for valid mac
    check_mac_format(args.mac)
    
    # try to connect, if not catch error
    try:
        r = requests.get(f"https://api.macvendors.com/{args.mac}")

        # check for anything above 400, if not, money
        if not r.ok:  
            print(f"error reaching server...\n{r} {r.reason}")
        else:
            print(f"device: {r.text}\nmac address: {args.mac}") # <------ money
    
    except requests.exceptions.ConnectionError:
        print("Error: No internet connection or unable to reach the server. Please check your connection and try again.")


if __name__ == "__main__":
    main()
    