"""
Bu komut dosyası, hayvanların etkileşime girip eylemler gerçekleştirdiği bir çiftlik günlüğünü simüle eder.

Farklı hayvanların (örneğin inekler ve tavuklar) davranışlarını şu şekilde gösterir:
- Onları "konuşturarak” karakteristik seslerini sergilemek.
- Onları besleyerek enerjilerini artırmak ve kaynaklar (örneğin süt veya yumurta) üretmek.
- Eylemlerinin sonuçlarını yazdırmak.

Kullanılan sınıflar:
- İnek: Süt üreten bir ineği temsil eder.
- Tavuk: Yumurta yumurtlayan (dişi ise) ve cinsiyete özgü sesler çıkaran bir tavuğu temsil eder.
"""

from farm.cow import Cow
from farm.chicken import Chicken

print("\n\n📝 Üçüncü Gün: Hayvanlar Konuşuyor")

# 1. Kodu okuyun ve sınıfları kodlamak için bazı ipuçları toplayın.
cow = Cow()
female_chicken = Chicken('female')
male_chicken = Chicken('male')

print(f"İnek {cow.talk()} diyor.")
print(f"Dişi tavuk {female_chicken.talk()} diyor.")
print(f"Erkek tavuk {male_chicken.talk()} diyor")

print("\n\n📝 Dördüncü Gün: Hayvanları Besle")

# 1. Tüm hayvanlarını `animals` listesinde sakla
animals = [cow, female_chicken, male_chicken]

# 2. Hepsini besle (döngü)
for animal in animals:
    animal.feed()

# 4. Sonuçları yazdır
print(f"The cow produced {cow.milk} liters of milk")
print(f"The female chicken produced {female_chicken.eggs} eggs")
print(f"The male chicken produced {male_chicken.eggs} eggs")

# 2. Her hayvan için `feed` yöntemini çağır (liste üzerinde bir döngü kullan)
pass  # BURAYA KODUNU YAZ

# 3. TODO'ları değiştirin

# 4. Aşağıdaki 3 satırı yazdırın:
# "The cow produced ## liters of milk"
# "The female chicken produced ## eggs"
# "The male chicken produced ## eggs"
pass  # KODUNUZ BURAYA