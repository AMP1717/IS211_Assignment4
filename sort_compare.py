import random
import time

def create_list(length):
    return [random.randint(0, 1e6) for _ in range(length)]

def insertion_sort(lst):
    start = time.time()
    for i in range(1, len(lst)):
        val = lst[i]
        j = i - 1
        while j >= 0 and val < lst[j] :
                lst[j + 1] = lst[j]
                j -= 1
        lst[j + 1] = val
    return time.time() - start

def shell_sort(lst):
    start = time.time()
    gap = len(lst) // 2
    while gap > 0:
        for i in range(gap, len(lst)):
            temp = lst[i]
            j = i

            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap

            lst[j] = temp
        gap //= 2
    return time.time() - start

def python_sort(lst):
    start = time.time()
    lst.sort()
    return time.time() - start

def main():
    lengths = [500, 1000, 10000]
    tests = 1
    functions = {
                "Insertion sort": insertion_sort, 
                "Shell sort": shell_sort, 
                "Python sort": python_sort
                }

    timers = {function_name: 0 for function_name in functions}

    for n in range(tests):
        for l in lengths:
            lst = create_list(l)
        
            for function_name, f in functions.items():
                timer = f(lst)
                timers[function_name] += timer
    
    for function_name, time in timers.items():
        print(f"{function_name} took {time/tests:10.7f} seconds to run, on average.")

main()