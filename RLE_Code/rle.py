def kompresi(data):
    hasilkompresi = ""
    hurufsebelumnya = ""
    x = 1
    if not data:
        return ""
    for char in data:
        if char !=hurufsebelumnya:
            if hurufsebelumnya:
                hasilkompresi += str(x) + hurufsebelumnya
            x = 1
            hurufsebelumnya = char
        else:
            x += 1
    hasilkompresi += str(x) + hurufsebelumnya
    return hasilkompresi

def dekompresi(data):
    hasildekompresi = ""
    x = ""
    for char in data:
        if char.isdigit():
            x += char
        else:
            hasildekompresi += char * int(x)
            x = ""
    return hasildekompresi

file = open("kompres.txt", "r")
kalimat = file.read()
print("Kalimat  : ", kalimat)
print("Masukkan Pilihan :")
print("1. Kompresi")
print("2. Dekompresi")
Pilihan = input ("Pilihan 1/2   : ")

#kompresi
if Pilihan == "1":
    hasilnya = kompresi(kalimat)
    print("Hasil Kompresi   : ", hasilnya)

#dekompresi
else:
    hasilnya = dekompresi(kalimat)
    print("Hasil Dekompresi   : ", hasilnya)
file.close()
filekompres = open("kompres.txt", "w")
filekompres.write(hasilnya)