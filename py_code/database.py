import psycopg2
import py_code.config as config
from psycopg2 import sql
import re

#connect to sql database
def get_connection():
    return psycopg2.connect(
        host=config.DB_HOST,
        user=config.DB_USER,
        password=config.DB_PASS,
        dbname=config.DB_NAME
    )

#database setup
#def init_db():
    #conn = get_connection()
    #cur = conn.cursor()
    #cur.execute('CREATE TABLE IF NOT EXISTS coins(id TEXT, usd NUMERIC, market_cap_change_percentage_24hr NUMERIC, usd_percentage_change_24hr NUMERIC)')
    #conn.commit()


#saving data to db
def save_to_db(data, token_name):
    conn = get_connection()
    cur = conn.cursor()

    inner_data = list()
    count = 0

    #loop to read all coins in list
    for i in data:
        
        inner_data.append(data[count])
        print ('coin ', count)
        #extracts invdividual column in dict stored in list
        tmp_data = inner_data[count]
        timestamp = None
        usd = None
        market_cap_change_percentage_24hr = None
        usd_24h_change = None
        coin_name = re.sub('[!@#$]''', '', (str(token_name[count])))
        
        try:
            timestamp = tmp_data['last_updated']
            usd = tmp_data['current_price']
            market_cap_change_percentage_24hr = tmp_data['market_cap_change_percentage_24h']
            usd_24h_change = tmp_data['price_change_percentage_24h']
            #saves data into db
            data_save = (timestamp, usd, market_cap_change_percentage_24hr, usd_24h_change)
            create_db = sql.SQL('CREATE TABLE IF NOT EXISTS {}(id SERIAL PRIMARY KEY, timestamp TEXT, usd NUMERIC, market_cap_change_percentage_24hr NUMERIC, usd_percentage_change_24hr NUMERIC)').format(sql.Identifier(coin_name))
            cur.execute(create_db)
            insert_db = sql.SQL('INSERT INTO {}(timestamp, usd, market_cap_change_percentage_24hr, usd_percentage_change_24hr) VALUES (%s, %s, %s, %s)').format(sql.Identifier((coin_name)))
            cur.execute(insert_db, data_save)
        except KeyError:
            print(f"missing data: USD: {usd}, timestamp: {timestamp}, USD_VOL_24hr: {market_cap_change_percentage_24hr}, USD_24h_change: {usd_24h_change}")
        
        #moves to the next coin
        count = count + 1
    conn.commit()


    