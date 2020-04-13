import pandas as pd
import numpy as np

from sklearn import preprocessing


df = pd.read_excel('data.xlsx')

df.head()

enc = preprocessing.OrdinalEncoder()

enc.fit_transform(df)

df.shape


















#df.head()

#enc = preprocessing.OrdinalEncoder()

#X = [df['Category'],df['type']]

#enc.fit(X)

#enc.transform(['A', 'B'])
