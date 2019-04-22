# Given a list of integers, count and output the number of times
# each value appears as a list of space-separated integers.
def countingSort(arr):
    sorter = [0] * 100
    for val in arr:
        sorter[val] += 1
    return sorter
#  Returns an array of integers where each value is the number of
#  occurrences of the element's index value in the original array.