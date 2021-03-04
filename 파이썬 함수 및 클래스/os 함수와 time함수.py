# 경로내 파일 또는 폴더 조회(윈도우 dir)
import glob
print(glob.glob("*.py")) # 지금 .py된 모든 파일 보여줘

# os : 운영체제에서 기본으로 제공하는 기능
import os
print(os.getcwd()) # 현재 디렉토리 보여줘

folder = "smaple_dir"

if os.path.exists(folder):   # 만약 sample_dir 이라는 폴더가 있으면 이구문을 실행
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print("폴더를 삭제하였습니다.")
else:
    os.makedirs(folder)      # os에서 폴더 만드는 명령어
    print(folder,"폴더를 생성하였습니다.")

# glob과 비슷함
print(os.listdir())

import time # 시간관련 함수
print(time.localtime())               # 로컬시간 나타내기
print(time.strftime("%Y-%m-%d %H:%M:%S"))   # 시간 간추리기

import datetime
print("오늘 날짜는", datetime.date.today())
today = datetime.date.today()     #오늘날짜 저장
tm = datetime.timedelta(days=100) #100일 저장
print("우리가 만난지 100일은",today+tm) #오늘부터 100일후
