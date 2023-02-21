import time
import random


def sequential_search(lst, item):
    start = time.time()
    for x in lst:
        if x == item:
            return True, time.time() - start
    return False, time.time() - start
        


def ordered_sequential_search(lst, item):
    start = time.time()
    for x in lst:
        if x == item:
            return True, time.time() - start
        if x > item:
            return False, time.time() - start
    return False, time.time() - start


def binary_search_iterative(lst, item):
    start = time.time()
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == item:
            return True, time.time() - start
        elif item < lst[mid]:
            right = mid - 1
        else:
            left = mid + 1
    
    return False, time.time() - start


def binary_search_recursive(lst, item):
    start = time.time()
    if len(lst) == 0:
        return False, time.time() - start

    mid = len(lst) // 2
    if lst[mid] == item:
        return True, time.time() - start

    if item < lst[mid]:
        result, rec_time = binary_search_recursive(lst[:mid], item)
        return result, rec_time + time.time() - start

    result, rec_time = binary_search_recursive(lst[mid + 1:], item)    
    return result, rec_time + time.time() - start


def create_list(length):
    return sorted([random.randint(0, 1e6) for _ in range(length)])

def main():
    lengths = [500, 1000, 10000]
    tests = 100
    functions = {
                "Sequential search": sequential_search, 
                "Ordered sequential search": ordered_sequential_search, 
                "Binary iterative search": binary_search_iterative, 
                "Binary recursive search": binary_search_recursive
                }

    timers = {function_name: 0 for function_name in functions}

    for n in range(tests):
        for l in lengths:
            lst = create_list(l)
        
            for function_name, f in functions.items():
                ret_val, timer = f(lst, -1)
                timers[function_name] += timer
    
    for function_name, time in timers.items():
        print(f"{function_name} took {time/tests:10.7f} seconds to run, on average.")

main()