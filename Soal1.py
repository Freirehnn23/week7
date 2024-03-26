def cek_anagram(word1, word2):

    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()

    if len(word1) != len(word2):
        return False

    letter_count = {}
    for letter in word1:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    for letter in word2:
        if letter in letter_count:
            letter_count[letter] -= 1
        else:
            return False

    for count in letter_count.values():
        if count != 0:
            return False

    return True

kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

if cek_anagram(kata1, kata2):
    print("Kedua kata adalah anagram.")
else:
    print("Kedua kata bukan anagram.")
