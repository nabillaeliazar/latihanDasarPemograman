while(True):
    print('-------------------------------')

    nama_barang = input("\nMasukakan nama barang pertama :")
    harga_barang1 = int(input('masukan harga barang :'))

    nama_barang = input("\nMasukakan nama barang kedua :")
    harga_barang2 = int(input('masukan harga barang :'))

    nama_barang = input("\nMasukakan nama barang ketiga :")
    harga_barang3 = int(input('masukan harga barang :'))

    persen = 10

    total = harga_barang1 + harga_barang2 + harga_barang3

    hargapersen = int(total * persen / 100)

    print("\n===========================================")
    print("============  S T R U K  B E L I ============")
    print("=============================================")
    print("\nModal                        :Rp.", total)
    print("harga penjualan                :Rp.", total + hargapersen)
    print("keuntungan atau laba           :Rp.", hargapersen)
    print("\n----------------------------------------------")

    apakahlanjut = input('apakah ingin input barang lain? Y or N : ')
    if(apakahlanjut!= 'Y') :
        break