import random
import math

# Fungsi menghitung FX


def hitungEnergi(x, y):
    energi = ((4 - (2.1 * (x1**2)) + ((x1**4) / 3)) * (x1**2)) + \
        (x1 * x2) + ((-4 + 4 * (x2**2)) * (x2**2))
    return energi

# Fungsi inisialisasi state random.


def inisialisasiState():
    x = random.uniform(-10, 10)
    return x

# Fungsi menghitung probabilitas penerimaan, jika energi baru lebih besar dari
# energi lama


def hitungProbabilitas(energi, energiBaru, temperature):
    if (energiBaru < energi):
        return 1.0
    else:
        return (math.exp((energi - energiBaru) / temperature))

# Pengaturan parameter program


iterasi = 100000
temperature = 1000
# tMinimal = 0.0001 <-- kalau dipake, hasil jadi lebih random, tidak stabil
coolingRate = 0.99  # Seberapa besar temperature akan berkurang setiap iterasi,
# ini berarti temperature berkurang 0.01 persen setiap iterasi
x1 = inisialisasiState()  # Menginisialisasi koordinat x1 dengan random
x2 = inisialisasiState()  # Menginisialisasi koordinat x2 dengan random
BEST_SO_FAR = hitungEnergi(x1, x2)  # Hitung best so far dari koordinat awal
awal = hitungEnergi(x1, x2)  # Untuk keindahan output aja, gk penting
titikAwal = x1, x2  # Untuk output
print("Titik awal = " + str(titikAwal))  # Output juga
while (iterasi > 0):  # Mulai iterasi
    x1 = inisialisasiState()
    x2 = inisialisasiState()
    # Hitung energi baru dari state yang di generate secara random
    energiBaru = hitungEnergi(x1, x2)
    probabilitasDiterima = hitungProbabilitas(BEST_SO_FAR, energiBaru,
                                              temperature)
    if (energiBaru < BEST_SO_FAR):
        BEST_SO_FAR = energiBaru
        koordinat = x1, x2  # Untuk output aja
    # Else disini akan aktif jika Energi baru lebih besar daripada
    # BEST_SO_FAR(BSF), karena, walaupun energi baru lebih besar dari BSF,
    # tetap ada kemungkinan energi itu dimasukan ke dalam BSF
    else:
        if(probabilitasDiterima > random.random()):
            BEST_SO_FAR = energiBaru
            koordinat = x1, x2  # Untuk output aja
    iterasi = iterasi - 1  # Pengurangan iterasi
    temperature *= coolingRate  # Pengurangan temperature

print("Solusi awal = " + str(awal))
# print("Temperature terakhir = " + str(temperature))
# print("Titik terbaik = " + str(koordinat))
print("Solusi terbaik = " + str(BEST_SO_FAR))
