# steganografi
## Profil
| #               | Biodata                 |
| --------------- | ----------------------- |
| **Nama**        | Nabilah Ananda Putri    |
| **NIM**         | 312110263               |
| **Kelas**       | TI.21.A.1               |
| **Mata Kuliah** | Kriptografi             |
### Keterangan
- Library dan Import
  ```py
  from stegano import lsb
  ```
  
  - Program `stegano` untuk menyisipkan dan mengungkapkan pesan pada gambar menggunakan metode LSB.
    
- Fungsi `enkripsi_otp_stegano` memiliki tujuan untuk melakukan enkripsi teks menggunakan metode One-Time Pad (OTP) dan menyisipkannya ke dalam gambar menggunakan steganografi dengan metode Least Significant Bit (LSB). Berikut adalah langkah-langkah yang diambil oleh fungsi ini:

- Pemeriksaan Panjang Kunci dan Teks:
   ```py
      if len(kunci) != len(teks):
        raise ValueError("Error: Panjang kunci harus sama dengan panjang teks.")
  ```
   
  - Fungsi memeriksa apakah panjang kunci `(kunci)` sama dengan panjang teks `(teks)`. Jika tidak sama, maka fungsi akan melempar ValueError.
  - Tujuan dari pemeriksaan ini adalah memastikan bahwa panjang kunci yang digunakan untuk enkripsi sesuai dengan panjang teks yang akan dienkripsi.
    
- Enkripsi Menggunakan OTP:
  ```py
      teks_terenkripsi = ''.join(chr(((ord(a) + ord(b)) % 95) + 32) for a, b in zip(teks, kunci))
    print("Teks enkripsi OTP : ", teks_terenkripsi)
    print("Teks akan dimasukkan ke gambar : ", path_gambar_input)
  ```
  
  - Fungsi kemudian melakukan enkripsi teks `(teks)` menggunakan kunci OTP `(kunci)`.
  - Setiap karakter dienkripsi menggunakan rumus `(ord(a) + ord(b)) % 95 + 32`.
  - Hasil enkripsi disimpan dalam variabel `teks_terenkripsi`.

- Sembunyikan Teks dalam Gambar:
  ```py
      rahasia = lsb.hide(path_gambar_input, teks_terenkripsi)
    rahasia.save(path_gambar_output)
    print("Gambar setelah menyisipkan teks : ", path_gambar_output)
  ```

  - Teks yang telah dienkripsi `(teks_terenkripsi)` kemudian disisipkan ke dalam gambar menggunakan metode LSB dari library stegano.
  - Gambar hasil disimpan dengan path yang diberikan oleh parameter `path_gambar_output`.

- Fungsi `dekripsi_stegano_otp` bertanggung jawab untuk mengungkapkan (dekripsi) teks yang telah disisipkan ke dalam gambar menggunakan steganografi metode Least Significant Bit (LSB) dan teks yang telah dienkripsi dengan One-Time Pad (OTP). Berikut adalah penjelasan langkah-langkahnya:

- Fungsi `dekripsi_stegano_otp`
  ```py
  def dekripsi_stegano_otp(path_gambar_output, kunci):
    # Ambil teks terenkripsi dari gambar
    teks_terenkripsi = lsb.reveal(path_gambar_output)

    # Dekripsi teks menggunakan kunci yang diberikan
    teks_didekripsi = ''.join(chr(((ord(a) - ord(b) - 32) % 95) + 32) for a, b in zip(teks_terenkripsi, kunci))
    return teks_didekripsi
  ```

- Ambil Teks Terenkripsi dari Gambar:
  ```py
  teks_terenkripsi = lsb.reveal(path_gambar_output)
  ```
  
  - Fungsi menggunakan `lsb.reveal` untuk mengambil teks terenkripsi dari gambar yang telah dimodifikasi menggunakan metode LSB.
  - Hasilnya disimpan dalam variabel `teks_terenkripsi`.

- Dekripsi Teks Menggunakan OTP:
  ```py
   teks_didekripsi = ''.join(chr(((ord(a) - ord(b) - 32) % 95) + 32) for a, b in zip(teks_terenkripsi, kunci))
  ```
  - Teks terenkripsi kemudian didekripsi menggunakan kunci OTP yang diberikan.
  - Setiap karakter didekripsi menggunakan rumus `(ord(a) - ord(b) - 32) % 95 + 32`.
  - Hasil dekripsi disimpan dalam variabel `teks_didekripsi`.

- Pengembalian Hasil Dekripsi:
  ```py
   return teks_didekripsi
  ```
  - Hasil dekripsi kemudian dikembalikan oleh fungsi.

- Penggunaan Fungsi pada Main Program
  ```py
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
  ```
  
- Pada program utama:
 - `path_gambar_input` dan `path_gambar_output` menyimpan path gambar input dan output.
 - Pengguna diminta untuk memasukkan teks rahasia dan kunci.
 - Fungsi `enkripsi_otp_stegano` digunakan untuk menyisipkan teks rahasia ke dalam gambar.
 - Setelah itu, hasil enkripsi diselesaikan dan dicetak.
 - Fungsi `dekripsi_stegano_otp` kemudian digunakan untuk mengungkapkan teks dari gambar yang telah dimodifikasi, dengan menggunakan kunci yang sama dengan kunci pada saat enkripsi.
 - Hasil dekripsi dicetak sebagai pesan yang didekripsi.

### Hasil
- Hasil Kode
<img width="363" alt="ss1" src="https://github.com/nabilahap/steganografi/assets/92380488/87dc2625-b937-426f-bfb2-1d20342d9642">

- Gambar
<img width="363" alt="ss1" src="https://github.com/nabilahap/steganografi/assets/92380488/0592d20c-2ba7-4dfb-8a21-807e61632460)">


- Gambar Tersembunyi
<img width="363" alt="ss1" src="https://github.com/nabilahap/steganografi/assets/92380488/6a549826-df55-44b0-881a-feb4034b216e)">


### Terima Kasih
