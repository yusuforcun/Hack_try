import time 
sifre=int(input(" Kırılacak şifreyi giriniz : "))
x=(0000)
adım=0
sayilar=(1,2,3,4,5,6,7,8,9,)

while True :
    print(" <<<",x,"kontrol ediliyor>>>")

    if sifre==x:
        break
    
    else:
        for sayilar in range(1):
            adım+=1
            x+=1
            time.sleep(0.01)

            if x==sifre:
                break

            else:
                continue

        print("adım",adım,"denenen sifre:",x ,"\n""")


print("\n şifreye ulaşıldı\n şifre=",sifre)