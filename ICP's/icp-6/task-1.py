import pandas as pd
import numpy as np
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt

df = pd.read_csv('train.csv')

# Create scatterplot of dataframe
sns.lmplot('GarageArea', # Horizontal axis
           'SalePrice', # Vertical axis
           data=df, # Data source
           fit_reg=False, # Don't fix a regression line
           scatter_kws={"marker": "D", # Set marker style
                        "s": 100}) # S marker size

# Set title
plt.title('plot between Garage Area and SalPrice')

plt.xlim(-200,1600)
# Set x-axis label
plt.xlabel('GarageArea')

# Set y-axis label
plt.ylabel('SalePrice')

plt.show()

train = df
train['GarageArea'] = train[train['GarageArea']>0]
train['GarageArea'] = train[train['GarageArea']<1200]


sns.lmplot('GarageArea', # Horizontal axis
           'SalePrice', # Vertical axis
           data=train, # Data source
           fit_reg=False, # Don't fix a regression line
           scatter_kws={"marker": "D", # Set marker style
                        "s": 100}) # S marker size

# Set title
plt.title('plot between Garage Area and SalPrice')

plt.xlim(-200, 1600)
# Set x-axis label
plt.xlabel('GarageArea')

# Set y-axis label
plt.ylabel('SalePrice')

plt.show()



