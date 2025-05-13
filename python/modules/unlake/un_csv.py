import requests, os, io
from zipfile import ZipFile
import unlake.url_builder

save_folder = "C:\\xampp\\htdocs\\educom-data-science\\python\\modules\\unlake\\data"

def remove(filestring, deletechars):
    
    for c in deletechars:
        filestring = filestring.replace(c,'')
    
    return filestring;

def get_csv(mart_id, data_filter):
    
    url = unlake.url_builder.build_download_url(mart_id, data_filter)
    
    response = requests.get(url)
    response.raise_for_status()
    
    return response

def save_csv(response, mart_id, data_filter):

    zip_bytes = io.BytesIO(response.content)
    
    with ZipFile(zip_bytes) as z:
        file_name = z.namelist()[0]
        
        with z.open(file_name) as extracted_file:
            
            mart_id = remove(mart_id, '\\/:*?"<>|')
            data_filter = remove(data_filter, '\\/:*?"<>|')
            
            local_filename = 'un_data_' + mart_id + '_' + data_filter + '.csv'
            path = os.path.join(save_folder, local_filename)
            
            with open(path, 'wb') as output_file:
                output_file.write(extracted_file.read())            
    
    return
