import duckdb, os
import rates.api, rates.currency, rates.exchange_rate 

db_path = "C:\\xampp\\htdocs\\educom-data-science\\python\\rates.duckdb"

custom_currencies = []
con = duckdb.connect(db_path)

##### INIT DB

def create_tables(con):
    
    rates.currency.create_table_currency(con)
    rates.exchange_rate.create_table_exchange_rate(con)
    rates.currency.populate_currency(con) 
    
    return

##### VIEW

con.sql('SELECT * FROM exchange_rate').show()

##### CLOSE

con.close()