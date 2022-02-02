#사용자 입력 받기
N=int(input("가로/세로의 길이를 입력 하세요: "))
K=int(input("증가시킬 배수를 입력 하세요: "))
pixel=[list(map(int, input("픽셀 정보를 입력 하세요: ").split())) for _ in range(N)]

# 픽셀 정보 출력 
for i in range(N):
    for ii in range(K):
        for j in range(N):
            for jj in range(K):
                print(pixel[i][j], end = ' ')
        print()