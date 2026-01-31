import pandas as pd
import matplotlib.pyplot as plt

# Load California Housing training data
df = pd.read_csv("california_housing_train.csv")

# Create a boxplot for median house value
plt.figure()
df["median_house_value"].plot(kind="box")
plt.title("California Housing: Median House Value")

# Save the figure
plt.savefig("figs/boxplot.png")
plt.close()
