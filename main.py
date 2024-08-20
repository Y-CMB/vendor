import requests
import argparse

parser = argparse.ArgumentParser(prog="MacFinder.py", description="A simple mac address vendor lookup.")
parser.add_argument("-m", help="str: mac address to lookup (i.e '00:11:22:33:44:55', '00-11-22-33-44-55', '001122334455')")

args = parser.parse_args()

r = requests.get(f"https://api.macvendors.com/{args.m}")

if 200 not in r:
    print(f"Error reaching server...{r.reason}")
else:
    print(f"Device: {r.text}\nMac: {args.m}")