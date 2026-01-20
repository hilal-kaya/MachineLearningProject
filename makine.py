import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# veri setini okudum
df = pd.read_csv("Smart_Bin.csv")

# ilk satırlara baktım
print(df.head())

#veri seti hakkında genel bilgi aldım 
print(df.info())

df.describe()

#eksik verileri temizledim
df.dropna(inplace=True)

#pivot tablosu olusturdum
pivot_sonuclari = pd.pivot_table(
    df,
    index="Container Type",
    columns="Recyclable fraction",
    values="FL_B",
    aggfunc="mean"
)
print(pivot_sonuclari)

#en hızlı dolan konteyner + atık turu 
pivot_uzun = pivot_sonuclari.stack().reset_index()
pivot_uzun.columns = [
    "Container Type",
    "Recyclable fraction",
    "FL_B_Ortalama"
]

en_hizli = pivot_uzun.sort_values(
    by="FL_B_Ortalama",
    ascending=False
)
print(en_hizli.head(10))

pivot_sonuclari.plot(
    kind="bar",
    figsize=(10, 6)
)
plt.title("Konteyner türüne göre ortalama doluluk (FL_B)")
plt.ylabel("Ortalama doluluk (FL_B)")
plt.xlabel("Konteyner türü")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#kategorik verileri sayısallastırdım
konteyner_encoder = LabelEncoder()
atik_encoder = LabelEncoder()
sinif_encoder = LabelEncoder()

df["Konteyner_Kodu"] = konteyner_encoder.fit_transform(df["Container Type"])
df["Atik_Turu_Kodu"] = atik_encoder.fit_transform(df["Recyclable fraction"])
df["Sinif_Kodu"] = sinif_encoder.fit_transform(df["Class"])

#modelde kullanılacak özellikler
X = df[
    [
        "FL_B", "FL_A", "VS",
        "FL_B_3", "FL_A_3",
        "FL_B_12", "FL_A_12",
        "Konteyner_Kodu",
        "Atik_Turu_Kodu"
    ]
]

y = df["Sinif_Kodu"]

X_egitim, X_test, y_egitim, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

#random forest ile modelimizi eğittim
rf_modeli = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

rf_modeli.fit(X_egitim, y_egitim)
rf_tahmin = rf_modeli.predict(X_test)

print("Accuracy:", accuracy_score(y_test, rf_tahmin))
print(classification_report(
    y_test,
    rf_tahmin,
    target_names=sinif_encoder.classes_
))

#hangi özellik daha önemli inceledim ve grafiklrstirdim
ozellik_onemleri = pd.DataFrame({
    "Özellik": X.columns,
    "Önem": rf_modeli.feature_importances_
}).sort_values(by="Önem", ascending=False)

print(ozellik_onemleri)

ozellik_onemleri.plot(
    x="Özellik",
    y="Önem",
    kind="bar",
    figsize=(10, 5),
    legend=False
)
plt.title("Random Forest - Özellik Önemleri")
plt.ylabel("Önem Derecesi")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#logistic reggresion
olceklendirici = StandardScaler()
X_egitim_olcekli = olceklendirici.fit_transform(X_egitim)
X_test_olcekli = olceklendirici.transform(X_test)

lr_modeli = LogisticRegression(max_iter=1000)
lr_modeli.fit(X_egitim_olcekli, y_egitim)
lr_tahmin = lr_modeli.predict(X_test_olcekli)

print("Accuracy:", accuracy_score(y_test, lr_tahmin))
print(classification_report(
    y_test,
    lr_tahmin,
    target_names=sinif_encoder.classes_
))
# modelleri karsılastırdım
rf_accuracy = accuracy_score(y_test, rf_tahmin)
lr_accuracy = accuracy_score(y_test, lr_tahmin)

modeller = ["Random Forest", "Logistic Regression"]
basarimlar = [rf_accuracy, lr_accuracy]

plt.figure(figsize=(6, 4))
plt.bar(modeller, basarimlar)
plt.ylabel("Accuracy")
plt.title("Model başarım karşılaştırması")
plt.ylim(0, 1)

for i, v in enumerate(basarimlar):
    plt.text(i, v + 0.01, f"{v:.2f}", ha="center")

plt.tight_layout()
plt.show()
