# 일반 유닛
class Unit:
    def __init__(self,name,hp): #여기서 __init__은 파이썬에서 생성자이다.
        self.name = name               # 멤버변수 : 클래스 내에 받은 변수
        self.hp = hp

# 일반유닛의 정보가 정확하게 공격유닛과 일치되니까 상속을써서 더 빠르게 표현

# 공격유닛
class AttackUnit(Unit):
    def __init__(self,name,hp,damage): #여기서 __init__은 파이썬에서 생성자이다.
        # 일반 유닛을 상속받았기에 일반유닛의 정보와 변수가 넘어온다.
        # 이때 써야할 문구는
        Unit.__init__(self,name,hp)
        # 유닛에서 이름과 체력을 받는다.
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

class flyable():
    def __init__(self,fling_speed):
        self.fling_speed = fling_speed

    def fling(self,name,location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]"\
              .format(name, location, self.fling_speed))
class Attackflyable(AttackUnit,flyable):
    def __init__(self,name,hp,damage,fling_speed):
        AttackUnit.__init__(self,name,hp,damage)
        flyable.__init__(self,fling_speed)

# 발키리 : 공격 유닛, 한번에 14발 발사
valkyrie = Attackflyable("발키리",200,6,5)
valkyrie.fling(valkyrie.name,"5시")

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self,name,hp,0)
        super.__init__(name,hp,0)            # 위쪽 구문과 같은 뜻이다. 차이점은 self를 안쓴다는것
                                             # 다중상속을 받을경우 마지막 상속받은 클래스의 변수값을 초기화 안시키므로
                                             # 쓸때 주의해야한다. 그냥 super안쓰는게 좋을듯하기도하고
        self.location = location
supply_depot = BuildingUnit("서플라이 디팟", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")
def game_over():
    pass                # pass 함수로 인하여 실행을 일단 실행해도 오류가없음
game_start()
game_over()



