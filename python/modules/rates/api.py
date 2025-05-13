import requests, time

BASE_URL_FIAT = "http://api.exchangeratesapi.io/v1/"
ACCESS_KEY_FIAT = "afad7f8cad4a41c7ff03d4729dd76dd7"

BASE_URL_CRYPTO = "https://api.coinranking.com/v2/"
ACCESS_KEY_CRYPTO = "coinrankingf26e9b1e456b115bd743d89c17a90c0462057fc7010fd5c0"
CRYPTO_REF_EURO = "5k-_VTxqtCEI"

def get_rates_from_api(currency_codes=[]):
    
    url = BASE_URL_FIAT + "latest"
    payload = {"access_key": ACCESS_KEY_FIAT}
    
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
    
    url = BASE_URL_FIAT + "symbols"
    payload = {"access_key": ACCESS_KEY_FIAT}
       
    response = requests.get(url, params=payload) 
    currencies = response.json()
        
    if 'error' in currencies:
        code = currencies['error']['code']
        msg = currencies['error']['message']
        print(f"Error in requesting possible symbols (currencies) with code: \"{code}\" and message: \"{msg}\".")
        
        return False
    
    return currencies
    
def get_crypto_info_from_api():
    
    headers = {
      'x-access-token': ACCESS_KEY_CRYPTO
    }

    response = requests.request("GET", BASE_URL_CRYPTO + "coins", headers=headers).json()
    
    coins = response['data']['coins']
    crypto_info = []
    
    for coin in coins:

        crypto = {}
        crypto['code'] = coin['symbol']
        crypto['name'] = coin['name']
        crypto['uuid'] = coin['uuid']
        crypto_info.append(crypto)

    return crypto_info

def get_crypto_rates_from_api():
     
    crypto_uuids = get_crypto_info_from_api()
    crypto_rates = {}
    
    headers = {
      'x-access-token': ACCESS_KEY_CRYPTO
    }

    for crypto in crypto_uuids:
        
        symbol = crypto['code']
        uuid = crypto['uuid']
        response = requests.request("GET", BASE_URL_CRYPTO + "coin/" + uuid + "/price?referenceCurrencyUuid=" + CRYPTO_REF_EURO, headers=headers).json()
        crypto_rates[symbol] = response['data']
        time.sleep(0.15)
    
    return crypto_rates