#!/usr/bin/env python3

import os


os.system("clear")


banner="""
M""MMMMM""MM M""MMMMMMMM M""MMMM""M
M  MMMMM  MM M  MMMMMMMM M. `MM' .M
M         `M M  MMMMMMMM MM.    .MM
M  MMMMM  MM M  MMMMMMMM MMMb  dMMM
M  MMMMM  MM M  MMMMMMMM MMMM  MMMM
M  MMMMM  MM M         M MMMM  MMMM
MMMMMMMMMMMM MMMMMMMMMMM MMMMMMMMMM



############################
Encoding person:IGNİS   ####
############################

"""
print(banner)


import os

print("""
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█

PORT TARAMA ARACI


1)Normal Port Tarama
2)Servis Ve Versiyon Tarama
3)Isletim Sistemi Tarama
4)Cıkıs Icın Q
""")

islemno =input("Islem Numarası Giriniz:")

if(islemno=="1"):
        hedefip = input("Hedef Ip Giriniz: ")
        os.system("nmap " + hedefip)
elif(islemno=="2"):
        hedefip = input("Hedef Ip Giriniz: ")
        os.system("nmap -sS -sV "+ hedefip)
elif(islemno=="3"):
        hedefip = input("Hedef Ip Giriniz: ")
        os.system("nmap -o "+ hedefip)
elif islemno=="q" or islemno=="Q":
                quit()
else:
         input("Hatali Girdiniz Devam Etmek İçin Enter'a basınız!")
