from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import f_regression
from sklearn.feature_selection import mutual_info_regression
from sklearn import preprocessing
from scipy.signal import lfilter
import pandas as pd

def extract_value(dataset):
    columns_Dataframe = dataset.columns 
    for column in columns_Dataframe:
        countNaN = dataset[column].isna().sum()
        if countNaN > 500:
            dataset =  dataset.drop(column, axis=1)
    return dataset

def extract_value_avg(dataset):
    columns_Dataframe = list(filter(lambda name_column: (name_column.find('avg')!= -1), dataset.columns)) #select all column that contains avg
    selected_columns = dataset[columns_Dataframe] 
    dataset = selected_columns.copy() 
    for column in columns_Dataframe:
        countNaN = dataset[column].isna().sum() 
        if countNaN > 450:
            dataset =  dataset.drop(column, axis=1)
    return dataset

def split_dataset(x,y):
    return train_test_split(x,y, test_size=0.2) #split data in train and test

def lasso_model(x,y):
    return SelectKBest(chi2, k=2).fit_transform(x, y)#only positive values

def variance_three_shold(X):
    sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
    return sel.fit_transform(X)

def fill_NaN_values(dataset):
    for column in dataset.columns:
        dataset[column] = dataset[column].fillna(0)
    return dataset

def select_y(wind_turbine):
   return pd.DataFrame(data=wind_turbine.Rbt_avg,columns=['Rbt_avg'])

def select_best_f_regression(x_train,y_train,k,x_test):    
    fs = SelectKBest(score_func=f_regression, k=k)
    fs.fit(x_train, y_train)
    X_train_fs = fs.transform(x_train)
    X_test_fs = fs.transform(x_test)
    return X_train_fs, X_test_fs, fs

def select_best_mutual_f_regression(x_train,y_train,k,x_test):    
    fs = SelectKBest(score_func=mutual_info_regression, k=k)
    fs.fit(x_train, y_train)
    X_train_fs = fs.transform(x_train)
    X_test_fs = fs.transform(x_test)
    return X_train_fs, X_test_fs, fs

def standardize(x_train):
    return preprocessing.StandardScaler().fit(x_train).transform(x_train)

def remove_noise(x_array):
    n = 15  # the larger n is, the smoother curve will be
    b = [1.0 / n] * n
    a = 1
    return lfilter(b,a,x_array)
