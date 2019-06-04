import pandas as pd

df = pd.DataFrame({'A': [1,'',3,4,5], 'B': ['',6,7,9,11]})
df.loc[df.A.isnull()]
df.A.unique()
df['A'].unique()
df.loc[:,'A'].unique()
df.sort_index(axis=1)
