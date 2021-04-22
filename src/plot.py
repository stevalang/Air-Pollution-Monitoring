import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Distribution graphs (histogram/bar graph) of column data
def plot_per_column_distibution(df, n_graph_shown, n_graph_per_row):
    nunique = df.nunique()
    df = df[[col for col in df if nunique[col] > 1 and nunique[col] < 50]] 
    n_row, n_col = df.shape
    column_names = list(df)
    n_graph_row = (n_col + n_graph_per_row - 1) / n_graph_per_row
    plt.figure(num=None, figsize=(6 * n_graph_per_row, 8 * n_graph_per_row),
               dpi=80, facecolor='w', edgecolor='k')
    for i in range(min(n_col, n_graph_shown)):
        plt.subplot(n_graph_row, n_graph_per_row, i + 1)
        column_df = df.iloc[:, i]
        if (not np.issubdtype(type(column_df.iloc[0]), np.number)):
            value_counts = column_df.value_counts()
            value_counts.plot.bar()
        else:
            column_df.hist()
        plt.ylabel('counts')
        plt.xticks(rotation=90)
        plt.title(f'{column_names[i]} (column {i})')
    plt.tight_layout(pad=1.0, w_pad=1.0, h_pad=1.0)
    plt.show()


# Correlation matrix
def plot_correlation_matrix(df, graph_width):
    df = df.dropna('columns')# drop columns with NaN
    # keep cols where there are more than 1 unique values
    df = df[[col for col in df if df[col].nunique() > 1]]
    if df.shape[1] < 2:
        print(f'No correlation plots shown: The number of non-NaN or constant columns\
        ({df.shape[1]}) is less than 2')
        return
    corr = df.corr()
    plt.figure(num=None, figsize=(graph_width, graph_width), dpi=80,
            facecolor='w', edgecolor='k')
    corr_mat = plt.matshow(corr, fignum=1)
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.colorbar(corr_mat)
    plt.title('Correlation Matrix', fontsize=15)
    plt.show()


# Scatter and density plots
def plot_scatter_matrix(df, plot_size, text_size):
    # keep only numerical columns
    df = df.select_dtypes(include=[np.number])
    # remove rows and cols that would lead to df being singular
    df = df.dropna('columns')
    # keep cols where there are more than 1 unique values
    df = df[[col for col in df if df[col].nunique() > 1]]
    column_names = list(df)
    # reducing the number of cols for matrix inversion of kernel density plots
    if len(column_names) > 10:
        column_names = column_names[:10]
    df = df[column_names]
    ax = pd.plotting.scatter_matrix(df, alpha=0.75, figsize=[plot_size, plot_size], diagonal='kde')
    corrs = df.corr().values
    for i, j in zip(*plt.np.triu_indices_from(ax, k=1)):
        ax[i, j].annotate('Corr. coef = %.3f' % corrs[i, j], (0.8, 0.2),
                          xycoords='axes fraction', ha='center', va='center', size=text_size)
    plt.suptitle('Scatter and Density Plot')
    plt.show()
