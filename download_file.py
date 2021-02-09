import requests
import os
import zipfile 
import pandas as pd

def read_csv():
    return pd.read_csv('data2017_2020\la-haute-borne-data-2017-2020.csv',';')

def read_file():
    return read_csv() if os.path.exists('data2017_2020\la-haute-borne-data-2017-2020.csv') else download_file()

def download_file(): 
    url = 'https://opendata-renewables.engie.com/media/datasets/01c55756-5cd6-4f60-9f63-2d771bb25a1a.zip'
    r = requests.get(url, stream=True)
    with open('01c55756-5cd6-4f60-9f63-2d771bb25a1a.zip', 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk) 
    with zipfile.ZipFile('01c55756-5cd6-4f60-9f63-2d771bb25a1a.zip', 'r') as zip_ref:
        zip_ref.extractall('data2017_2020/') 
    os.remove("01c55756-5cd6-4f60-9f63-2d771bb25a1a.zip") 
    return read_csv()