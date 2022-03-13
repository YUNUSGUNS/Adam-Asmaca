# from cgi import test
# from contextlib import nullcontext
# from ctypes.wintypes import HACCEL
# from email.mime import image
# from gc import callbacks
from asyncio import events
import random
from time import time
from tkinter import *
from tkinter import messagebox
# import tkinter
# from turtle import pen
from PIL import Image, ImageTk
from numpy import delete


def delete_word():
    veri.delete(0,END)

def kelime_yazdırma(kelime):
    global kelime_çıktısı
    kelime_çıktısı = Label(text=kelime,font=("Arial", 15))
    kelime_çıktısı.place(relx=0.43,rely=0.25)


def harf_ara(bulunan_kelime):

    global hak 
    eslesme = False
    aranan_harf = veri.get().upper() 

    if len(aranan_harf) == 1 :

        if(hak==0):

            messagebox.showinfo("KAYBETTİNİZ","HAKKINIZ DOLDU KAYBETTİNİZ\nCevap:"+rastgele_kelime)
            kelime_çıktısı.destroy()
            oyun("C:\\Users\\ygune\\Desktop\\Adam_asmaca\\Adam-Asmaca\\Words\\Kelimeler")
            change_img()
           
        for i in range(len(rastgele_kelime)-1):  
            if (aranan_harf == rastgele_kelime[i]):
                eslesme = True
                bulunan_kelime[i] = aranan_harf
        
        if (eslesme==False):
            mesaj = Label(text=aranan_harf+" harfi kelimede bulunmamamktadır.")
            mesaj.place(relx=0.50,rely=0.35)
            mesaj.after(1000,mesaj.destroy)
            hak -= 1
            change_img()
        kelime_çıktısı.destroy()
        kelime_yazdırma(kelime)
        veri.delete(0,END)
    else:
        
        harf_girin_mesaji = Label(text="Lütfen bir harf giriniz.")
        harf_girin_mesaji.place(relx=0.50,rely=0.35)
        harf_girin_mesaji.after(1000,harf_girin_mesaji.destroy)

    if(aynı_mı(kelime)==True):  
        messagebox.showinfo("TEBRİKLER","🎉🎉🎉TEBRİKLER🎉🎉🎉\n OYUNU KAZANDINIZ")
        kelime_çıktısı.destroy()
        oyun("C:\\Users\\ygune\\Desktop\\Adam_asmaca\\Adam-Asmaca\\Words\\Kelimeler")
        change_img()
        
def aynı_mı (kelime):
    #global rastgele_kelime
    kaçış=False
    if boşluk!=-1:
        kaçış=True
    for i in range(len(rastgele_kelime)-1):
        if rastgele_kelime[i] != kelime[i]:
            if kaçış==True and i == boşluk:
                continue
            else:
                return False
    return True 

def change_img():
    #global hak
    resim ="C:\\Users\\ygune\\Desktop\\Adam_asmaca\\Adam-Asmaca\\Images\\"
    resim += str(6-hak)
    resim+=".png"
    image = Image.open(resim)
    boyutlu_resim = image.resize((215, 250))
    resim = ImageTk.PhotoImage(boyutlu_resim)
    label.configure(image=resim)
    label.image=resim

def entry_update(text):
   veri.delete(0,END)
   veri.insert(0,text)

def harf_al():
    harfler="ABCÇDEFGĞHİIJKLMNOÖPRSŞTUÜXVYZ"
    harf_sayisi=0
    for i in range(5):
        for j in range(6):

            def func(x=harfler[harf_sayisi]):
                return entry_update(x)

            harf = harfler[harf_sayisi]
            harf_sayisi+=1
            button[i*6+j*5] = Button(pencere,text=harf,width=11,height=2,command =  func)
            button[i*6+j*5].place(relx=0.05+j*0.150,rely=0.60+i*0.06) 

