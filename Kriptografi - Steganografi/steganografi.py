from stegano import lsb

def enkripsi_otp_stegano(teks, kunci, path_gambar_input, path_gambar_output):
    # Memeriksa panjang kunci dengan teks
    if len(kunci) != len(teks):
        raise ValueError("Error: Panjang kunci harus sama dengan panjang teks.")

    # Enkripsi teks menggunakan kunci yang diberikan
    teks_terenkripsi = ''.join(chr(((ord(a) + ord(b)) % 95) + 32) for a, b in zip(teks, kunci))
    print("Teks enkripsi OTP : ", teks_terenkripsi)
    print("Teks akan dimasukkan ke gambar : ", path_gambar_input)

    # Sembunyikan teks terenkripsi dalam gambar
    rahasia = lsb.hide(path_gambar_input, teks_terenkripsi)
    rahasia.save(path_gambar_output)
    print("Gambar setelah menyisipkan teks : ", path_gambar_output)

def dekripsi_stegano_otp(path_gambar_output, kunci):
    # Ambil teks terenkripsi dari gambar
    teks_terenkripsi = lsb.reveal(path_gambar_output)

    # Dekripsi teks menggunakan kunci yang diberikan
    teks_didekripsi = ''.join(chr(((ord(a) - ord(b) - 32) % 95) + 32) for a, b in zip(teks_terenkripsi, kunci))
    return teks_didekripsi

path_gambar_input = 'img/jaehyun.jpeg'  # Ganti dengan path gambar Anda
path_gambar_output = 'img/jaehyun_tersembunyi.jpeg'  # Ganti dengan path output yang diinginkan

# Input Teks dan Key
teks_rahasia = input("Masukkan teks rahasia: ")
kunci = input("Masukkan kunci: ")

# Mulai Enkripsi
enkripsi_otp_stegano(teks_rahasia, kunci, path_gambar_input, path_gambar_output)
print("Enkripsi selesai.")

# Dekripsi
teks_didekripsi = dekripsi_stegano_otp(path_gambar_output, kunci)
print(f"Pesan yang didekripsi: {teks_didekripsi}")
