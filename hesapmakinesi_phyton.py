toplama='+'
cikarma='-'
carpma='*'
bolme='/'
a=int(input("Lutfen 1. sayiyi giriniz:"))
b=int(input("Lutfen 2. sayiyi giriniz:"))
x=input("Lutfen yapacaginiz islemi seciniz:")
if(x=='+'):
    print("Sonuc:" , (a+b))
elif(x=='-'):
    print("Sonuc:" , (a-b))
elif(x=='*'):
    print("Sonuc:" , (a*b))
elif(x=='/'):
    print("Sonuc:" , (a/b))
else:
    print("Lutfen gecerli bir islem girin!")
