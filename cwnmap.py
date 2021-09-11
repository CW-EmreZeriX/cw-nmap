import os


os.system("apt install nmap -y")
os.system("clear")

print("  ______        __    _   _ __  __    _    ____    ")
print(" / ___\ \      / /   | \ | |  \/  |  / \  |  _ \   ")
print("| |    \ \ /\ / /____|  \| | |\/| | / _ \ | |_) |  ")
print("| |___  \ V  V /_____| |\  | |  | |/ ___ \|  __/   ")
print(" \____|  \_/\_/      |_| \_|_|  |_/_/   \_\_|      ")
print("---------------------------------------------------")
print("Nmap kullanımını kolaylaştırmak için CyberWarrior adına yazılmıştır.")
print("---------------------------------------------------")
while(True): 
    a=input("Sistem güncellensin mi?(y/n):")
    print("---------------------------------------------------")
    if(a=="y"):
        os.system("apt update -y")
        os.system("apt upgrade -y") #EmreZeriX tarafından kodlanmıştır.
        break
    elif(a=="n")
        print("Sistem güncellenmeden devam ediliyor...")
        break
    else:
        print("y diyerek güncelleme yapabilir/n diyerek güncelleme yapmadan devam edebilirsiniz.")    
print("---------------------------------------------------")            
print("1-Nmap tarama")
print("2-Nmap agresif tarama")
print("3-Nmap belirli port detaylı tarama")
print("4-Nmap belirlediğiniz portları detaylı tarama")
print("---------------------------------------------------")

while(True):
    islem=int(input("Hangi işlemi yapmak istiyorsunuz:"))
    print("---------------------------------------------------")
    if(islem<5):
        if(islem==1):
            ip=input("Hedef ip adresi:")
            print("---------------------------------------------------")
            print("{0} Hedefine Nmap taraması başlatılıyor...".format(ip))
            os.system("nmap {0}".format(ip))
            break
        elif(islem==2):
            ip=input("Hedef ip adresi:")
            print("---------------------------------------------------")
            print("{0} Hedefine Nmap agresif tarama başlatılıyor...")
            os.system("nmap -A {0}".format(ip))
            break
        elif(islem==3):
            ip=input("Hedef ip adresi:") #EmreZeriX
            port=input("Hedef port:")
            print("---------------------------------------------------")
            print("{0} Hedefinin {1} portuna detaylı tarama başlatılıyor...".format(ip,port))
            os.system("nmap {0} -p{1} -A ".format(ip,port))
            break
        elif(islem==4):
            ip=input("Hedef ip adresi:") #EmreZeriX
            port1=input("Başlangıç portu:") 
            port2=input("Bitiş portu:")
            print("---------------------------------------------------")
            print("{0} hedefinin {1} portu ile {2} portu arasindaki tüm portlar taranıyor...".format(ip,port1,port2))
            os.system("nmap {0} -p{1}, {2}".format(ip,port1,port2))   
            break
    else:
        print("İşlem numarasını kontrol ediniz!")
        print("---------------------------------------------------")

