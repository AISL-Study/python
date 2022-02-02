list_odd=[3,5,7,9]
list_even=[2,4,6,8]
while 1:
    print(
    "-----------------------------------------------------\n"
    '\"구구단을 외자, 구구단을 외자" 프로그램을 실행합니다.\n'
    "1. 홀수 구구단\n"
    "2. 짝수 구구단\n"
    "3. 종료\n"
    "-----------------------------------------------------\n"
    )
    mode=input("숫자를 입력하세요:")
  
    if mode == '1':
        for i in list_odd:
              print("{}단".format(i))
              for j in range(1,10):           
                print("{} * {} = {}".format(i,j,i*j))
    elif mode == '2':
        for i in list_even:
              print("{}단".format(i))
              for j in range(1,10):           
                print("{} * {} = {}".format(i,j,i*j))
    elif mode == '3':
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못 입력하셨습니다. 1~3 번 숫자를 입력하세요.")           
            
