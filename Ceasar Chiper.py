abjad = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] #membuat aray yang berisi abjad A sampai Z

key = int(input('Masukkan cipher key yang anda inginkan (misal 5): ')) #menentukan key yang akan digunakan dalam metode caesar cipher


def enkripsi_dekripsi(kalimat,cipher_key): # membuat fungsi yang bertujuan untuk menerapkan caesar cipher
  kalimat = kalimat.upper() # membuat variable kalimat dan berisi huruf kecil
  hasil_encode = ''  # membuat variable string untuk memuat hasil enkripsi
  for karakter in kalimat: # membuat perulangan untuk mengenkripsi kalimat
    if karakter in abjad: 
      index_lama = abjad.index(karakter) # index lama adalah index pada array abjad
      index_baru = (index_lama + cipher_key ) % len(abjad) # membuat index baru dengan menggeser sejauh key yang telah ditentukan dengan batas index 26
      abjad_baru = abjad[index_baru] # membuat abjad baru dari index baru yang telah diperoleh 
      hasil_encode = hasil_encode + abjad_baru # membuat variable baru yang memuat hasil enkripsi
    else:
       hasil_encode = hasil_encode + ' ' # jika karakter yang dimasukkan bukan berasal dari abjad A - Z maka akan menjadi spasi
  return hasil_encode # mengembalikan hasil enkripsi

kalimat = input('Masukkan kalimat yang ingin dienkripsi ') # memasukkan kalimat yang akan di enkripsi
# ENKRIPSI
kalimat_hasil = encode(kalimat,key) # memanggil fungsi Caesar_cipher untuk mengenkripsi kalimat
print('Kalimat yang di inginkan : ',kalimat)
print('Hasil enkripsi:' , kalimat_hasil) # Menampilkan hasil enkripsi
# DEKRIPSI (dengan enkripsi ulang menggunakan nilai minus key)
kalimat_awal = encode(kalimat_hasil,-key) # memanggil fungsi Caesar_cipher untuk mendekripsi kalimat
print('Jika hasil dienkripsi ulang menggunakan nilai negatif dari cipher key sebelumnya maka kalimat hasilnya adalah:',-key, 'adalah', kalimat_awal)
 # Menampilkan hasil dekripsi
