from tabulate import tabulate

#Validasi angka
def string_validation(title):
    while True:
        a = input(title)
        if a.isalpha() == True:
            break
        else:
                print('Silahkan inputkan hanya text')
    return a.capitalize()
    
#Validasi text
def integer_validation(title):
    while True:
        a = input(title)
        try:
            a = int(a)
            break
        except:
            print('Yang anda inputkan bukan bilangan')
    return a

#Tampilkan buah
def show(database, header=['index', 'name', 'stock', 'price']):
    #menampilkan data dalam format tabulasi
    print(tabulate(database, headers=header, tablefmt="simple_grid"))

def add(database):
    name = string_validation('Masukkan Nama Buah: ')
    stock = integer_validation('Masukkan Stock Buah: ')
    price = integer_validation('Masukkan Harga Buah: ')

    #Validasi data, jika sudah ada tambahkan yg akan diganti, jika belum tambahkan data lalu 
    for id, buah in enumerate(database):
        if name in buah:
            database[id] = [id, name, stock, price]
            break
    else:
        database.append([id+1, name, stock, price])
        
    # Tampilkan data
    show(database)
                            
def delete(database):
    #Menampilkan database terbaru
    show(database)

    #User input
    idx = integer_validation('Masukkan index buah yang ingin dihapus: ')

    for buah in database:
        if idx == buah[0]:
            del database[idx]
            break
    else:
        print('Buah yang anda cari tidak ada')

    # Memperbarui index
    for id, buah in enumerate(database):
        if id != buah[0]:
            database[id][0] = id

    show(database)

#def buy():

def inputBuah(nama, stock, harga):
    """Fungsi meminta user untuk input jumlah buah 
    dan menghitung harganya.

    Args:
        nama (String): Nama buah yang akan dibeli
        stock (Integer): Stock buah yang akan dibeli
        harga (Integer): Harga buah per kg

    Returns:
        nBuah (Integer): Jumlah buah yang dipesan 
        hargaBuah (Integer): Total harga buah
    """
    while True:
        # Input jumlah buah
        nBuah = int(input(f'Masukkan jumlah {nama}: '))

        # Membandingkan antara jumlah permintaan dengan stock
        if nBuah > stock:
            print(f'Jumlah terlalu banyak, stock tersisa {stock} buah')
            continue

        # Berhenti minta input, ketika jumlah permintaan terpenuhi
        break

    # Hitung total harga untuk buah tersebut
    hargaBuah = nBuah * harga

    return nBuah, hargaBuah
