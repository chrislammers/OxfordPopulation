# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 18:22:21 2024

@author: chris
"""


import pandas as pd

df = pd.read_csv("out.csv")
df["Price"] = df["Price"].replace("[\£$,]", "", regex=True).astype(float)  # Clean and convert prices to float
average_prices = df.groupby("State")["Price"].mean().sort_values()

print("Average hotel prices by state:")
# print(average_prices)

print("The cheapest hotels are in "+str(average_prices.keys()[0])+" at an average price of "+str(average_prices[0])+" of your local currency")