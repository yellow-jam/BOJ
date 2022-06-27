def main():
    M, N = [int(w) for w in input().split(" ")]
    is_prime = [True for i in range(N + 1)]
    is_prime[1] = False
    for i in range(1, int(N ** 0.5) + 1):
        if(is_prime[i]):
            for j in range(i * i, N + 1, i):
                is_prime[j] = False         #자연수 목록에서 배수를 제거

    for i in range(M, N + 1):
        if(is_prime[i]):
            print(i)
if __name__ == "__main__":
    main()
