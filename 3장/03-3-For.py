# 전형적인
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

# 다양한
a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)

# 응용
# 총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다. 합격인지 불합격인지 결과를 보여 주시오.
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print(f"{number}번 학생은 합격입니다.")
    else:
        print(f"{number}번 학생은 불합격입니다.")

# 응용2 : for문과 continue
for mark in marks:
    number = number + 1
    if mark < 60:
        continue
    print(f"{number}번 학생 축하합니다. 합격입니다.")

# range 함수
add = 0
for i in range(1, 11):
    add = add + i
print(add)

# 응용3 : for문과 range 함수
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print(f"{number}번 학생 축하합니다. 합격입니다.")

# 응용4 : 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i * j, end=" ")
    print('')

result = [x * y for x in range(2, 10)
                for y in range(1, 10)]
print(result)