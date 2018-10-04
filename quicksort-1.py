# Author: Nour Benmohamed
# 11/05/2017
# program to sort a list using the quicksort method

# this function will put all the elements that are smaller than pivot in the beginning of the list and the
# elements that are bigger than pivot in the end of the list then it will insert pivot, which was initially the last
# element of the list, in between these two sections of the list and it will return the index of pivot.


def partition(the_list, p, r, compare_func):
    i = p-1
    j = p
    while j < r:
        if not compare_func(the_list[j], the_list[r]):
            j += 1
        else:
            temp = the_list[i+1]
            the_list[i+1] = the_list[j]
            the_list[j] = temp
            i += 1
            j += 1
    temp = the_list[i + 1]
    the_list[i + 1] = the_list[j]
    the_list[j] = temp
    return i+1

# This function will recursively sort the list using partition. The base case is when there is less than two elements in
# the list, it will do nothing


def quicksort(the_list, p, r, compare_func):
    if r-p < 1:
        return the_list
    else:
        q = partition(the_list, p, r, compare_func)
        quicksort(the_list, p, q-1, compare_func)
        quicksort(the_list, q+1, r, compare_func)
    return the_list

# This function will call quicksort to sort the specified list


def sort(the_list, compare_func):
    p = 0
    r = len(the_list)-1
    quicksort(the_list, p, r, compare_func)
