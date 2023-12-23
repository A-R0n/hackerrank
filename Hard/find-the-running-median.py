a = [12, 4, 5, 3, 8, 7]
b = []

def isHeapOdd():
    if len(b) % 2 == 1:
        return True
    return False

def find_the_running_median():
    for _ in range(len(a)):
        first_elem = a.pop(0)
        # print(f'first_elem {first_elem}')
        # sys.exit()
        # heapq.heappush(b, first_elem)
        b.append(first_elem)
        b.sort()
        # print(f'heap looks like this {b}')
        if isHeapOdd():
            middle_idx = len(b)//2
            median_num = b[middle_idx]
            print(float(median_num))
        else:
            left_middle_idx = len(b)//2 - 1
            right_middle_idx = len(b)//2
            left_middle_num = b[left_middle_idx]
            right_middle_num = b[right_middle_idx]
            median_num = (left_middle_num + right_middle_num)/2
            print(float(median_num))

if __name__ == '__main__':
    find_the_running_median()