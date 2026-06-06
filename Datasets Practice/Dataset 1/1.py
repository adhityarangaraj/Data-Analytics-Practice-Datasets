import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("largest-islands.csv")

tropics_10 = df.query('climate == "tropics"').head(10)
print(tropics_10)

largest_per_region = df.groupby("region").first()
print(largest_per_region)

multiple_countries = df[df["countries"].str.contains(",")]
print(multiple_countries)

df_sorted = df.sort_values("rank")
plt.plot(df_sorted["rank"], df_sorted["area"])
plt.xlabel("Rank")
plt.ylabel("Area")
plt.title("Island Area vs Rank")
plt.show()