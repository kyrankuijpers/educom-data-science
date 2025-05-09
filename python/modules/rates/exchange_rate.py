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

def get_rates_in_period(con, codes, startdate, enddate):
    
    result = {}

    for code in codes:
            
        query = """
                SELECT * FROM exchange_rate
                INNER JOIN currency 
                ON exchange_rate.currency_id = currency.id
                WHERE DATE BETWEEN ? AND ? AND code = ?
                """                    
        code_rates_df = con.sql(query, params=(startdate, enddate, code)).fetchdf()
    
        code_rates = code_rates_df.to_dict(orient="records")
        result[code] = code_rates   
    
    return result

def get_rates_with_currency(con, codes):
    
    result = {}

    for code in codes:
            
        query = """SELECT * FROM exchange_rate
                    INNER JOIN currency 
                    ON exchange_rate.currency_id = currency.id
                    WHERE code = ?
                """
                    
        code_rates_df = con.sql(query, params=(code,)).fetchdf()
    
        code_rates = code_rates_df.to_dict(orient="records")
        result[code] = code_rates
    
    return result

    

    


