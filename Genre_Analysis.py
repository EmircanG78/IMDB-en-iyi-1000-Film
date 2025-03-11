import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("imdb_raw.csv")
#print(df.head())
Top_movies = df.sort_values("rating", ascending= False)
#print(Top_movies[["title", "rating", "genre"]])

df["genre"] = df["genre"].str.split(", ")  # Virgüle göre ayırır
df_exploded = df.explode("genre")  # Her türü ayrı satır yapar

genre_counts = df_exploded["genre"].value_counts()
print(genre_counts)

plt.figure(figsize=(12,6))
plt.bar(genre_counts.index, genre_counts.values, color = "skyblue")
plt.xticks(rotation = 90)
plt.xlabel("Name of Genre")
plt.ylabel("Number of Counts ")
plt.title("Genre Counter")
plt.show()
plt.clf()

