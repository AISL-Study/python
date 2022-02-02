def hanoi(n, A,B,C): 
    #원반이 1개 이면 A장대에서 C장대로 이동 
    if n == 1: 
        print(A, C) 
        return
    # 원반 n - 1개를 A장대에서 B 장대로 이동  
    hanoi(n - 1,A,C,B) 
    #가장 큰 원반을 A 장대에서 C 장대로 이동
    print(A,C) 
    # 원반 n-1개를 B 장대에서 C 장대로 이동 
    hanoi(n - 1, B,A,C)

N=int(input("원반의 개수를 입력하세요: "))
print(2**N-1)
hanoi(N,1,2,3)
