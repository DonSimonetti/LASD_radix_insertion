import sys
import MyArraysUtils as mut


print(sys.version)

num_arrays = sys.argv[1]

generate_arrays_only = False
if "-generate_arrays_only" in sys.argv:
    generate_arrays_only = True
    print("Generating arrays only")

print("Generating", num_arrays, "arrays..")
mut.generate_arrays(int(num_arrays))
print("Done")

if not generate_arrays_only:
    print("Starting test with InsertionSort")
    mut.perform_insertion_sort_analysis()

    print("\nStarting test with RadixSort")
    mut.perform_radix_sort_analysis()

if "-flush_arrays" in sys.argv:
    print("Flushing used arrays:")
    for i in range(mut.arrays_list.__len__()):
        print(mut.arrays_list[i])
