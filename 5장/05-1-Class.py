class Cookie:  # 클래스 만들기
    pass

a = Cookie()  # 객체 만들기
b = Cookie()

# 사칙연산 클래스 만들기
class FourCal:
    def __init__(self, first, second):  # 생성자, 객체 생성 시 자동 호출
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second
    
    def add(self):
        return self.first + self.second

    def mul(self):
        return self.first * self.second
    
    def sub(self):
        return self.first - self.second
    
    def div(self):
        return self.first / self.second

# 클래스의 상속
class MoreFourCal(FourCal):  # FourCal 클래스의 모든 기능 사용 가능
    def pow(self):
        return self.first ** self.second

# 메서드 오버라이딩
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = FourCal(4, 2)
# a.setdata(4, 2)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

b = FourCal(3, 8)
# b.setdata(3, 8)
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())

a = MoreFourCal(4, 2)
print(a.pow())

a = SafeFourCal(4, 0)
print(a.div())


