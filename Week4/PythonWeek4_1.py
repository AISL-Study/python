# 1. 서울시 버스 노선 정보 시스템 만들기
import pandas as pd

# 정류장 정차 버스 찾기 함수
def search_bus(station_name):
    # 엑셀 파일을 열어 노선명과 정류소명 정보 읽기
    excel_source = pd.read_excel("20190124기준_서울시_버스노선정보.xls", usecols = ['노선명', '정류소명'])
    # 검색하고자 하는 정류장이 포함된 정보 추출
    search = excel_source[excel_source['정류소명'].str.contains(station_name)]
    # 정류소명과 정차 버스 출력
    for i in range(len(search)):
        print("[{}] 정류소에 [{}] 버스가 정차합니다.".format(search.iloc[i, 1], search.iloc[i, 0]))

# 버스노선의 정차 정류장 찾기 함수
def search_station(bus_number):
    # 엑셀 파일을 열어 노선명과 정류소명 정보 읽기
    excel_source = pd.read_excel("20190124기준_서울시_버스노선정보.xls", usecols = ['노선명', '정류소명'])
    # 검색하고자하 하는 버스노선이 포함된 정보 추출
    search = excel_source[excel_source['노선명'].str.contains(bus_number)]
    # 정차 버스와 정류소명 출력
    for i in range(len(search)):
        print("[{}] 버스가 [{}] 정류장에 정차합니다.".format(search.iloc[i, 0], search.iloc[i, 1]))

while True:
    print("===================================")
    print("1. 정류장 정차 버스 찾기")
    print("2. 버스노선의 정차 정류장 찾기")
    print("3. 종료")
    print("===================================")
    # 명령 입력
    cmd = int(input("정수값을 선택하시오: "))

    # 입력받은 명령이 1인 경우
    if cmd == 1:
        # 정류장 이름 입력
        station_name = input("정류장 이름을 입력하세요(일부 명칭도 가능): ")
        search_bus(station_name)
    # 입력받은 명령이 2인 경우
    elif cmd == 2:
        # 버스 노선 입력
        bus_number = input("버스노선명을 입력하세요: ")
        search_station(bus_number)
    # 입력받은 명령이 3인 경우 - 프로그램 종료
    elif cmd == 3:
        print("프로그램을 종료합니다.")
        break