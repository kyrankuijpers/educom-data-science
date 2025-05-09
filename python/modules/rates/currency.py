import duckdb 
import rates.api 

def create_table_currency(con):
    con.sql("""
        CREATE SEQUENCE IF NOT EXISTS currency_id_seq START 1;
            
        CREATE TABLE IF NOT EXISTS currency (
            id   INTEGER PRIMARY KEY DEFAULT nextval('currency_id_seq'),
            code VARCHAR UNIQUE, 
            name VARCHAR
        );""")
    
    return

def get_currency_by_code(con, code):
    
    currency_df = con.sql(f"""
        SELECT * FROM currency WHERE code = '{code}'
        """).fetchdf()
    
    result = currency_df.to_dict(orient="records")
    currency_dict = result[0] if result else {}    
        
    return currency_dict
    

def insert_currency(con, code, name):
    
    con.execute("""INSERT INTO currency (code, name)
            VALUES (?, ?);""", (code, name))
            
    return

def populate_currency(con):
    
    currencies = rates.api.get_currencies_from_api()
    symbols = currencies['symbols']
    
    for code, name in symbols.items():
        insert_currency(con, code, name)
        
    return

def main():
    
    return

if __name__ == "__main__":
    main()