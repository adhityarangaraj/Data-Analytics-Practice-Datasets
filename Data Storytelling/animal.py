import matplotlib.pyplot as plt
import pandas as pd

word_trends = pd.read_csv("animal-word-trends-intro.csv")


def plot_word_trend(animal):
    trend = word_trends.query("word == @animal")
    plt.plot(trend["year"], trend["frequency"], label=animal)
    plt.ylabel("Frequency per million")


plot_word_trend("cat")
plot_word_trend("dog")
plt.title('Word frequency for "cat" and "dog" over time')
plt.legend()
plt.show()