import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plot

df = pd.read_csv("train.csv")

# print(df.head(10))
# print(df.describe())
print(df['Property_Area'].value_counts())

# df['ApplicantIncome'].hist(bins=50)
# plot.show()
#
# df.boxplot(column='ApplicantIncome')
# plot.show()

df.boxplot(column='ApplicantIncome', by = 'Education')
plot.show()


