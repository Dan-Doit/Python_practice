#스코어 파일 이라는걸 만들껀데
#             자료를 txt파일에서 가져오고
#                           쓰기 전용이고(덮어쓰기가됨)
#                                  인코딩을 '한글'로 할꺼임 이거안하면 한글 깨짐
score_file = open("score.txt","w",encoding="utf8")
print("수학점수 : 0",file=score_file)
print("영어점수 : 50",file=score_file)
score_file.close()       # !!!!!!!!!!꼭 연파일은 닫아야한다!!!!!!!!!!
# 지금까지 뜻이 score.txt를 쓰기 목적으로 열어 내용을 쓰고 저장후 닫음
# 와...신기함 이거 실행시키니까 python 지정한 폴더에 메모장파일이 생기고 저장됨

#                           a는 이어쓰기 (마지막부터 이어서 써짐)
score_file = open("score.txt","a",encoding="utf8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()
                            r은 읽어오기
score_file = open("score.txt","r",encoding="utf8")
# 한번에 다 읽어오기
print(score_file.read())
score_file.close()

score_file = open("score.txt","r",encoding="utf8")
# 한줄씩 읽고 커서를 다음줄로 이동
print(score_file.readline())
print(score_file.readline())
score_file.close()


score_file = open("score.txt","r",encoding="utf8")
# 한문장씩 끝까지 출력함
while True:
    line = score_file.readline()
    if not line:
        break
    print(line,end='')
score_file.close()

score_file = open("score.txt","r",encoding="utf8")
lines = score_file.readlines() #list 형태로 저장
for line in lines:
    print(line, end='')
score_file.close()
