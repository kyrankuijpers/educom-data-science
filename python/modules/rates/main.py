import duckdb
import rates.api, rates.currency, rates.exchange_rate 

custom_currencies = []
con = duckdb.connect("rates.duckdb")

##### INIT DB

def create_tables(con):
    
    rates.currency.create_table_currency(con)
    rates.exchange_rate.create_table_exchange_rate(con)
    rates.currency.populate_currency(con) 
    
    return

##### VIEW

con.sql('SELECT * FROM exchange_rate').show()
con.sql('SELECT * FROM currency').show()  

##### CLOSE

con.close()