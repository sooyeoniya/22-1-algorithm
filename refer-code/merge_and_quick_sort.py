import random
import time


def main():

    ###################
    #   Create List   #
    ###################

    n = 100
    s = []

    for i in range(n):
        s.append(random.randint(0, n))

    s1 = s.copy()
    s2 = s.copy()
    s.sort()

    # print("s1:", s1)  # merge sort
    # print("s2:", s2)  # quick sort
    # print()

    ##################
    #   Merge Sort   #
    ##################

    start = time.perf_counter()
    merge_sort(s=s1, low=0, high=len(s2) - 1)
    end = time.perf_counter()
    print("[Merge Sort Result]")
    print("Elapsed Time: {0:0.4f}ms".format((end - start) * 1_000))
    print("s1:", s1)
    print("Correct:", s == s1)
    print()

    ##################
    #   Quick Sort   #
    ##################

    start = time.perf_counter()
    quick_sort(s=s2, low=0, high=len(s2) - 1)
    end = time.perf_counter()
    print("[Quick Sort Result]")
    print("Elapsed Time: {0:0.4f}ms".format((end - start) * 1_000))
    print("s2:", s2)
    print("Correct:", s == s2)
    print()

    #############
    #   TRIAL   #
    #############

    TRIAL = 100
    total_elapsed_time_merge_sort = 0
    total_elapsed_time_quick_sort = 0

    print("[progressing] - TRIAL: {}".format(TRIAL))
    print(">" * (TRIAL // (TRIAL // 20)))

    for trial in range(TRIAL):
        # Create list
        n = 5000
        s = []
        for i in range(n):
            s.append(random.randint(0, n))

        s1 = s.copy()
        s2 = s.copy()

        # Merge Sort
        start = time.perf_counter()
        merge_sort(s=s1, low=0, high=len(s2) - 1)
        end = time.perf_counter()
        total_elapsed_time_merge_sort += end - start

        # Quick Sort
        start = time.perf_counter()
        quick_sort(s=s2, low=0, high=len(s2) - 1)
        end = time.perf_counter()
        total_elapsed_time_quick_sort += end - start

        if TRIAL >= 20 and (trial + 1) % (TRIAL // 20) == 0:
            print(">", end="", flush=True)

    print()
    print("Merge Sort - Elapsed Time: {:.5}s".format(total_elapsed_time_merge_sort))
    print("Quick Sort - Elapsed Time: {:.5}s".format(total_elapsed_time_quick_sort))


def merge_sort(s, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(s, low, mid)
        merge_sort(s, mid + 1, high)
        merge(s, low, mid, high)


def merge(s, low, mid, high):
    tmp = [0] * (high - low + 1)
    i = low
    j = mid + 1
    t = 0

    # 코딩을 추가하세요.


def quick_sort(s, low, high):
    if low < high:
        pivot = partition(s, low, high)
        quick_sort(s, low, pivot - 1)
        quick_sort(s, pivot + 1, high)


def partition(s, low, high):
    x = s[high]
    i = low - 1

    # 코딩을 추가하세요.

    return i


if __name__ == "__main__":
    main()
