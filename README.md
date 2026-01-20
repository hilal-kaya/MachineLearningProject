## Smart Bin Machine Learning Project

Bu projedeki amaç akıllı konteynerlere ait sensör verilerini analiz ederek hangi konteyner türünün, hangi atık türünde daha hızlı dolduğunu belirlemek ve ayrıca 
konteynerların boşaltılması gerekip gerekmediğini makine öğrenmesi modelleri ile tahmin etmektir.

# Veri
Projede 'Smart_Bin.csv' adlı veri seti kullandık.
Veri seti; konteyner doluluk seviyeleri, geçmiş doluluk bilgileri ve atık türlerine ait bilgiler içermektedir.

Projeye başlamadan önce veri setini inceledik: 

<img width="508" height="187" alt="Ekran Resmi 2026-01-20 21 13 28" src="https://github.com/user-attachments/assets/5d66e0b1-7720-4e33-bd72-72c9f75755e2" />

Eksik verileri aşağıdaki şekilde temizledik:

<img width="508" height="60" alt="Ekran Resmi 2026-01-20 21 14 33" src="https://github.com/user-attachments/assets/c4b5299d-affe-4acd-b2ca-1d3b1e6a20e4" />

# Pivot Analizi
Pivot tablosu oluşturduk ve bu tablo sayesinde:
Hangi konteyner türünün, hangi atık türünde daha hızlı dolduğunu gördük. 
En hızlı dolan konteyner + atık türü kombinasyonlarını şu şekilde belirledik:
<img width="508" height="434" alt="Ekran Resmi 2026-01-20 21 19 44" src="https://github.com/user-attachments/assets/8754500a-7d67-4f4a-821e-230763c3bdab" />

pivot sonuçlarını grafikle gösterdik:
<img width="985" height="590" alt="Unknown" src="https://github.com/user-attachments/assets/277719cb-4d6d-4c61-b910-a9994de05042" />

# Makine Öğrenmesi Modelleri
Pivot analizine ek olarak, konteynerin boşaltılması gerekip gerekmediğini tahmin etmek için iki farklı makine öğrenmesi modeli kullandik.
<img width="508" height="606" alt="Ekran Resmi 2026-01-20 21 25 24" src="https://github.com/user-attachments/assets/e6081a7b-93e3-44d5-a47f-2de22cc8bf75" />

Önemli olan featureları belirledik ve grafikleştiridk. 
<img width="989" height="490" alt="Unknown-2" src="https://github.com/user-attachments/assets/1f848cde-335f-4ac4-9f3d-180f29d1cb30" />


Logistic Reggression ile de modelimizi eğittik.

<img width="508" height="276" alt="Ekran Resmi 2026-01-20 21 29 52" src="https://github.com/user-attachments/assets/e9619d1d-1db5-452f-b65e-78f3169f51b1" />

# Model Karşılaştırılması
Sonra iki modelin başarımını grafiklerle karşılaştırdık:

<img width="590" height="390" alt="Unknown-3" src="https://github.com/user-attachments/assets/3b8c91a8-93b8-4439-9329-92cba13b1146" />

# Sonuç
Bu projede:
Verinin gerekli pivot analizini yaptık ve hangi konteyner + atık türü kombinasyonunun daha hızlı dolduğunu belirledik.
İki farklı makine öğrenmesi modelini eğitip karşılaştırdık.
Grafikler ile analizlerimizi destekledik. 















