import gzip
import shutil
import os

# 1-topshiriq: Ma'lumotlarni siqishga misol
print("--- 1-topshiriq: Ma'lumotlarni siqish ---")

# Katta hajmli matn yaratamiz (takrorlanuvchi matn siqish uchun qulay)
original_text = "Dasturlashni o'rganish kelajak uchun juda muhim qadamdir. " * 500
data = original_text.encode('utf-8')

# Asl ma'lumotni oddiy faylga yozamiz
with open('asl_fayl.txt', 'wb') as f:
    f.write(data)

# Gzip yordamida siqish (Lossless compression - yo'qotishsiz siqish)
with open('asl_fayl.txt', 'rb') as f_in:
    with gzip.open('siqilgan_fayl.txt.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

asl_hajm = os.path.getsize('asl_fayl.txt')
siqilgan_hajm = os.path.getsize('siqilgan_fayl.txt.gz')

print(f"Asl fayl hajmi: {asl_hajm} bayt")
print(f"Siqilgan fayl hajmi: {siqilgan_hajm} bayt")
print(f"Siqish samaradorligi: {round((1 - siqilgan_hajm/asl_hajm)*100, 2)}%")

# 2-topshiriq: Siqilgan faylni ochish va tekshirish
print("\n--- 2-topshiriq: Faylni ochish va xulosa ---")

with gzip.open('siqilgan_fayl.txt.gz', 'rb') as f:
    ochilgan_ma_lumot = f.read().decode('utf-8')

# Tekshirish: ochilgan ma'lumot asl holati bilan bir xilmi?
if original_text == ochilgan_ma_lumot:
    print("Xulosa: Ma'lumot muvaffaqiyatli tiklandi. Hech qanday yo'qotish yo'q.")
else:
    print("Xulosa: Ma'lumot tiklashda xatolik yuz berdi.")

print(f"Ochilgan matnning boshlanishi: {ochilgan_ma_lumot[:50]}...")