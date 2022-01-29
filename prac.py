# 추가한 모듈
import pandas as pd
import os

# 파일 경로 설정
df = pd.read_excel('C:\\내 파일\\대학 수업\\study\\6. Python_Study_4\\20190124기준_서울시_버스노선정보.xls', sheet_name='Sheet0', usecols= ["노선명", "정류소명"])
out = list(df)
np = pd.DataFrame.to_numpy(df)

bus = input("노선명: ")

for i in range(39364 - 1):
    if bus in np[i][1]:
        print("["+np[i][1]+"]", "버스가", "[" + np[i][0] + "]", "정류장에 정차합니다.")
