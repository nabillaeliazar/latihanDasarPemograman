# deskriptif 
# membuat variabel nama barang
# membuat variabel harga barang
# membuat variabel persen harga 
# input nama barang 
# input harga barang 
# menghitung harga barang 
# harga barang * persen / 100
# print harga barang berserta nama barang 


nama_barang = input ("\nmasukan nama barang:") 
harga_barang1 = int(input("\nmasukan harga barang:"))
nama_barang = input ("\nmasukan nama barang:") 
harga_barang2 = int(input("\nmasukan harga barang:"))
nama_barang = input ("\nmasukan nama barang:") 
harga_barang3 = int(input("\nmasukan harga barang:"))

persen = 10

total = harga_barang1+harga_barang2+harga_barang3

hargapersen = int(total*10/100)

print('harga barang setelah di persenkan:', hargapersen) 
print('total harga keuntungan :', total + hargapersen)