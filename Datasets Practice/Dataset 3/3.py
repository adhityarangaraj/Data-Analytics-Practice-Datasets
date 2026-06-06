import pandas as pd

df = pd.read_csv("jean-pocket-measurements.csv")

women_jeans = df.query('gender == "women"')
men_jeans = df.query('gender == "men"')

avg_women_front_height = women_jeans["height_front"].mean()
avg_men_front_height = men_jeans["height_front"].mean()
height_diff = avg_men_front_height - avg_women_front_height

print("Average Front Pocket Height:")
print("Women's:", avg_women_front_height, "cm")
print("Men's:", avg_men_front_height, "cm")
print("Difference:", height_diff, "cm")

print("\nStyle differences for Women:")
print(women_jeans.groupby("style")["height_front"].mean())

print("\nStyle differences for Men:")
print(men_jeans.groupby("style")["height_front"].mean())

print("\nAverage Back Pocket Sizes:")
print(df.groupby("gender")[["height_back", "width_back"]].mean())

phone_height = 15.0

women_fit = (women_jeans["height_front"] >= phone_height).mean() * 100
men_fit = (men_jeans["height_front"] >= phone_height).mean() * 100

print(f"\nPercentage of front pockets fitting a {phone_height}cm phone:")
print(f"Women's: {women_fit}%")
print(f"Men's: {men_fit}%")