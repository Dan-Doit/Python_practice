#여러 식상한거 말고 탈출법중

#\r : 커서를 맨 앞으로 이동
print("Red Apple\rPine Apple") # 커서를 이동해서 앞에 문구가 안나옴

#\b : 백스페이스바 지우기
print("Red Apple\b") # e을 지우고 출력이됨

#문제를 풀어보자
url = "http://www.naver.com"
my = url.replace("http://www.","") # 앞에 잡용어 제거
my = my[:my.index(".")]            # .com제거

print(my[:3]+"%s%s!" %(len(my),my.count("e")))