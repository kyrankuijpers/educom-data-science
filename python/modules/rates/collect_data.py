import duckdb, sys
from datetime import datetime as dt
import rates.exchange_rate, rates.api, rates.currency

def is_file_locked(path):
    try:
        with open(path, 'a'):
            return False
    except IOError:
        return True

def save_rates_from_api(con):
    
    ##### GET DATA FROM API 
    data = rates.api.get_rates_from_api()

    ##### RESTRUCTURE DATA 
    if data:
        
        rate_rows = []
        
        timestamp = data['timestamp']
        date = data['date']
        
        base_code = data['base']
        base_info = rates.currency.get_currency_by_code(con, 'EUR')  
        base_id = base_info['id']  
        
        for code, rate in data['rates'].items():
            currency_info = rates.currency.get_currency_by_code(con, code)  
            currency_id = currency_info['id'] 
            
            rate_rows.append([currency_id, base_id, rate, date, timestamp])

    ##### SAVE API DATA TO DB
    if rate_rows:
        
        rates.exchange_rate.insert_rates(con, rate_rows)

    return

db_path = "C:\\xampp\\htdocs\\educom-data-science\\python\\rates.duckdb"

if is_file_locked(db_path):
    runtime = dt.now()
    print(f"\nDatabase file {db_path} is currently locked. Exiting at {runtime}.")
    sys.exit(1)

with duckdb.connect(db_path) as con:
    runtime = dt.now()
    print(f"\nConnected and running at {runtime}.")
    save_rates_from_api(con)