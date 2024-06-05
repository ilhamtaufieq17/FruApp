nApel = int(input('Masukkan Jumlah Apel: '))
nJeruk = int(input('Masukkan Jumlah Jeruk: '))
nAnggur = int(input('Masukkan Jumlah Anggur: '))

#Harga buah
hargaApel = 10000
hargaJeruk = 15000
hargaAnggur = 20000

#Hitung total harga per buah
totalHargaApel = nApel * hargaApel
totalHargaJeruk = nJeruk * hargaJeruk
totalHargaAnggur = nAnggur * hargaAnggur

#Total keseluruhan
totalBelanja = totalHargaApel + totalHargaJeruk + totalHargaAnggur

print(f'''
Detail Belanja
      
Apel = {nApel} x {hargaApel} = {totalHargaApel}
Jeruk = {nJeruk} x {hargaJeruk} = {totalHargaJeruk}
Anggur = {nAnggur} x {hargaAnggur} = {totalHargaAnggur}

Total: {totalBelanja}
''')
