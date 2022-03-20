abjad = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] 

key = int(input('Masukkan cipher key yang anda inginkan (misal 5): ')) 


def enkripsi_dekripsi(kalimat,cipher_key): 
  kalimat = kalimat.upper() 
  hasil_encode = ''  
  for karakter in kalimat:
    if karakter in abjad: 
      index_lama = abjad.index(karakter) 
      index_baru = (index_lama + cipher_key )
      abjad_baru = abjad[index_baru]  
      hasil_encode = hasil_encode + abjad_baru 
    else:
       hasil_encode = hasil_encode + ' ' 
  return hasil_encode 

kalimat = input('Masukkan kalimat yang ingin dienkripsi ') 
# ENKRIPSI
kalimat_hasil = encode(kalimat,key) 
print('Kalimat yang di inginkan : ',kalimat)
print('Hasil enkripsi:' , kalimat_hasil) 
# DEKRIPSI (dengan enkripsi ulang menggunakan nilai minus key)
kalimat_awal = encode(kalimat_hasil,-key)
print('Jika hasil dienkripsi ulang menggunakan nilai negatif dari cipher key sebelumnya maka kalimat hasilnya adalah:',-key, 'adalah', kalimat_awal)
