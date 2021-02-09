
import pandas as pd   
import numpy as np
def pearson_correlation(data):
    return data.corr(method="pearson")

def transform_value(result):
    for value in range(len(result.index)):
        for val in range(len(result.columns)):
            result.iloc[value,val]=f'{result.iloc[value,val]:f}' 
    return result