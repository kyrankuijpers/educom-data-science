import duckdb
import rates.exchange_rate, rates.api, rates.currency

db_path = "C:\\xampp\\htdocs\\educom-data-science\\python\\rates.duckdb"
con = duckdb.connect(db_path)

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

save_rates_from_api(con)

con.close()