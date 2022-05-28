import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpt
import sklearn as sk
import seaborn as sb
from scipy import stats


if __name__ == '__main__':
    dataset = pd.read_csv('data.csv', na_values=['NA'], delimiter=";")

    g = sb.FacetGrid(dataset, row="smoker", col="time", margin_titles=True)
    g.map(dataset.scatterplot, "total_bill", "tip", alpha=.7)


    
