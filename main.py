#imports
import requests
import py_code.config as config
import py_code.database as database

#details of coin
def fetch_price(token_name):

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
            status = res.raise_for_status()
        except status == 400:
            print('(400, Bad Request)')
        except status == 401:
            print('(401, Unauthorized)')
        except status == 403:
            print('(403, Forbidden)')
        except status == 429:
            print('(429, Too many requests)')
        except status == 500:
            print('(500, Internal Server Error)')
        except status == 503:
            print('(503, Service Unavailable)')
        except status == 1020:
            print('(1020, Access Denied, violation of CDN firewaLL rule)')
        except status == 10002:
            print('(10005, Missing API Key)')
        except status == 10010:
            print('(10010, Invalid API Key, change from demo to pro)')
        except status == 1020:
            print('(10011, Invalid API Key, change from pro to demo)')
        except status == 10005:
            print('(10005, no access to endpoint, need upgrade for access)')
        else:
            state = True
   
    return res.json()

if __name__ == '__main__':
    database.init_db()
    token_name = input((str('please enter a valid token name: ')))
    results = fetch_price(token_name)
    print('fetched: ', results)
    database.save_to_db(results, token_name)