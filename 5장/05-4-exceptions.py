# try:
#     ...
# except [발생 오류[as 오류 메시지 변수]]:
#     ...

try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")