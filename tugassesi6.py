
print("=====program grade nilai=====")

while(True):
    mapel = input("masukan mata pelajaran: ")
    nilai = input("masukan nilai anda : ")

    if(nilai.isnumeric() == True):
        nilai_int = int(nilai)
        if nilai_int >= 101:
            grade = "nilai salah"
            predikat = "nilai tidak tersedia, silahkan coba kembali"
        elif nilai_int >= 90:
            grade = "A"
            predikat = "dengan pujian"
        elif nilai_int >= 80:
            grade = "B"
            predikat = "sangat memuaskan"
        elif nilai_int >= 70:
            grade = "c"
            predikat = "memuaskan"
        elif nilai_int >= 60:
            grade = "D"
            predikat = "tidak memuaskan"    
        elif nilai_int >= 0:
            grade = "E"
            predikat = "tidak lulus"

        print("===================")
        print("mata peelajaran:", mapel)
        print("grade: ", grade)
        print("predikat: ", predikat)

    else :
        print("data salah!")

    apakahlanjut = input("\napakahlanjut? Y or N : ")
    if(apakahlanjut != "y"):
        break