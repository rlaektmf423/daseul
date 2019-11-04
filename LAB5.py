# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:39:14 2019

@author: user
"""

import pandas as pd
s=pd.Series([3,5,6,7,8], index=['1','2','3','4','5'])


import pandas as pd
import matplotlib.pyplot as plt
data = [[2, 4, 6, 8, 10],
        [6 ,7, 9, 2, 4],
        [1, 3, 5, 7, 9],
        [7, 8, 2, 4, 2]]
df=pd.DataFrame(data,columns=['a','b','c','d','e'])
df
plt.boxplot(df)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Box Plot')
plt.show()

import os
os.chdir(C:\Users\user\Downloads)

chipo = pd.read_excel
chipo.dtypes
chipo.isna().sum()
chipo = chipo.dropna()
chipo.isna().sum()
chipo.quantity
chipo['quantity']
plt.boxplot(chipo.quantity)
plt.boxplot(chipo.item_price)
plt.boxplot([chipo.quantity,chipo.item_price])
plt.xticks9[1,2],['quantity','item price'])
plt.title('Boxplot')
plt.show()