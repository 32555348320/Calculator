
import re

def sifre_gucu_degerlendir(sifre):
    uzunluk = len(sifre)
    
    # Şifre uzunluğu
    uzunluk_puani = min(10, uzunluk)  # Maksimum puan 10

    # Rakam kontrolü
    rakam = bool(re.search(r'\d', sifre))
    rakam_puani = 2 if rakam else 0

    # Özel karakter kontrolü
    ozel_karakter = bool(re.search(r'[@$!%*?&]', sifre))
    ozel_karakter_puani = 4 if ozel_karakter else 0

    # Toplam puan
    toplam_puan = uzunluk_puani + rakam_puani + ozel_karakter_puani

    # Güç değerlendirmesi
    if toplam_puan < 8:
        guc = "Zayıf"
    elif 8 <= toplam_puan < 12:
        guc = "Orta"
    elif 12 <= toplam_puan < 16:
        guc = "Güçlü"
    else:
        guc = "Çok Güçlü"

    return guc, toplam_puan

def main():
    sifre = input("Lütfen şifrenizi giriniz: ")
    guc, puan = sifre_gucu_degerlendir(sifre)
    print(f"Şifrenizin gücü: {guc} (Puan: {puan})")

if __name__ == "__main__":
    main()

