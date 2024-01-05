import random
import time


def main():
    num = 1_000
    s = []

    for value in range(num):
        s.append(random.randint(0, num))

    key = random.randint(0, num)

    start = time.time()
    location = sequential_search(s, key)
    end = time.time()

    #print(s)
    print("[Sequential Search Result]")
    print("Key value {0}: location {1}".format(key, location))
    print("Elapsed Time: {0:0.8f}ms".format((end - start) * 1_000))
    print()

    s.sort()

    start = time.time()
    location = binary_search(s, key)
    end = time.time()

    #print(s)
    print("[Binary Search Result]")
    print("Key value {0}: location {1}".format(key, location))
    print("Elapsed Time: {0:0.8f}ms".format((end - start) * 1_000))
    print()

    start = time.time()
    location = recursive_binary_search(s, key, 0, num - 1)
    end = time.time()

    #print(s)
    print("[Recursive Binary Search Result]")
    print("Key value {0}: location {1}".format(key, location))
    print("Elapsed Time: {0:0.8f}ms".format((end - start) * 1_000))
    print()


def sequential_search(s, key):
    num = len(s)
    location = 0

    # 코딩을 추가하세요.

    return location


def binary_search(s, key):
    num = len(s)
    low = 0
    high = num - 1
    location = -1

    # 코딩을 추가하세요.

    return location


def recursive_binary_search(s, key, low, high):
    mid = round((low + high) / 2)

    # 코딩을 추가하세요.


if __name__ == "__main__":
    main()
