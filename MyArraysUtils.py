import random
import time
import insertion
import radix

arrays_list = []


def random_array(size):
    array = []
    for i in range(size):
        array.append(random.randrange(1, 100))
    return array


def generate_arrays(number):
    array_size = 10
    for i in range(0, number):
        arrays_list.append(random_array(array_size))
        array_size *= 10
        print("Generated array",i)


def perform_insertion_sort_analysis():
    for i in range(0, arrays_list.__len__()):
        arr = arrays_list[i].copy()
        print("InsertionSort array #" + (i + 1).__str__() + ". size: " + len(arrays_list[i]).__str__(), flush=True)
        start_time = time.time()
        insertion.insertion_sort(arr)
        print("Executed in " + (time.time() - start_time).__str__() + " seconds\n", flush=True)


def perform_radix_sort_analysis():
    for i in range(0, arrays_list.__len__()):
        arr = arrays_list[i].copy()
        print("RadixSort array #" + (i + 1).__str__() + ". size: " + len(arrays_list[i]).__str__(), flush=True)
        start_time = time.time()
        radix.radixsort(arr)
        print("Executed in " + (time.time() - start_time).__str__() + " seconds\n", flush=True)


def light_shuffle(arr, power=2):  # power==0 -> no shuffle
    for i in range(0, power):
        pos1 = random.randrange(0, len(arr))
        pos2 = random.randrange(0, len(arr))

        tmp = arr[pos1]
        arr[pos1] = arr[pos2]
        arr[pos2] = tmp
