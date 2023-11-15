def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j-1] > array[j]:
            array[j], array[j-1] = array[j-1], array[j]
            j = j - 1
    return array

array = [40, 30, 50, 10, 20]
print("Array before the Insertion Sort:", array)
sorted_array = insertion_sort(array)
print("Array after the Insertion Sort:", sorted_array)
