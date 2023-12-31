class BangunDatar:
    def hitung_luas(self):
        pass    
class Persegi(BangunDatar):
    def init(self, sisi):
        self.sisi = sisi
    def hitung_luas(self):
        return self.sisi * self.sisi
class PersegiPanjang(BangunDatar):
    def init(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    def hitung_luas(self):
        return self.panjang * self.lebar
class Segitiga(BangunDatar):
    def init(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
    def hitung_luas(self):
        return 0.5 * self.alas * self.tinggi
class Lingkaran(BangunDatar):
    def init(self, radius):
        self.radius = radius
    def hitung_luas(self):
        return 3.14 * self.radius * self.radius
class Trapesium(BangunDatar):
    def init(self, atas, bawah, tinggi):
        self.atas = atas
        self.bawah = bawah
        self.tinggi = tinggi
    def hitung_luas(self):
        return 0.5 * (self.atas + self.bawah) * self.tinggi
class BelahKetupat(BangunDatar):
    def init (self, diagonal1, diagonal2):
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2
    def hitung_luas(self):
        return 0.5 * self.diagonal1 * self.diagonal2
class JajarGenjang(BangunDatar):
    def init (self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi 
    def hitung_luas(self):
        return self.alas * self.tinggi 
# Input jumlah bangun datar
n = int(input("Masukkan jumlah bangun datar: "))
# list untuk menyimpan bangun datar
bangun_datar_list = []
# Meminta input dan membuat objek bangun datar sesuai dengan jenisnya
for i in range(n):
    print(f"Bangun datar ke-{i+1}:")
    jenis = input("Jenis (persegi/persegi panjang/segitiga/lingkaran/trapesium/belah ketupat/jajar genjang): ")
    if jenis == "persegi":
        sisi = float(input("Panjang sisi: "))
        bangun = Persegi(sisi)
    elif jenis == "persegi panjang":
        panjang = float(input("Panjang: "))
        lebar = float(input("Lebar: "))
        bangun = PersegiPanjang(panjang, lebar)
    elif jenis == "segitiga":
        alas = float(input("Alas: "))
        tinggi = float(input("Tinggi: "))
        bangun = Segitiga(alas, tinggi)
    elif jenis == "lingkaran":
        radius = float(input("Jari jari: "))
        bangun = Lingkaran(radius)
    elif jenis == "trapesium":
        atas = float(input("Panjang sisi atas: "))
        bawah = float(input("Panjang sisi bawah: "))
        tinggi = float(input("Tinggi: "))
        bangun = Trapesium(atas, bawah, tinggi)
    elif jenis == "belah ketupat":
        diagonal1 = float(input("Diagonal 1: "))
        diagonal2 = float(input("Diagonal 2: "))
        bangun = BelahKetupat(diagonal1, diagonal2)
    elif jenis == "jajar genjang":
        alas = float(input("Alas: "))
        diagonal2 = float(input("Tinggi: "))
        bangun = JajarGenjang(alas, tinggi)
    else:
        print("Jenis bangun datar tidak valid.")
        continue
bangun_datar_list.append(bangun)
# Menghitung luas masing-masing bangun datar
luas_bangun_datar = [bangun.hitung_luas() for bangun in bangun_datar_list]
# Mengurutkan luas bangun datar
luas_bangun_datar.sort()
# Menghitung total luas bangun datar
total_luas = sum(luas_bangun_datar)
# Menampilkan hasil
print("\nLuas Bangun Datar:")
for i, luas in enumerate(luas_bangun_datar):
    print(f"Bangun datar ke-{i+1}: {luas:.2f}")
print(f"Total Luas: {total_luas:.2f}")