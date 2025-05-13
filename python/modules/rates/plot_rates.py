import matplotlib.pyplot as plt
from datetime import datetime as dt
import pytz
import duckdb
import rates.exchange_rate as rat

db_path = "C:\\xampp\\htdocs\\educom-data-science\\python\\rates.duckdb"

timezone = pytz.timezone('Europe/Amsterdam')

def prepare_rate_and_period_for_plot(result):
    
    plot_currencies = []

    for code, rows in result.items():
        
        plot_currency = {}
        rates_x = []
        datetimes_y = []
        rate_changes_x = []
        
        startrate = rows[0]['rate']
        
        for row in rows:
            
            rate_x = row['rate']
            rates_x.append(rate_x)
            
            rate_change_x = (rate_x - startrate) / startrate * 100
            rate_changes_x.append(rate_change_x)
            
            timestamp_y = row['timestamp']
            datetime_y = dt.fromtimestamp(timestamp_y, timezone)   
            datetimes_y.append(datetime_y)
            
        plot_currency['code'] = code
        plot_currency['rates'] = rates_x
        plot_currency['datetimes'] = datetimes_y
        plot_currency['rate_changes'] = rate_changes_x
        plot_currencies.append(plot_currency)
    
    return plot_currencies

def plot_rates(result):
    
    plot_currencies = prepare_rate_and_period_for_plot(result)

    for currency in plot_currencies:

        dayshours = [datetime.strftime("%d-%H") for datetime in currency['datetimes']]       
        plt.plot(dayshours, currency['rates'], label = currency['code'])
        
    plt.legend()

    plt.show()
    
    return

def plot_rates_changes(result):
    
    plot_currencies = prepare_rate_and_period_for_plot(result)

    for currency in plot_currencies:

        dayshours = [datetime.strftime("%d-%H") for datetime in currency['datetimes']]       
        plt.plot(dayshours, currency['rate_changes'], label = currency['code'])
        
    plt.legend()

    plt.show()  
    
    return

def main():
     
    with duckdb.connect(db_path) as con:
    
        codes = ['USD', 'BTC', 'ETH', 'CNY']
        result = rat.get_rates_in_period(con, codes, '2025-05-08', '2025-05-12')
    
    plot_rates_changes(result)

    return

if __name__ == "__main__":
    main()











