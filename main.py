#imports
import requests
import py_code.config as config
import py_code.database as database
import time


#details of coin
def fetch_price(token_name):

#for searching by name, implement later, use .replace() instead.
    #while " " in token_name:
        #temp_name = ""
        #c = 0
        #for i in token_name:
            #if i == " ":
                #temp_name = temp_name + ('%20')
            #else:
                #temp_name = temp_name + i
            #c = c + 1
            #if c == len(token_name):
                #token_name = temp_name
                #break


    params = {
        'ids': token_name,
        'vs_currencies' : 'usd',
        'include_24hr_vol': True,
        'include_24hr_change': True
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
    token_name = input((str('please enter a valid token name: ')))
    while token_name.isspace():
            token_name = input((str('please enter a valid token name: ')))

    results = fetch_price(token_name)

    #retry if there are no results or error happened
    if results == None:
        choice = list('Y', 'N', "y", 'n')
        decision = None
        while decision not in choice:
            decision = str(input('retry? Y/N'))
            if decision == 'Y' or 'y':
                token_name = input((str('please enter a valid token name: ')))
                results = fetch_price(token_name)
            else:
                break
    
    print('fetched: ', results)
    database.save_to_db(results, token_name)