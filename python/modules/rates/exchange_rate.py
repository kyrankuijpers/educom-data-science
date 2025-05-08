import duckdb, datetime
import rates.currency, rates.api

def create_table_exchange_rate(con):
    con.sql("""
        CREATE SEQUENCE IF NOT EXISTS rate_id_seq START 1;
        
        CREATE TABLE IF NOT EXISTS exchange_rate (
            id INTEGER PRIMARY KEY DEFAULT nextval('rate_id_seq'),
            currency_id INTEGER REFERENCES currency(id),
            base_id INTEGER REFERENCES currency(id),
            rate DECIMAL,
            date DATE,
            timestamp INTEGER
            );
        """)    
    
    return

def insert_rate(con, currency_id, base_id, rate, date, timestamp):
    
    con.execute("""INSERT INTO exchange_rate
            (currency_id, base_id, rate, date, timestamp)
            VALUES (?, ?, ?, ?, ?);""", (currency_id, base_id, rate, date, timestamp))
            
    return

def insert_rates(con, rate_rows):
      
    con.executemany("""INSERT INTO exchange_rate
                    (currency_id, base_id, rate, date, timestamp)
                    VALUES (?, ?, ?, ?, ?)""", rate_rows)

    return

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

def main():
    
    con = duckdb.connect("rates.duckdb")
    con.sql("SELECT * FROM exchange_rate").show()
    con.close()
    
    return

if __name__ == "__main__":
    main()