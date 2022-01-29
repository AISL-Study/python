# 서울시 버스 노선 정보 시스템 만들기


# 추가한 모듈
import pandas as pd
import os

# 파일 경로 설정
df = pd.read_excel('C:\\내 파일\\대학 수업\\study\\6. Python_Study_4\\20190124기준_서울시_버스노선정보.xls', sheet_name='Sheet0')
out = list(df.columns)


# 제작한 오류
class OutOfRangeError(Exception):
    pass



def ServiceBoard():
        print("=" * 34)
        print("""\
1. 정류장 정차 버스 찾기
2. 버스노선의 정차 정류장 찾기
3. 종료\
            """)
        print("=" * 34)


def SelectionBoard():

    Mode = int(input("정수값을 선택하시오: "))
    if Mode == 1:
        return 1

    elif Mode == 2:
        return 2

    elif Mode == 3:
        return -1

    else:
        raise OutOfRangeError("Error: You've entered a number out of range.")
        


# 실행
try:

    # 파일 경로 설정
    df = pd.read_excel('C:\\내 파일\\대학 수업\\study\\6. Python_Study_4\\20190124기준_서울시_버스노선정보.xls', sheet_name='Sheet0', usecols= ["노선명", "정류소명"])
    out = list(df)
    np = pd.DataFrame.to_numpy(df)

    while 1:
        ServiceBoard()
        ConfirmNumber = SelectionBoard()
        if ConfirmNumber == -1: 
            break

        elif ConfirmNumber == 1:
            InsertedStation = input("정류장 이름을 입력하세요(일부 명칭도 가능): ")
            for i in range(39364 - 1):
                if np[i][1] in InsertedStation:
                    print("["+InsertedStation+"]", "버스가", "[" + np[i][0] + "]", "정류장에 정차합니다.")
                    raise NotImplementedError

        elif ConfirmNumber == 2:
            InsertedBusNumber = input("버스노선명을 입력하세요: ")
            for i in range( 39364 - 1 ):
                if np[i][0] == InsertedBusNumber:
                    print("["+InsertedBusNumber+"]", "버스가", "[" + np[i][1] + "]", "정류장에 정차합니다.")


    print("프로그램이 정상적으로 종료되었습니다.")

except OutOfRangeError as exception:
    print("Error: You've entered a number out of range.")