print(12*"="+"aplikasi sederhana" + 12 * "=")

print("menu")
print("1.menghitung luas segitiga")
print("2.menghitung luas persegi panjang")
print("3.menentukan bilangan ganjil")
print("4.Quit")

while True :
    print("menu")
    print("1.menghitung luas segitiga")
    print("2.menghitung luas persegi panjang")
    print("3.menentukan bilangan ganjil")
    print("4.Quit")

    listmenu = input("masukan pilihan : ")

    if listmenu == "1":
        print("menu -- LUAS SEGITIGA")
        alas = float(input("masukan alas = "))
        tinggi = float (input("masukan tinggi = "))
        rumus1 = 1/2 * alas * tinggi
        print ("luas segitiga =", float(rumus1))

    elif listmenu == "2":
        print("menu -- luas persegi panjang ")
        panjang = float(input("masukan panjang = "))
        lebar = float (input("masukan lebar = "))
        rumus2 = pamjang * lebar
        print ("luas persegi panjang =", float(rumus2))
    
    elif listmenu == "3":
        print("menu--hasil ganjil/genap")
        angka = int(input("\nmasukan angka : "))

        if (angka % 2 == 0):
            print("angka", angka "merupakan angka genap")
    