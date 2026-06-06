import pandas as pd

df = pd.read_csv("munsell-array-fixed-choice.csv")

english_counts = df["english_color"].value_counts(normalize=True) * 100
spanish_counts = df["spanish_color"].value_counts(normalize=True) * 100
tsimane_counts = df["tsimane_color"].value_counts(normalize=True) * 100

english_df = english_counts.reset_index(name="percentage").rename(
    columns={"english_color": "color"}
)
spanish_df = spanish_counts.reset_index(name="percentage").rename(
    columns={"spanish_color": "color"}
)
tsimane_df = tsimane_counts.reset_index(name="percentage").rename(
    columns={"tsimane_color": "color"}
)

print("--- English Speaker Color Name Percentages ---")
print(english_df)
print("\n--- Spanish Speaker Color Name Percentages ---")
print(spanish_df)
print("\n--- Tsimane Speaker Color Name Percentages ---")
print(tsimane_df)

merged_df = pd.merge(
    english_df, tsimane_df, on="color", suffixes=("_english", "_tsimane")
)
print("\n--- Merged Data for Correlation (English vs. Tsimane) ---")
print(merged_df)