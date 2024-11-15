def process_test_cases():
    T = int(input())
    for _ in range(T):
        N,M = map(int, input().split())
        if N>M:
            print(N-M)
        else:
            print(0)
process_test_cases()
