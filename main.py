# Mendefinisikan fungsi bubble sort
def bubbleSort(array):
    
    # Perulangan untuk menghitung panjang array
    for i in range(len(array)):
        
        # Swapping
        swapped = False
        
        # Perulangan untuk membandingkan elemen array
        for j in range(0, len(array) - i - 1):

            # Proses perbandingan dan swapping
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

                swapped = True
        print("Iterasi Ke-", i)
 
        # Jika array sudah terurut maka swapping tidak di lakukan
        if not swapped:
            break
# Pendeklarasian data yang akan di proses
angka = [-10, 56, 34, 0, -5]
print("Data : ", angka)

# Pemanggilan fungsi bubble sort
bubbleSort(angka)

# Menampilkan hasil
print('Hasil:')
print(angka)
