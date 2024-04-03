from matplotlib.gridspec import GridSpec
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def line_graph(col1:pd.DatetimeIndex, col2:pd.DatetimeIndex, save_path:str, title_name:str):
    x = col1.index
    plt.figure(figsize= (15,4))
    grid = GridSpec(nrows=2, ncols=1) # get 2x1
    ax1 = plt.subplot(grid[0])

    sns.lineplot(x = x, y = col1, ax= ax1, color = "skyblue", label = "비교대상1")
    sns.scatterplot(x = x, y = col1, ax= ax1, color = "skyblue")

    sns.lineplot(x = x, y = col2, ax= ax1, color = "red", label = "비교대상2")
    sns.scatterplot(x = x, y = col2, ax= ax1, color = "red")

    ax1.set_xlabel("비교 col", fontsize = 10)
    ax1.set_ylabel("")
    ax1.set_title(f'비교 그래프 " {title_name}')
    plt.rc('font', family = 'Malgun Gothic')
    plt.legend(loc = 2, bbox_to_anchor = (1,1))
    plt.xticks(rotation = -45)
    plt.tight_layout()
    plt.savefig(f"{save_path}\\{title_name}.png", dpi = 500)
