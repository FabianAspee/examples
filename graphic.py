import seaborn as sb
import matplotlib.pyplot as plt 
import numpy as np 
import math
import seaborn as sns 
from scipy.stats import norm

def linear_graph_unique(linear_data):
    plt.figure(figsize=(20,8))
    plt.plot(linear_data if type(linear_data) is np.ndarray else linear_data.values.reshape(-1,)) 
    
def plot_image():
    plt.show()
    
def pearson_graph(pearson_matrix):
    plt.matshow(pearson_matrix) 
    plt.show() 
def seaborn_pearson_plot(pearson_matrix): 
    a4_dims = (20, 9) 
    ax = plt.subplots(figsize=a4_dims) 
    sb.heatmap(pearson_matrix, 
            xticklabels=pearson_matrix.columns,
            yticklabels=pearson_matrix.columns,
            cmap='RdBu_r',
            annot=True,
            linewidth=0.5,
            ax=ax[1]) 
    plt.show() 

def plot_feature_selection(fs):
    for i in range(len(fs.scores_)):
	    print('Feature %d: %f' % (i, fs.scores_[i]))
    # plot the scores
    plt.bar([i for i in range(len(fs.scores_))], fs.scores_)
    plt.show()

def create_my_plot(dataframe): 
    # create distplots 
    row = math.floor(len(dataframe.columns)/3)
    mod = len(dataframe.columns)%3
    final_row = row +1 if mod>0 else row
    fig = plt.figure(figsize=(22, 15))
    i=1 
    for column in dataframe.columns:
        fig.add_subplot(final_row,3,i)
        _,bins,_ = plt.hist(dataframe[column], bins=50, density=True, color='g')

        mu, std = norm.fit(dataframe[column])   
        p = norm.pdf(bins, mu, std)
        i=i+1
        plt.plot(bins, p, 'k', linewidth=2)
        title = "Fit results: mean = %.2f,  std = %.2f, name = %s" % (mu, std, column)
        plt.title(title)
    
    plt.suptitle('Data with Normal Distribution')
  