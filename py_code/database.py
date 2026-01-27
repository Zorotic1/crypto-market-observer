import sqlite3
import py_code.config as config

#database setup
def init_db():
    conn = sqlite3.connect(config.DB)
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS coins(id TEXT, usd DECIMAL, usd_vol_24hr DECIMAL, usd_change_24hr DECIMAL)')


#saving data to db
def save_to_db(data, token_name):
    conn = sqlite3.connect(config.DB)
    cur = conn.cursor()

    inner_data = data[token_name]

    usd = inner_data['usd']
    usd_vol_24hr = inner_data['usd_24h_vol']
    usd_24h_change = inner_data['usd_24h_change']

    data_save = (token_name, usd, usd_vol_24hr, usd_24h_change)

    cur.execute('INSERT INTO coins(id, usd, usd_vol_24hr, usd_change_24hr) VALUES (?, ?, ?, ?)', data_save)
