# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 14:21:23 2024

@author: chris
"""


import pandas as pd

# this uses UK census data for ages of people in Oxford.
df = pd.read_csv("oxfordAges.csv", usecols=[2,4])
df = df.rename(columns={"Age (101 categories) Code":"Age", "Observation":"Number"})

# Add up all the people.
totalPop = df["Number"].agg(sum)

halfPop = totalPop/2

# Count each number until you get halfway
for age in df.values:
    # print(age)
    halfPop-=age[1]
    if halfPop < 0:
        print("The median age is", age[0])
        break