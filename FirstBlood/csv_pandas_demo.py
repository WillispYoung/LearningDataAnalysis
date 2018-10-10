import csv
import random

with open("data.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["A", "B", "C", "D", "E", "F", "G"])
    for i in range(0, 10):
        line = []
        for j in range(0, 7):
            line.append(random.randint(100, 1000))
        writer.writerow(line)

# first line is filled with labels
# line count is unnecessary

import pandas as pd
import numpy as np
import matplotlib as plt

df = pd.read_csv("data.csv")
# print(df.head(7))
# print(df.describe())

# df['C'].hist(bins=30)
# plt.pyplot.show()  # this is the way to show the plot, python-tk required

# df.boxplot(column="D", by="F")  # by is a measure of grouping
# plt.pyplot.show()  # box plot

# print(df['G'].value_counts())

# df['A_log'] = np.log(df['A'])
# df['A_log'].hist(bins=30)
# plt.pyplot.show()  # plot for log values
