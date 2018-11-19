#!/usr/bin/python
import sys, argparse, requests, threading

params = {'id': id, 'tweet_stat_count': '0'}

def main():
    # set up arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', metavar='url', nargs='+', required=True, help="URL to tweet to tamper with")
    parser.add_argument('-c', '--csrf', metavar='csrf', nargs='+', required=True, help="CSRF token to your twitter account")
    parser.add_argument('-C', '--cookie', metavar='cookie', nargs='+', required=True, help="Cookie to your twitter account")
    parser.add_argument('-v', '--verbose', required=False, dest='verbose')
    args = parser.parse_args()

    headers = {
        'authority': 'api.twitter.com',
        'method': 'POST',
        'path': '/1.1/favorites/destroy.json',
        'scheme': 'https',
        'accept': '*/*',
        'content-type':'application/x-www-form-urlencoded',
        'accept-Encoding': 'gzip, deflate, br',
        'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:27.0) Gecko/20100101 Firefox/27.0',
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAPYXBAAAAAAACLXUNDekMxqa8h%2F40K4moUkGsoc%3DTYfbDKbT3jJPCEVnMYqilB28NHfOPqkca3qaAxGfsyKCs0wRbw',
        'referer' : args.url[0],
        'cookie': args.cookie[0],
        'origin': 'https://twitter.com',
        'x-csrf-token': args.csrf[0],
        'x-twitter-active-user': 'yes',
        'x-twitter-auth-type': 'OAuth2Session'
    }

    # check for verbose option
    if args.verbose:
        verbose = True

    if args.url and args.csrf and args.cookie:
        # get ahold of twitter id
        url = args.url[0]
        id = url.split('/')[-1]

        # parameters and headers for request


        # send request
        #response = requests.post("https://api.twitter.com/1.1/favorites/create.json", params=params, headers=headers)
        #response = requests.post("https://api.twitter.com/1.1/favorites/destroy.json", params=params, headers=headers)
        #print(response)
        '''
        async def create():
            response = requests.post("https://api.twitter.com/1.1/favorites/create.json", params=params, headers=headers)
            print("CREATE: " + str(response))

        async def destroy():
            response = requests.post("https://api.twitter.com/1.1/favorites/destroy.json", params=params, headers=headers)
            print("DESTROY: " + str(response))

        loop = asyncio.get_event_loop()

        loop.run_until_complete(
            asyncio.gather(
                create(), destroy()
            )
        )
        print("exit")
        loop.close()
        '''
        #print(asyncio.run(create()))
        #print(asyncio.run(destroy()))

if __name__ == '__main__':
    main()