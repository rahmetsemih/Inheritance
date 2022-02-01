class Insan():
    def __init__(self, isim, yas, sehir):
        self.isim = isim
        self.yas = yas
        self.sehir = sehir
        self.hobi = []

    def hobi_ekle(self, hobi):
        self.hobi.append(hobi)

    def bilgi(self):
        if self.hobi == []:
            pass
        else:
            print("Hobileri:")
            for i, j in enumerate(self.hobi):
                print(i+1, "-", j)
        print(f"{self.isim} {self.yas} yaşındadır ve {self.sehir}'lidir.")


class Ogrenci(Insan):
    ogrenciler = []

    def __init__(self, isim, yas, sehir, egitim_seviyesi):
        super().__init__(isim, yas, sehir)
        self.egitim_seviyesi = egitim_seviyesi
        self.ogrenciler.append(self.isim)

    def bilgi(self):
        super().bilgi()
        print(f"{self.isim} {self.egitim_seviyesi} eğitim seviyesinde öğrencidir.")

    @staticmethod
    def ortalama(a, b):
        print(f" Yıl sonundaki ortalamanız: {(a+b)/2}")

    @classmethod
    def öğrenci_listesi(cls):
        if cls.ogrenciler == []:
            print("Kayıtlı öğrenci bulunmamaktadır.")
        else:
            for i, j in enumerate(cls.ogrenciler):
                print(i+1, "-", j)


def test(): #Yazdığımız kodları yazdırdığımız yer...
    print("*"*20)
    insan = Insan("Semih", 20, "İstanbul")
    insan.hobi_ekle("Kitap okumak")
    insan.hobi_ekle("Seyahat etmek")
    insan.bilgi()

    print("*"*20)
    ogrenci = Ogrenci("Semih", 21, "İstanbul", "Öğrenci(Üni)")
    ogrenci.hobi_ekle("Kitap okumak")
    ogrenci.hobi_ekle("Seyahat etmek")
    ogrenci.bilgi()

    print("*"*20)
    Ogrenci.öğrenci_listesi()
    Ogrenci.ortalama(50,70)

test()