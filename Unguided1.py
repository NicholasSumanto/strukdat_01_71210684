print("Pilih menu:")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")

while True :
    m = str(input("Pilihan Anda :"))
    a = eval(input("Bilangan Pertama :"))
    b = eval(input("Bilangan Kedua :"))


    if  m == "1" :
        jumlah = a + b
        print(jumlah)
    elif m == "2" :
        pengurangan = a - b
        print(pengurangan)
    elif m == "3" :
        kali = a*b
        print(kali)
    elif m == "4" :
        bagi = a/b
        print(bagi)
    c = input("Ketik Q untuk berhenti! :")
    if c == "Q" :
        break





