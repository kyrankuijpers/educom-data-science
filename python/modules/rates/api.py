import requests

BASE_URL = "http://api.exchangeratesapi.io/v1/"
ACCESS_KEY = "afad7f8cad4a41c7ff03d4729dd76dd7"

def get_rates_from_api(currency_codes=[]):
    
    url = BASE_URL + "latest"
    payload = {"access_key": ACCESS_KEY}
    
    if not currency_codes == []:
        
        currency_string = ",".join(currency_codes)
        payload['symbols'] = currency_string
       
    response = requests.get(url, params=payload) 
    data = response.json()
        
    if 'error' in data:
        code = data['error']['code']
        msg = data['error']['message']
        print(f"Error in requesting latest rates with code: \"{code}\" and message: \"{msg}\".")
        
        return False
    
    return data

def get_currencies_from_api():
    
    url = BASE_URL + "symbols"
    payload = {"access_key": ACCESS_KEY}
       
    response = requests.get(url, params=payload) 
    currencies = response.json()
        
    if 'error' in currencies:
        code = currencies['error']['code']
        msg = currencies['error']['message']
        print(f"Error in requesting possible symbols (currencies) with code: \"{code}\" and message: \"{msg}\".")
        
        return False
    
    return currencies
    
