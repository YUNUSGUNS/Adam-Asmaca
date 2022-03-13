import random


def harf_ara(aranan_harf,rastgele_kelime,bulunan_kelime):
    global hak
    eslesme = False
    for i in range(len(rastgele_kelime)-1):
        
        if (aranan_harf == rastgele_kelime[i]):
            eslesme = True
            bulunan_kelime[i] = aranan_harf
    
    if (eslesme==False):
        print(aranan_harf," harfi kelimede bulunmamamktadır.")
        hak = hak - 1

    for i in bulunan_kelime:
        print(i, end="")     
    print()


    
def aynı_mı (aranan_kelime,kelime):
    for i in range(len(aranan_kelime)-1):
        if aranan_kelime[i] != kelime[i]:
            return False
    return True        



#KELİMLERİ OKUMA VE SEÇME
kelime_dosyası = open("Kelimeler.txt",encoding="utf-8")
kelimeler__listesi = kelime_dosyası.readlines()
kelime_dosyası.close()




while(True):
    rastgele_kelime = random.choice(kelimeler__listesi).upper()

    kelime=[]

    for i in range(len(rastgele_kelime)-1):
        print("_ ", end="")
        kelime.append("_")
    print()

    hak=5 
    while(True):

        if aynı_mı(rastgele_kelime,kelime):
            print("🎉🎉🎉🎉🎉Tebrikler bildiniz🎉🎉🎉🎉🎉")
            break

        if hak != 0:

            aranan_harf = input("Harf giriniz:")
            aranan_harf=  aranan_harf.upper()
            
            harf_ara(aranan_harf,rastgele_kelime,kelime)
        else:
            print("😞😞😞Hakkınz doldu kaybettiniz😞😞😞")
            print("Aranan kelime : ",rastgele_kelime)
            break

    print("BİTTİ")
    