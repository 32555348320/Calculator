kelime="phyton"
yanit=""
while True:
    giris=input("Tahmininizi giriniz:")

    if giris=='q':
        print("Uygulamadan cikiliyor")
        input()
        break
    if giris in kelime:
        yanit+=giris
        print("Dogru tahmin {}".format(giris))
    else:
        print("Tekrar deneyiniz")
        input()
        
    if len(yanit)==len(kelime):
      print("{} kelimesindeki tum harfleri bildiniz".format(kelime))
      input()
      break

    
