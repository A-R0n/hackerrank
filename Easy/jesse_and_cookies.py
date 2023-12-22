import heapq
## K is the sugar threshold
K = 9
## A is all of our sugar objects -cookies-
## represented as integer values
A = [2,7,3,6,4,6]

def get_least_sugary_cookie() -> int:
    return heapq.heappop(A)

def get_next_least_sugary_cookie():
    ## after the smallest item gets popped, the data structure reorganizes itself 
    ## using a bubble sort
    ## so that the new smallest is at index 0
    return get_least_sugary_cookie()

def push_combined_cookie(item: int):
    heapq.heappush(A, item)

def combine_cookies(l0: int,l1: int) -> int:
    return l0 + (2*l1)

def check_if_cookies_sweet_enough() -> bool:
    if all(i >= K for i in A):
        return True
    return False

def determine_min_num_operations() -> int:
    count = 0
    cookiesSweetEnough = check_if_cookies_sweet_enough()
    while not cookiesSweetEnough:
        count += 1
        l0 = get_least_sugary_cookie()
        l1 = get_next_least_sugary_cookie()
        sweetness = combine_cookies(l0,l1)
        push_combined_cookie(sweetness)
        cookiesSweetEnough = check_if_cookies_sweet_enough()
    return count

def heapify_A():
    heapq.heapify(A)

def cookies():
    ## by converting the list into a min heap,
    ## we are promised that the first element is the smallest
    ## and the next two elements are 2nd and 3rd smallest
    ## (not necessarily in that order)
    heapify_A()
    min_num_operations = determine_min_num_operations()
    print(min_num_operations)

if __name__ == '__main__':
    cookies()