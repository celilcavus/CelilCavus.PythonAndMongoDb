import pymongo
from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://kullaniciadi:sifre@cluster0.6jdmqyb.mongodb.net/veritabaniadi?retryWrites=true&w=majority")

# print(client.list_database_names())

db = client.OgrenciNot

collection = db["OgrenciNot"]
while True:
    print("Öğrenci Sistemine Hoşgeldiniz..")
    print("1-Öğrenci Ekle")
    print("2-Öğrenci Sil")
    print("3-Öğrenci Listele")
    print("4-Öğrenci Güncelle")
    print("Q-Çikis")
    print("*"*40)
    secenek = input("Seçeniğiniz Nedir? :")

    if(secenek == "1"):
        while True:
            try:
                Ad = input("Öğrenci Adi : ")
                Soyad = input("Öğrenci Soyadi :")
                Numara = int(input("Öğrenci No : "))
                Final = int(input("Final Notu :"))
                Vize = int(input("Vize Notu :"))

                ortalama = (Vize * 0.4 + Final * 0.6)

                harfnotu = ""
                dortluksistem = 0.00

                if (ortalama >= 90 and ortalama <= 100):
                    harfnotu = "aa".upper()
                    dortluksistem = 4.00
                elif (ortalama >= 80 and ortalama <= 89):
                    harfnotu = "ba".upper()
                    dortluksistem = 3.50
                elif (ortalama >= 70 and ortalama <= 79):
                    harfnotu = "bb".upper()
                    dortluksistem = 3.00
                elif (ortalama >= 60 and ortalama <= 69):
                    harfnotu = "cb".upper()
                    dortluksistem = 2.50
                elif (ortalama >= 50 and ortalama <= 59):
                    harfnotu = "cc".upper()
                    dortluksistem = 2.00
                elif (ortalama >= 40 and ortalama <= 49):
                    harfnotu = "dc".upper()
                    dortluksistem = 1.50
                elif (ortalama >= 30 and ortalama <= 39):
                    harfnotu = "dd".upper()
                    dortluksistem = 1.00
                elif (ortalama >= 0 and ortalama <= 29):
                    harfnotu = "ff".upper()
                    dortluksistem = 0.00

                student = {"Name": Ad, "Surname": Soyad, "Numara": Numara, "Final": Final, "Vize": Vize,
                        "Ortalama": ortalama, "Harf Notu": harfnotu, "DortlukSistem": dortluksistem}
                
                collection.insert_one(student)
                yesNo = print("Öğrenci Eklemek İstermisiniz (Y/N) : ")

                if(yesNo == "Y" or yesNo == "y"):
                    continue
                else:
                    break
            
            except Exception as ex:
                print("*"*20)
                sistem =  input("Beklenmedik Hata Oluştu Sistem Yeniden Başlatilsin mi? (Y/N) : ")
                if(sistem == 'Y' or sistem == 'y'):
                    print("Sistem Yeniden Başlatiliyor.")
                    continue
                else:
                    print("İyi Günler Dilerim.!")
                    break
   
    elif(secenek == "2"):
        print("Öğrenci Listesi")
        print("*"*20)
        
        for i in  collection.find("",{"_id":0,"Name":1,"Surname":1,"Numara":1}):
            print(i)
        try:
            OgrNo = input("Silinicek Öğrencinin Numarasini Giriniz : ")
            onay = input("Seçiminizi Onaylayiniz (Y/N) : ")
            
            if(onay == "Y" or onay == "y"):
                collection.delete_many({"Numara":int(OgrNo)})
            else:
                print("Silme işlemi iptal edildi.!")
                continue 
        except Exception as ex:            
            print("*"*20)
            sistem =  input("Beklenmedik Hata Oluştu Sistem Yeniden Başlatilsin mi? (Y/N) : ")
            if(sistem == 'Y' or sistem == 'y'):
                print("Sistem Yeniden Başlatildi.")
                continue
            else:
                print("İyi Günler Dilerim.!")
                break
            
    elif(secenek == "3"):
         print("Öğrenci Listesi")
         print("*"*20)
         for i in  collection.find("",{"_id":0}):
            print(i)
         
    elif(secenek == "4"):
        print("Öğrenci Listesi")
        print("*"*20)
        
        for i in  collection.find("",{"_id":0,"Name":1,"Surname":1,"Numara":1}):
            print(i)
        try:
            OgrNo = input("Güncellenicek Öğrencinin Numarasini Giriniz : ")
            print("\n")
            Ad = input("Öğrenci Adi : ")
            Soyad = input("Öğrenci Soyadi :")
            Numara = int(input("Öğrenci No : "))
            Final = int(input("Final Notu :"))
            Vize = int(input("Vize Notu :"))
            print("\n")
            onay = input("Seçiminizi Onaylayiniz (Y/N) : ")
            
            if(onay == "Y" or onay == "y"):
                collection.update_one({"Numara":int(OgrNo)},
                                       {"Name": Ad, 
                                        "Surname": Soyad,
                                          "Numara": Numara,
                                            "Final": Final,
                                              "Vize": Vize})
            else:
                print("Güncelleme işlemi iptal edildi.!")
                continue 
        except Exception as ex:            
            print("*"*20)
            print("Hata : {} ".format(ex))
            sistem =  input("Beklenmedik Hata Oluştu Sistem Yeniden Başlatilsin mi? (Y/N) : ")
            if(sistem == 'Y' or sistem == 'y'):
                print("Sistem Yeniden Başlatildi.")
                continue
            else:
                print("İyi Günler Dilerim.!")
                break
    
    elif(secenek == "q" or secenek =="Q"):
        print("İyi Günler Dilerim!")
        break
    else:
        print("-"*20)
        print("Lütfen Doğru Seçim Yapiniz :)")
        continue
