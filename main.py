import brute_force
import merge_sort as merge_sort
import time
import random

def measure_time(func, arr):
    start_time = time.perf_counter()
    func(arr)
    end_time = time.perf_counter()
    return end_time - start_time

def main():
    input_sizes = [100, 200, 400, 800, 1600, 3800, 6400, 12800, 25600]

    for n in input_sizes:
        arr = [random.randint(1, 1000) for _ in range(n)]  # diziyi burada oluşturuyoruz
        
        # Her iki fonksiyon da aynı diziyi kullanacak şekilde kopyalıyoruz
        arr_for_bf = arr.copy()  
        arr_for_ms = arr.copy()
        
        # Brute force algoritmasının süresi
        bf_time = measure_time(brute_force.find_max_sum_indices, arr_for_bf)
        print(f"brute_force (n={n}) süresi: {bf_time:.6f} saniye")
        
        # Merge sort algoritmasının süresi
        ms_time = measure_time(merge_sort.merge_sort, arr_for_ms)
        print(f"merge_sort (n={n}) süresi: {ms_time:.6f} saniye")
        print('-' * 50)

if __name__ == "__main__":
    main()
