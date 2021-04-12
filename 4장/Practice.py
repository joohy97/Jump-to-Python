# Q1
def is_odd(num):
    if num % 2 == 0:
        return "짝수입니다."
    elif num % 2 == 1:
        return "홀수입니다"
    else:
        return "숫자가 아닙니다"
print(is_odd(5)) # 홀수입니다
print(is_odd(50)) # 짝수입니다

# Q2
def calc_mean(*args):
    sum = 0
    for a in args:
        sum = sum + a # 합계 구하기
    return sum / len(args) 
print(calc_mean(2, 2, 2, 4, 4, 4)) # 3.0

# Q3
input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = int(input1) + int(input2) # 입력 자료형은 문자열이므로 숫자형으로 자료형을 변환시켜줘야한당
print("두 수의 합은 %s 입니다" % total)

# Q4
print("you" "need" "python") # youneedpython
print("you"+"need"+"python") # youneedpython
print("you", "need", "python") # you need python 이거만 띄어쓰기
print("".join(["you", "need", "python"])) # youneedpython

# Q5
f1 = open("4장/test.txt", 'w')
f1.write("Life is too short")
f1.close() # 파일을 닫지 않으면 또 열 수 없다 사용이 끝나면 꼭 닫아주기!

f2 = open("4장/test.txt", 'r')
print(f2.read())
f2.close()

# Q6
f = open("4장/test1.txt", "a")
while True:
    a = input("작성할 내용을 입력하세요 : ")
    if a == "":
        break
    else:
        f.write(a + '\n')

f.close()

# Q7