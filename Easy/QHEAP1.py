## url --> https://www.hackerrank.com/challenges/qheap1/problem?isFullScreen=true

# This question is designed to help you get a better understanding of basic heap operations.

# There are  types of query:

# "1 v " - Add an element  to the heap.
# "2 v " - Delete the element  from the heap.
# "3" - Print the minimum of all the elements in the heap.
# NOTE: It is guaranteed that the element to be deleted will be there in the heap. Also, at any instant, only distinct elements will be in the heap.

# Input Format

# The first line contains the number of queries, Q.
# Each of the next Q lines contains one of the  types of query.

# Constraints


# Output Format

# For each query of type 3, print the minimum value on a single line.
import heapq
my_heap = []
elems_to_delete = set()
ERROR_MESSAGE = 'unknown query type'

def format_as_list() -> list:
    return list(map(int,input().split()))

def add_elem_to_heap(elem: int):
    heapq.heappush(my_heap,elem)

def add_elem_to_delete_from_heap(elem: int):
    elems_to_delete.add(elem)

def discad_elem_to_delete_from_heap(elem: int):
    elems_to_delete.discard(elem)

def remove_smallest_elem():
    heapq.heappop(my_heap)

def delete_elem_from_heap():
    remove_smallest_elem()

def print_min_value():
    print(my_heap[0])

def print_error():
    print(ERROR_MESSAGE)

def qheap1():
    stdin = int(input())
    for _ in range(stdin):
        stdin_list = format_as_list()
        query_type = stdin_list[0]
        if query_type == 1:
            add_elem_to_heap(stdin_list[1])
        elif query_type==2:
            add_elem_to_delete_from_heap(stdin_list[1])
        elif query_type==3:
            # delete all the item that will be present in the set.
            while my_heap[0] in elems_to_delete:
                discad_elem_to_delete_from_heap(my_heap[0])
                delete_elem_from_heap()
            print_min_value()
        else:
            print_error()

if __name__ == '__main__':
    qheap1()