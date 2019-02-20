# 1. Import necessary libraries and datasets
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

plt.show()

df = pd.read_csv("./taxi.csv")

# 2. Visualize the data
# # Pair-plot to see the co-relation between features
sns.pairplot(df)
# # Head-maps to see the co-relation mathematically
sns.heatmap(df)
