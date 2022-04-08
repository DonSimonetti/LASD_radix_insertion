import sys
import MyArraysUtils as mut


def main():
    print(sys.version)

    numArrays = sys.argv[1]

    generateArraysOnly = False
    for i in range(1, len(sys.argv)):
        if str(sys.argv[i]) == "-generate_arrays_only":
            generateArraysOnly = True
            print("Generating arrays only")

    print("Generating", numArrays, "arrays..")
    mut.generate_arrays(int(numArrays))
    print("Sorting and shuffling..")
    for i in range(mut.arrays_list.__len__()):
        mut.arrays_list[i]=sorted(mut.arrays_list[i])
        mut.light_shuffle(mut.arrays_list[i],4 ** (i + 1))
    print("Done")

    if not generateArraysOnly:
        print("Starting test with InsertionSort using almost sorted arrays")
        mut.perform_insertion_sort_analysis()

        print("\nStarting test with RadixSort using almost sorted arrays")
        mut.perform_radix_sort_analysis()

    if "-flush_arrays" in sys.argv:
        print("Flushing used arrays:")
        for i in range(mut.arrays_list.__len__()):
            print(mut.arrays_list[i])

    return


if __name__ == '__main__':
    main()