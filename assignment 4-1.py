# 서울시 버스 노선 정보 시스템 만들기

# 추가한 모듈
import pandas as pd
import os

# 전역 변수, 파일 경로 설정
global TotalIndex
TotalIndex = 39364

global df, out, np

# 파일 경로 설정 (다른 컴퓨터에 사용할 경우 경로를 바꿀 것)
# pd.read_excel('경로명\파일명', sheet_name='', usecols= ["노선명", "정류소명"])
df = pd.read_excel('C:\\내 파일\\대학 수업\\study\\6. Python_Study_4\\20190124기준_서울시_버스노선정보.xls', sheet_name='Sheet0', usecols= ["노선명", "정류소명"])
out = list(df)
np = pd.DataFrame.to_numpy(df)


# 제작한 오류
class OutOfRangeError(Exception):
    pass # 입력한 값이 범위를 초과한 경우 출력


# 시작 보드 출력
def ServiceBoard():
        print("=" * 34)
        print("""\
1. 정류장 정차 버스 찾기
2. 버스노선의 정차 정류장 찾기
3. 종료\
            """)
        print("=" * 34)


# 모드 선택 함수
def SelectionBoard():

    Mode = int(input("정수값을 선택하시오: "))
    if Mode == 1:
        return 1

    elif Mode == 2:
        return 2

    elif Mode == 3:
        return -1

    else:
        raise OutOfRangeError("Error: You've inserted a number out of range.")


# 버스 정류장 검색 함수
def GetBusNumber(InsertedStation):
    for i in range( TotalIndex - 1 ):
        if InsertedStation in np[i][1]:
            string_bus_station = "[{}] 정류소에 [{}] 버스가 정차합니다.".format(np[i][1], np[i][0])
            print(string_bus_station)


# 버스 노선명 검색 함수
def GetBusStation(InsertedBusNumber):
    for i in range( TotalIndex - 1 ):
        if np[i][0] == InsertedBusNumber:
            string_bus_number = "[{}] 버스가 [{}] 정류장에 정차합니다.".format(np[i][0], np[i][1])
            print(string_bus_number)


# 실행
try:
    while 1:
        ServiceBoard()
        ConfirmNumber = SelectionBoard()
        if ConfirmNumber == -1: 
            break

        elif ConfirmNumber == 1:
            InsertedStation = input("정류장 이름을 입력하세요(일부 명칭도 가능): ")
            GetBusNumber(InsertedStation)

        elif ConfirmNumber == 2:
            InsertedBusNumber = input("버스노선명을 입력하세요: ")
            GetBusStation(InsertedBusNumber)

    print("프로그램이 정상적으로 종료되었습니다.")



except OutOfRangeError as exception:
    print("type(exception):", type(exception))
    print("Error: You've inserted a number out of range.")

except ValueError as exception:
    print("type(exception):", type(exception))
    print("Error: You've not inserted integer.")