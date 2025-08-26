# Project calculator simple

angka_1 = int(input('Masukan nilai :'))
angka_2 = int(input('Masukan nilai :'))

def opretion():
    tambah = angka_1 + angka_2
    print(f'Hasil :{tambah}')

    kurang = angka_1 - angka_2
    print(f'Hasil :{kurang}')

    kali = angka_1 * angka_2
    print(f'Hasil :{kali}')
    
    bagi = angka_1 / angka_2
    print(f'Hasil :{bagi}')


opretion()