def rastgele_harf_bul():
    global rastgele_kelime,kelime
    bulunmayan_harfler=[]
    for i in range(len(kelime)):
        if(kelime[i] == "_"):
            bulunmayan_harfler.append(i)

    rastgele_harf_index = int(random.choice(bulunmayan_harfler))
    entry_update(rastgele_kelime[rastgele_harf_index])
    

def oyun(oyun_türü_sec):

    oyun_türü_sec_print = oyun_türü_sec.split("\\")
    
    kelime_çıktısı.destroy()

    oyun_türü_mesaji = Label(text=str(oyun_türü_sec_print[-1])+" kategorisinden kelime seçildi",font=("Arial", 11))
    oyun_türü_mesaji.place(relx=0.30,rely=0.45)
    oyun_türü_mesaji.after(2000,oyun_türü_mesaji.destroy)
    
    #DEĞERLER
    global button,hak
    hak=6
    button = {}
    
    oyun_türü_secimi = "C:\\Users\\ygune\\Desktop\\Adam_asmaca\\Adam-Asmaca\\Words\\"
    oyun_türü_secimi += str(oyun_türü_sec_print[-1])
    oyun_türü_secimi+=".txt"

    #KELİMELERİ OKUMA VE SEÇME
    kelime_dosyası = open(oyun_türü_secimi,encoding="utf-8")
    kelimeler__listesi = kelime_dosyası.readlines()
    kelime_dosyası.close()

    global rastgele_kelime,kelime,boşluk
    rastgele_kelime = random.choice(kelimeler__listesi).upper()

            

    kelime=[]
    boşluk=-1
    for i in range(len(rastgele_kelime)-1):
        kelime+="_"
        if rastgele_kelime[i] ==" ":
            kelime[i]="/"
            boşluk = i

    kelime_yazdırma(kelime)

def liste_box_yap():
    global oyun_türü
    oyun_türü = list_box.get(list_box.curselection())
    oyun(oyun_türü)
    

#****************************************************************************
#Create an instance of tkinter frame
pencere= Tk()

baslik = pencere.title("Adam asmaca")
pencere.geometry("600x700+90+50")

#ÇIKIŞ BUTONU
cikis = Button(text="Çıkış",width=10,command=pencere.quit)
cikis.place(relx=0.85,rely=0.93)

#SİLME BUTONU
silme_butonu = Button(text="Sil",command=delete_word,width=24,height=2)
silme_butonu.place(relx=0.350,rely=0.54)

#ENTRY VERİ GİRİŞİ BUTONU
veri = Entry(pencere,width=28)
veri.place(relx=0.35,rely=0.49)

#HARF GÖNDERME
harf_gonderme = Button(pencere,text="Harfi Gönder",width=24,height=2,command= lambda: harf_ara(kelime))
harf_gonderme.place(relx=0.05,rely=0.54)

#RASTGELE HARF
rastgele_harf = Button(pencere,text="İPUCU",width=24,height=2,command= lambda: rastgele_harf_bul())
rastgele_harf.place(relx=0.650,rely=0.54)

#LİSTBOX YAPIMI
list_box = Listbox(pencere,height=3)
list_box.place(relx=0.2,rely=0.91)
list_box.insert(END,"ULKELER")
list_box.insert(END,"SEHIRLER")   
list_box.insert(END,"Kelimeler")

yeni_kelime = Button(text="Yeni Kelime",width=10,command= lambda:liste_box_yap() )
yeni_kelime.place(relx=0.02,rely=0.93)


#oyun_türü="Kelimeler"

kelime_çıktısı = Label()

oyun("C:\\Users\\ygune\\Desktop\\Adam_asmaca\\Adam-Asmaca\\Words\\Kelimeler")


#HARFLER
harf_al()

#İLK RESİM
image = Image.open("C:\\Users\\ygune\\Desktop\\Adam_asmaca\\Adam-Asmaca\\Images\\0.png")
boyutlu_resim = image.resize((215, 250))
img1 = ImageTk.PhotoImage(boyutlu_resim)
label= Label(pencere,image= img1 )
label.place(relx=0.05,rely=0.055)


pencere.mainloop()