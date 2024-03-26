def hitung_kemunculan_kata(kalimat, kata):
    kalimat_bersih = kalimat.replace(".", "").replace(",", "").replace("!", "").replace("?", "").lower()
    kata_kalimat = kalimat_bersih.split()
    jumlah_kemunculan = kata_kalimat.count(kata.lower())
    return jumlah_kemunculan

kalimat = input("Masukkan kalimat: ")
kata_cari = input("Masukkan kata yang ingin Anda cari: ")
jumlah_kemunculan = hitung_kemunculan_kata(kalimat, kata_cari)

print(f"Kata yang anda inputkan muncul sebanyak: {jumlah_kemunculan}")
