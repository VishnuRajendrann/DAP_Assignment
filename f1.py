import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("F1 Seasons champions.csv")
dataframe = pd.DataFrame(data)
dfh = dataframe.head(22)
dfh.plot(x="Grand Prixs", y="Laps", kind="bar", title="Number of laps in each of the Formula 1 Grand Prix circuits")
plt.show()
