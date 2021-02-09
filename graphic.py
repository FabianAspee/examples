import seaborn as sb
import matplotlib.pyplot as plt 
import numpy as np
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