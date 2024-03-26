def hapus_spasi_berlebih(kalimat):
    kalimat = kalimat.strip()  
    kalimat = " ".join(kalimat.split())  
    return kalimat

kalimat_input = input("Masukkan kalimat: ")
kalimat_output = hapus_spasi_berlebih(kalimat_input)

print(f"Yang Benar Adalah: {kalimat_output}")
