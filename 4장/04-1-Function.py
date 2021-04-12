# def 함수명(매개변수):
#     <수행할 문장1>
#     <수행할 문장2>
#     ...

def add(a, b):
    return a + b
a = 3
b = 4
c = add(a, b)
print(c)

# 입력값이 없는 함수
def say():
    return 'Hi'
a = say()
print(a)

# 결과값이 없는 함수
def add2(a, b):
    print(f"{a}, {b}의 합은 {a + b}입니다.")
add2(3, 4)

# 입력값과 결과값이 둘 다 없는 함수
def say2():
    print('Hello')
say2()


# 입력값이 몇 개가 될 지 모를 때
# def 함수이름(*매개변수): 
#     <수행할 문장>
#     ...

def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result
print(add_many(1, 2, 3))
print(add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
        return result
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
        return result
print(add_mul('add', 1, 2, 3, 4, 5))
print(add_mul('mul', 1, 2, 3, 4, 5))
