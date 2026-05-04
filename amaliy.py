import pandas as pd
import numpy as np

# --- 1-topshiriq: Guruh ro'yxati ma'lumotlari ---
print("--- 1-topshiriq: Guruh ro'yxati ---")
guruh_data = {
    'ID': [101, 102, 103, 104, 105, 102], # 102 takrorlangan
    'FIO': ['Anvarov A.', 'Soliye J.', 'Karimov O.', None, 'Soliye J.'],
    'Yosh': [20, 21, None, 22, 21],
    'Stipendiya': [500000, 600000, 550000, None, 600000]
}

df_guruh = pd.DataFrame(guruh_data)


df_guruh['Yosh'] = df_guruh['Yosh'].fillna(df_guruh['Yosh'].mean()) # Bo'sh yoshni o'rtacha bilan to'ldirish[cite: 1]
df_guruh['Stipendiya'] = df_guruh['Stipendiya'].fillna(df_guruh['Stipendiya'].median()) # Bo'sh stipendiyani median bilan to'ldirish[cite: 1]
df_guruh = df_guruh.drop_duplicates() # Takroriy qatorlarni o'chirish[cite: 1]

print(df_guruh, "\n")

# --- 2-topshiriq: Mashina markalari ma'lumotlari ---
print("--- 2-topshiriq: Mashinalar jadvali ---")
mashina_data = {
    'Model': ['Chevrolet Gentra', 'Hyundai Elantra', 'Kia K5', None, 'Chevrolet Gentra'],
    'Yil': [2022, 2023, None, 2021, 2022],
    'Narxi': [15000, 22000, 28000, 12000, 15000]
}

df_mashina = pd.DataFrame(mashina_data)

# Ma'lumotlarni tozalash
df_mashina['Yil'] = df_mashina['Yil'].fillna(method='ffill') # Oldingi qiymat bilan to'ldirish
df_mashina = df_mashina.dropna(subset=['Model']) # Modeli yo'q qatorni o'chirish[cite: 1]
df_mashina = df_mashina.drop_duplicates() # Takroriylarni o'chirish[cite: 1]

# Faqat kerakli atributlarni ajratish
df_final = df_mashina[['Model', 'Narxi']] #[cite: 1]

print(df_final)