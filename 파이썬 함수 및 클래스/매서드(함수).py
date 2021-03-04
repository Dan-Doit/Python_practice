class Unit:
    def __init__(self,name,hp,damage): #여기서 __init__은 파이썬에서 생성자이다.
        self.name = name               # 멤버변수 : 클래스 내에 받은 변수
        self.hp = hp
        self.damage = damage
        print("{}유닛이 생성되었습니다.".format(name))
        print("체력 {0}, 공격력 {1},\n".format(hp, damage))
# 공격유닛
class AttackUnit:
    def __init__(self,name,hp,damage): #여기서 __init__은 파이썬에서 생성자이다.
        self.name = name               # 멤버변수 : 클래스 내에 받은 변수
        self.hp = hp
        self.damage = damage
        print("{}유닛이 생성되었습니다.".format(name))
        print("체력 {0}, 공격력 {1},\n".format(hp, damage))
    def attack(self,location):
        print("{0}:{1}방향으로 적군을 공격합니다. [공격력 : {2}]"\
              .format(self.name,location,self.damage))

    def damaged(self,damage):
        print("{0}가 데미지를 입었습니다. [받은 데미지 : {1}]" \
              .format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{0} 유닛이 파괴되었습니다.".format(self.name))

# 파이어뱃 : 공격유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃",50,10)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)