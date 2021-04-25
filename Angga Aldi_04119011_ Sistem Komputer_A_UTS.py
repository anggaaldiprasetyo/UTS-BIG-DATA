kalimat = input("Masukan Kalimat :")
file = kalimat.split()
jumlah=len(file)
for kata in kalimat.split():
    print(kata)
print("")
print(file)
print("jumlah kata pada kalimat tersebut adalah", jumlah)