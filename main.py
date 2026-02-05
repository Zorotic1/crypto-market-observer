#imports
import requests
import py_code.config as config
import py_code.database as database
import time


#details of coin
def fetch_price(token_names):
    
    #handles multiple tokens being requested
    if len(token_names) > 1:
        c = 0
        temp_token_names = str()
        while c != len(token_names):
            temp_token_names = temp_token_names + token_names[c] + ","
            c = c + 1
        temp_token_names = temp_token_names[:-1]
    else:
        temp_token_names = token_names
    
    print(temp_token_names)

    params = {
        'ids': temp_token_names,
        'vs_currency' : 'usd',
        'include_24hr_vol': True,
        'precision': 2,
        'price_change_percentage': '24h'
    }



    headers = {
        'x-cg-demo-api-key': config.COINGECKO_API_KEY
    }

    state = False

    while state != True:
        try:
            res = requests.get(config.API_URL, params=params, headers=headers)
            res.raise_for_status()
            state = True
            return res.json()
        except requests.exceptions.HTTPError as e:
            code = e.response.status_code
            if code == 429:
                print('(429, Too many requests)')
                time.sleep(60)
            elif code >= 500 or code == 400:
                print('Error Code: ', code, ', terminating.')
                break
            else:
                print('Error Code:', code)
                time.sleep(5)
        except res == None:
            return None
    return None

#main
if __name__ == '__main__':
    database.init_db()
    #token name input
    token_names = ['bitcoin', 'binancecoin', 'ethereum']
    token_names = sorted(token_names)
    for i in token_names:
        while i.isspace():
                print('token_name contains spaces, please edit before retrying')
                break
    results = dict()
    print('token_names', token_names)
    results = fetch_price(token_names)

    #retry if there are no results or error happened
    if results == None:
        choice = list('Y', 'N', "y", 'n')
        decision = None
        while decision not in choice:
            decision = str(input('retry? Y/N'))
            if decision == 'Y' or 'y':
                token_names = input((str('please enter a valid token name: ')))
                results = fetch_price(token_names)
            else:
                break
    database.save_to_db(results, token_names)