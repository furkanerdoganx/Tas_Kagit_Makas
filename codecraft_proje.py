import random

secenekler = ["taş", "kağıt", "makas"]
tas = secenekler[0]
kagit = secenekler[1]
makas = secenekler[2]

print("Taş kağıt makas oyununa hoşgeldiniz. Oyunu bitirmek için b ye basınız.")

while True:
    secim = input ("taş? kağıt? makas? : ")
    pc_secimi = random.choice(secenekler)
    
    if secim == tas:
        if pc_secimi == tas:
            print("Bilgisayarın seçimi: " , pc_secimi , ". Berabere kaldınız.")
            
        elif pc_secimi == kagit:
            print("Bilgisayarın seçimi:" , pc_secimi , ". Yenildiniz.")
            
        else:
            print("Bilgisayarın seçimi:" , pc_secimi , ". Kazandınız.")
        continue    
            
    if secim == kagit:
        if pc_secimi == kagit:
            print("Bilgisayarın seçimi" , pc_secimi , ". Berabere kaldınız.")
            
        elif pc_secimi == makas:
            print("Bilgisayarın seçimi" , pc_secimi , ". Yenildiniz.")
            
        else:
            print("Bilgisayarın seçimi" , pc_secimi , ". Kazandınız.")
        continue
            
            
    if secim == makas:
        
        if pc_secimi == tas:
            print("Bilgisayarın seçimi" , pc_secimi , ". Kaybettiniz.")
            
        elif pc_secimi == kagit:
            print("Bilgisayarın seçimi" , pc_secimi , ". Kazandınız.")
            
        else:
            print("Bilgisayarın seçimi ", pc_secimi , ". Berabere kaldınız.")
        continue    
            
            
    if secim == 'b':
        print("Oyun bitti. Görüşmek üzere..")
       
    break
            
         
            
