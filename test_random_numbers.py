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
    print("Done")

    if not generateArraysOnly:
        print("Starting test with InsertionSort")
        mut.perform_insertion_sort_analysis()

        print("\nStarting test with RadixSort")
        mut.perform_radix_sort_analysis()

    if "-flush_arrays" in sys.argv:
        print("Flushing used arrays:")
        for i in range(mut.arrays_list.__len__()):
            print(mut.arrays_list[i])

    return


if __name__ == '__main__':
    main()
