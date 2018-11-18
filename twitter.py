#!/usr/bin/python

import sys, getopt, argparse, requests

headers = {
    'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:27.0) Gecko/20100101 Firefox/27.0',
    'Referer' : 'http://sportsbeta.ladbrokes.com/football',
}

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", required=True, help="URL to tweet to tamper with", action="store_true")
    parser.add_argument("-v", "--verbose", required=False, dest="verbose")
    args = parser.parse_args()

    if args.verbose:
        verbose = True

if __name__ == '__main__':
    Main()