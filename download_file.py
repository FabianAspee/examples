import requests
import os
import zipfile 
import pandas as pd

def read_csv(name_file=None,separator=';',columns=None):
    return pd.read_csv(f'data2017_2020\\{name_file}',separator,names=columns)

def read_file(name_file,url=None,isZip=False,separator=';',columns=None):
    return read_csv(name_file,separator,columns) if os.path.exists(f'data2017_2020\\{name_file}') else download_file() if isZip==True else download_file_csv(name_file,url,separator,columns)

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

def download_file_csv(name_file,url,separator,columns):  
    r = requests.get(f'{url}/{name_file}', stream=True)
    with open(name_file, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)  
    return read_csv(name_file,separator,columns)