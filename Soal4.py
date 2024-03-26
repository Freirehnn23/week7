def cari_kata(kalimat):
    kata_kalimat = kalimat.split()
    terpendek = terpanjang = kata_kalimat[0]

    for kata in kata_kalimat:
        if len(kata) < len(terpendek):
            terpendek = kata
        if len(kata) > len(terpanjang):
            terpanjang = kata

    return terpendek, terpanjang

kalimat_input = input("Masukan Kalimat yang Ingin Anda Masukan: ")
kata_terpendek, kata_terpanjang = cari_kata(kalimat_input)

print(f"Kata yang Pendek adalah: {kata_terpendek}, Sedangkan Kata yang Panjang Adalah: {kata_terpanjang}")

