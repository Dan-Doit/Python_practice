import pickle
    # 피클 파일을 읽기형태로 읽어서 profile_file 라는 변수에 저장한다.
with open("profile.pickle","rb") as profile_file:
    # 데이터를 불러오기하여 출력함 클로즈해줄필요없이 with문 탈출시 바로 닫아짐
    print(pickle.load(profile_file))

위드의 좋은점은 쓰는것도 불러오는것도 다른거보다 빠르다. 예시로
with open("study.txt","w",encoding="utf8") as study_file:
    study_file.write("열심히 파이썬을 공부하고있어요.")

with open("study.txt","r",encoding="utf8") as study_file:
    print(study_file.read())
