print('Selamat Datang di Pasar Buah')

#Stok buah
stockApel = 10
stockJeruk = 8
stockAnggur = 15

#Harga buah
hargaApel = 10000
hargaJeruk = 15000
hargaAnggur = 20000

#Iput Jumlah apel
while True:
    #input jumlah
    nApel = int(input('Masukkan Jumlah Apel: '))
    #Membandingkan input dengan stock
    if nApel > stockApel:
        print (f'Jumlah terlalu banyak, stock tersisa {stockApel}buah')
        continue
    #Berhenti ketika stock > permintaan
    break

while True:
    #input jumlah
    nJeruk = int(input('Masukkan Jumlah Jeruk: '))
    #Membandingkan input dengan stock
    if nJeruk > stockApel:
        print (f'Jumlah terlalu banyak, stock tersisa {stockJeruk}buah')
        continue
    #Berhenti ketika stock > permintaan
    break

while True:
    #input jumlah
    nAnggur = int(input('Masukkan Jumlah Anggur: '))
    #Membandingkan input dengan stock
    if nAnggur > stockAnggur:
        print (f'Jumlah terlalu banyak, stock tersisa {stockAnggur}buah')
        continue
    #Berhenti ketika stock > permintaan
    break

#nApel = int(input('Masukkan Jumlah Apel: '))
#nJeruk = int(input('Masukkan Jumlah Jeruk: '))
#nAnggur = int(input('Masukkan Jumlah Anggur: '))

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

#Proses Pembayaran
while True:
    #Input pembayaran
    bayar = int(input('Masukkan Jumlah Pembayaran: '))

    #Hitung selisih
    selisih = totalBelanja - bayar

    #Bandingkan pembayaran dengan total belanja
    if selisih > 0:
        print(f'Uang anda kurang sebesar Rp.{selisih}')
        continue
    #Kembalian
    else:
        print(f'Terima kasih, uang kembalian anda sebesar Rp. {abs(selisih)}')
        break