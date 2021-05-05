TugbaHesap={
    'isim':'Tugba',
    'hesapNo':'12345678',
    'bakiye':5000,
    'ekHesap':1000
    }

MeloHesap={
    'isim':'Melo',
    'hesapNo':'87654321',
    'bakiye':7000,
    'ekHesap':2000
    }

def ParaCek(hesap,tutar):
    print(f"Merhaba {hesap['isim']}")

    if(hesap['bakiye'] >= tutar):
        hesap['bakiye']-=tutar
        print("Paranizi alabilirsiniz..")
        bakiyeSorgula(hesap)

    else:
        ToplamPara=hesap['bakiye']+hesap['ekHesap']

        if(ToplamPara>=tutar):
            ekHesapKullanilsinMi=input("Ek hesap kullanilsin mi?=")

            if(ekHesapKullanilsinMi=='e'):
                EkKullanilacakPara=tutar-hesap['bakiye']
                hesap['bakiye']=0
                hesap['ekHesap']-=EkKullanilacakPara
                print("Paranizi alabilirsiniz..")
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} TL bulunmaktadir.")
        else:
            print("Uzgunuz, bakiye yetersiz..")
            bakiyeSorgula(hesap)

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} TL bulunmaktadir.Ek bakiye tutariniz:{hesap['ekHesap']}")


ParaCek(TugbaHesap,2500)
print("-"*30)
ParaCek(MeloHesap,3400)