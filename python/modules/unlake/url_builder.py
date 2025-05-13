import requests, json

base_url_download = "https://data.un.org/Handlers/DownloadHandler.ashx?DataFilter="

def get_mart_ids():
    
    mart_url = "http://data.un.org/Handlers/ExplorerHandler.ashx?t=marts"
    mart_ids = []
    
    response = requests.get(mart_url)
    bad_json = response.text
    
    data = unfuck_json(bad_json)
    
    for mart in data:
        mart_id = mart['martId']
        mart_ids.append(mart_id)
    
    return mart_ids

def get_json_with_data_filters(mart_id):
    
    base_url_data_filters = "http://data.un.org/Handlers/ExplorerHandler.ashx"
    
    response = requests.get(base_url_data_filters, params={"m": mart_id})
    bad_json = response.text
    
    data = unfuck_json(bad_json)
    
    return data

def unfuck_json(bad_json):
    
    good_json = bad_json.replace('Nodes: ', '"Nodes" : ')
    data = json.loads(good_json)['Nodes']
    
    return data

def build_download_url(mart_id, data_filter):
    
    url = base_url_download + data_filter + "&DataMartId=" + mart_id
    
    return url



