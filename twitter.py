#!/usr/bin/python

import sys, getopt, argparse, requests

headers = {
    'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:27.0) Gecko/20100101 Firefox/27.0',
    'Referer' : 'http://sportsbeta.ladbrokes.com/football',
}

def usage():
    print("usage: twitter.py [-u]")
    print("optional arguments:")
    print("\t-h, --help     show this help message and exit")
    print("\t-u, --url      url for tweet to tamper with")
    print("\t-v, --verbose  toggle verbose")

parser = argparse.ArgumentParser()
parser.add_argument("help")
parser.add_argument("u")
parser.add_argument("v")
args = parser.parse_args()

if args.help:
    usage()

elif args.u:
    url = True

elif args.v:
    verbose = True