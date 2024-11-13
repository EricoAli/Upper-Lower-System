kalimat = input("Masukkan kalimat yang ingin dirapikan: ")

def mengubah_case(kata):
    hitung_upper = sum(1 for char in kata if char.isupper())
    hitung_lower = sum(1 for char in kata if char.islower())
    if hitung_upper > hitung_lower:
        return kata.upper()
    elif hitung_lower > hitung_upper:
        return kata.lower()
    else:
        if kata[-1].isupper():
            return kata.upper()
        else:
            return kata.lower()

def mengubah_kalimat(kalimat):
    kata_kata = kalimat.split()
    hasil = [mengubah_case(kata) for kata in kata_kata]
    return ' '.join(hasil)

print("Hasil:", mengubah_kalimat(kalimat))