import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Data_Cleaner import clean_raw_data

df = clean_raw_data("imdb_raw.csv")
#print(df.info())

year_count = df["release_year"].value_counts().sort_index() # yıllara göre film sayısını bulmak için

print(year_count.head())

#Bar plot grafiği
plt.figure(figsize= (12, 6))
plt.bar(year_count.index, year_count.values, color = "red")

plt.xlabel("Yıl", fontsize = 12)
plt.ylabel("Film Sayısı", fontsize = 12)
plt.title("IMDB En İyi 1000 Filmin Yıllara Göre Dağılımı", fontsize = 14)
plt.grid(axis= "both", linestyle = "--" )

plt.tight_layout()

#Scatter plot + trend line
plt.figure(figsize=(12,6))
plt.scatter(year_count.index, year_count.values, color = "blue")

z = np.polyfit(year_count.index, year_count.values,1) # Bir polinom oluşturur, seçtiğimiz 1 ise doğrusal olduğunu gösterir (derece)
# Veriye uygun polinom katsayıları hesaplar

p = np.poly1d(z) # Polinomu fonksiyon haline getirir
# Katsayıları Fonksiyon gibi kullanmaya yarar
plt.plot(year_count.index, p(year_count.index), "r--", label = "Doğrusal Eğilim")
plt.xlabel("Yıl", fontsize = 12)
plt.ylabel("Film Sayısı", fontsize = 12)
plt.title("IMDB En İyi 1000 Filmin Yıllara Göre Dağılımı (Scatter & Trend Çizgisi)", fontsize = 14)
plt.legend()
plt.grid(True)
plt.show()