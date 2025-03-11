import pandas as pd 

def clean_raw_data(imdb_raw_csv):
    df = pd.read_csv(imdb_raw_csv)

    df["release_year"] = df["release_year"].str.extract(r'(\d{4})') # 4 basamaklı yılları ayıklamak için
    df["release_year"] = pd.to_numeric(df["release_year"], errors= "coerce") # değerleri sayısal değerlere çevirir. Sayıya çevrilemeyenler NaN yapılır.
    df.dropna(subset= ["release_year"]) # Değeri olmayan satırları (NaN) siler
    df["release_year"] = df["release_year"].astype(int) # "release_year sütununu" int değerlere çevirir
    
    # runtime'ı temizleme
    df["runtime"] = df["runtime"].str.replace("min", "").astype(float) # sayının sonundaki "min" ifadesini siler ve sayıyı float değere çevirir
    
    return df