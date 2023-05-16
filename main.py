def bubbleSort(array):
    for i in range(len(array)):
        swapped = False
        for j in range(0, len(array) - i - 1):

            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

                swapped = True
        print("Iterasi Ke-", i)

        if not swapped:
            break
angka = [-10, 56, 34, 0, -5]
print("Data : ", angka)

bubbleSort(angka)

print('Hasil:')
print(angka)
