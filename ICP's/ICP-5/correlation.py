import pandas as pd
import numpy as np
import seaborn
import seaborn as sns


#loading dataset
dataset = pd.read_csv('train.csv')
dataset['Sex'] = dataset['Sex'].map({'female':1, 'male':0}).astype(int)

#grouping by sex
print(dataset[['Sex', 'Survived']].groupby(['Sex'], as_index=True).mean().sort_values(by='Survived', ascending=False))
