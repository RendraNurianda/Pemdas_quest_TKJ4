# list kosong
list_kosong = []

# list yang berisi kumpulan string
list_buah = ['Pisang', 'Nanas', 'Melon', 'Durian']

# list yang berisi kumpulan integer
list_nilai = [80, 70, 90, 60]

# list campuran berbagai tipe data
list_jawaban = [150, 33.33, 'Presiden Sukarno', False]

print(list_buah[0])
print(list_buah[2])
print(list_buah[1])
print(list_buah[3])


list_buah = ['Pisang', 'Nanas', 'Melon', 'Durian']

print(list_buah[0:1])
print(list_buah[0:2])
print(list_buah[1:3])
print(list_buah[0:-1])
print(list_buah[-1:-3])
print(list_buah[-1:3])
print(list_buah[-3:-1])
    
['Pisang']
['Pisang', 'Nanas']
['Nanas', 'Melon']
['Pisang', 'Nanas', 'Melon']
[]
[]
['Nanas', 'Melon']

list_buah = ['Pisang', 'Nanas', 'Melon', 'Durian']

print(list_buah[0:])
print(list_buah[1:])
print(list_buah[2:])
print(list_buah[3:])
print(list_buah[:0])
print(list_buah[:1])
print(list_buah[:2])
print(list_buah[:3])
print(list_buah[:4])



list_buah = ['Pisang', 'Nanas', 'Melon', 'Durian']

print(list_buah)

# ubah data pertama
list_buah[0] = 'Jeruk'

print(list_buah)

# ubah data terakhir
list_buah[-1] = 'Mangga'

print(list_buah)

# ubah data dalam range
list_buah[1:3] = ['Naga', 'Pepaya']

print(list_buah)

list_buah = ['Jeruk', 'Naga', 'Pepaya', 'Mangga']
print(list_buah)

# tambah data di belakang list
list_buah.append('Sirsak')
print(list_buah)

list_angka = [1, 2, 3, 4, 5]
print(list_angka)

# hapus satu angka di belakang
angka_yang_terhapus = list_angka.pop()

print('angka yang terhapus:', angka_yang_terhapus)
print(list_angka)


print('\n' * 2)

list_buah = ['Mangga', 'Jambu', 'Jeruk', 'Jambu']
print(list_buah)

del list_buah[1]
print(list_buah)

del list_buah[0:2]
print(list_buah)


list_buah = ['Mangga', 'Jeruk', 'Zaitun', 'Apel', 'Durian']
print(list_buah)

# urutkan secara ascending
list_buah.sort()
print(list_buah)

# membalikkan posisi item list (tidak harus berurut)
list_buah.reverse()
print(list_buah)


['Mangga', 'Jeruk', 'Zaitun', 'Apel', 'Durian']
['Apel', 'Durian', 'Jeruk', 'Mangga', 'Zaitun']
['Zaitun', 'Mangga', 'Jeruk', 'Durian', 'Apel']

