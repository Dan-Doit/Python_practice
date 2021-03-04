# # 스타크래프트로 배우는 클래스
# # 마린 : 공격 유닛,군인, 총을쏨
# name = "마린"
# hp = 40
# damage = 5
#
# print("{}유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1},\n".format(hp,damage))
#
# # 탱크 : 공격유닛, 탱크, 일반모드/시즈모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35
#
# print("{}유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1},\n".format(tank_hp,tank_damage))
#
# tank_name2 = "탱크"
# tank_hp2 = 150
# tank_damage2 = 35
#
# print("{}유닛이 생성되었습니다.".format(tank_name2))
# print("체력 {0}, 공격력 {1},\n".format(tank_hp2,tank_damage2))
#
# def attack(name,location,damage) :
#     print("{0}:{1} 방향으로 적군을 공격합니다.[공격력] : {2}".\
#           format(name,location,damage))
#
# attack(name,"1시", damage)
# attack(tank_name,"1시", tank_damage)
#
# # 이런식으로 하면 언제 만들어 유닛이 몇천일텐데
# # 그래서 우리는 클래스를 만든다. 붕어빵 틀이라고 생각하면됨

class Unit:
    def __init__(self,name,hp,damage): #여기서 __init__은 파이썬에서 생성자이다.
        self.name = name               # 멤버변수 : 클래스 내에 받은 변수
        self.hp = hp
        self.damage = damage
        print("{}유닛이 생성되었습니다.".format(name))
        print("체력 {0}, 공격력 {1},\n".format(hp, damage))

marine1 = Unit("마린",40,5)  # 정확하게 데이터값을 입력해주어야함 self를 제외한
marine2 = Unit("마린",40,5)
tank1 = Unit("탱크",150,35)
tank2 = Unit("탱크",150,35)

# 레이스 : 공중유닛, 비행기, 클로킹 (상대방에게 보이지않음)
wraith1 = Unit("레이스",80,5)
print("체력 {0}, 공격력 {1},\n".format(wraith1.hp,wraith1.damage)) # Unit 클래스의 변수 사용가능

# 다크아칸이 뺏음
# 객체를 클래스에서가 아닌 외부에서도 수정할수있다.
wraith2 = Unit("레이스",80,5)
wraith2.cloking = True

if wraith2.cloking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))