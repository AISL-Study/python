import pandas as pd
#파일경로,파일명 선언
Location ='C:/Users/Public/python_4'
File ='Bus.xls'
#추출 행 선언
Row = 39363
#추룰 및 변환 
data_pd = pd.read_excel('{}\{}'.format(Location,File))
data_np = pd.DataFrame.to_numpy(data_pd)

while 1:
    # 안내 문구 출력
    print("=====================================\n"
          '1. 정류장 정차 버스 찾기\n'
          '2. 버스 노선의 정차 정류장 찾기\n'
          '3. 종료 \n' 
          "=====================================\n")
        
    # 사용자 입력 받기 
    mode = input("정수값을 선택 하시오: ")
    
    # 1. 정류장 정차 버스 찾기
    if mode == '1':
        station=input("정류장 이름을 입력하세요(일부 명칭도 가능): ")

    # 사용자의 입력이 포함된 6열(정류소명)을 가진 행 찾기
        for r in range(Row):
            if station in data_np[r][6]:
                print("[{}] 정류소에 [{}] 버스가 정차합니다.".format(data_np[r][6],data_np[r][1]))
                
    # 2. 버스 노선의 정차 정류장 찾기
    if mode =='2':
        bus=input("버스 노선 명을 입력 하세요: ")

    # 사용자의 입력이 포함된 1열(노선명)을 가진 행 찾기
        for r in range(Row):
            if bus in data_np[r][1]:
                print("[{}] 버스가 [{}] 정류장에 정차합니다.".format(data_np[r][1],data_np[r][6]))
    # 3. 종료 
    if mode == '3':
        print("프로그램이 종료되었습니다.")
        break 