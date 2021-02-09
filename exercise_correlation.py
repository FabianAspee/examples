from IPython.display import display, HTML
import pandas as pd
import numpy as np
import pearson_correlation as ps
import pre_processing as pre
import graphic as gr
import download_file as dl
 
from pca import pca
 
data = dl.read_file() 
wind_turbine = data[data['Wind_turbine_name'] =='R80721']
wind_turbine = pre.extract_value_avg(wind_turbine.copy())
  
  
#----------------------------------------PEARSON-----------------------------------------------------
pearson_matrix = ps.pearson_correlation(wind_turbine)  
result = ps.transform_value(pearson_matrix)
result=result.astype(float)
#gr.seaborn_pearson_plot(result)  
#----------------------------------------PEARSON-----------------------------------------------------

#-----------------------------------FILLNaNVALUES AND SELECT TARGET----------------------------------
wind_turbine = pre.fill_NaN_values(wind_turbine.copy())
y_train =pre.select_y(wind_turbine)
wind_turbine = wind_turbine.drop('Rbt_avg',axis=1)  
wind_turbine.hist()

#-----------------------------------FILLNaNVALUES AND SELECT TARGET----------------------------------

#-----------------------------------SPLIT AND STANDARIZE DATA ---------------------------------------
x_train, x_test, y_train, y_test = pre.train_test_split(wind_turbine,y_train)  
x_train = pre.standardize(x_train)
x_test = pre.standardize(x_test)  
#-----------------------------------SPLIT AND STANDARIZE DATA ---------------------------------------
#-----------------------------------VIEW OUTLIER --------------------------------------------------
 
model = pca(alpha=0.05, n_std=3)
out = model.fit_transform(x_train) 
display(out)
print(out['outliers'])
model.biplot(legend=True, SPE=True, hotellingt2=True)
model.biplot3d(legend=True, SPE=True, hotellingt2=True)

# Create only the scatter plots
model.scatter(legend=True, SPE=True, hotellingt2=True)
model.scatter3d(legend=True, SPE=True, hotellingt2=True)
 
#-----------------------------------VIEW OUTLIER --------------------------------------------------


#-----------------------------------PLOT ORIGINAL AND STANDAR DATA ---------------------------------
ba_avg_data_graph = wind_turbine.Ba_avg.head(300) 
 
gr.linear_graph_unique(ba_avg_data_graph)
one_column_select = x_train[0:300,0:1]
gr.linear_graph_unique(one_column_select)#[start_row_index:end_row_index, start_column_index:end_column_index]

one_column_select = pre.remove_noise(one_column_select.copy())

display(one_column_select) 
gr.linear_graph_unique(one_column_select)#[start_row_index:end_row_index, start_column_index:end_column_index]
gr.plot_image()
#-----------------------------------PLOT ORIGINAL AND STANDAR DATA ---------------------------------

#----------------------------------PLOT BEST FEATURES ---------------------------------------------

new_x_train,new_x_test,selectBest = pre.select_best_f_regression(x_train,y_train,'all',x_test) 
gr.plot_feature_selection(selectBest) 
new_x_train,new_x_test,selectBest = pre.select_best_mutual_f_regression(x_train,y_train,'all',x_test)
gr.plot_feature_selection(selectBest)
#----------------------------------PLOT BEST FEATURES --------------------------------------------- 