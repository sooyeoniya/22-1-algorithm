import time


def main():
    num = 10

    start = time.time()
    result1 = iterative_fibonacci(num)
    end = time.time()

    print("[Iterative Fibonacci]")
    print("Num {0} : Fibonacci Number {1}".format(num, result1))
    print("Elapsed Time: {0:08f}s".format((end - start)))
    print()

    start = time.time()
    result2 = recursive_fibonacci(num)
    end = time.time()

    print("[Recursive Fibonacci]")
    print("Num {0} : Fibonacci Number {1}".format(num, result2))
    print("Elapsed Time: {0:08f}s".format((end - start)))
    print()


def iterative_fibonacci(num):
    pass # pass 라는 본 라인은 추후 삭제하세요.    
	


def recursive_fibonacci(num):
    pass # pass 라는 본 라인은 추후 삭제하세요.    
    # 코딩을 추가하세요.


if __name__ == "__main__":
    main()
