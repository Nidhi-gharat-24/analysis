# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 14:15:48 2020

@author: admin
"""

import pandas as pd
import matplotlib.pyplot as plt
workbook1 = 'state.xlsx'

df = pd.read_excel(workbook1)
print(df.head())

values = df[['States','sales']]
print(values)

ax = values.plot.bar(x='States',y='sales',rot=0)
plt.show()
      
      
      