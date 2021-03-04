# # 피클 (pickle) : 파일 형태로 저장해주기
import pickle                    #피클은 항상 바이너리 파일(2진수)로 열어야함 인코딩 노필요
# profile_file = open("profile.pickle","wb")
# profile = {"이름":"박명수", "나이":30,"취미":["축구","야구","배구"]}
# print(profile)
# pickle.dump(profile,profile_file) # 쓴내용 저장 하기 , 앞에가 쓴문장, 뒤가 저장할 파일 이름
# profile_file.close()

profile_file = open("profile.pickle","rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile 불러오기
print(profile)
profile_file.close()