import duckdb, os
import rates.api, rates.currency, rates.exchange_rate, rates.plot_rates 

db_path = "C:\\xampp\\htdocs\\educom-data-science\\python\\rates.duckdb"

##### INIT DB

def create_tables(con):
    
    rates.currency.create_table_currency(con)
    rates.exchange_rate.create_table_exchange_rate(con)
    rates.currency.populate_currency(con) 
    rates.currency.populate_currency_crypto(con)
    
    return

##### VIEW
with duckdb.connect(db_path) as con:

    con.sql("""SELECT * FROM exchange_rate
            """)
    
    codes = ['USD', 'GBP', 'RUB', 'CNY', 'AUD']
    result = rates.exchange_rate.get_rates_in_period(con, codes, '2025-05-07', '2025-05-12')

#rates.plot_rates.plot_rates_changes(result)

with duckdb.connect(db_path) as con:    

    rates.currency.show_currencies(con)
    rates.currency.get_currency_by_code(con, 'GT')
