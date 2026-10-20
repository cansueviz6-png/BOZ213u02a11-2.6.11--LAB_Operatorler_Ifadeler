hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
# Kodunuzu buraya yazın.
toplam = hour * 60 + mins + dura
bitis_saat = (toplam // 60) % 24
bitis_dakika = toplam % 60
print(bitis_saat, ":", bitis_dakika, sep="")
