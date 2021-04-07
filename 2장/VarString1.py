#문자열 표현 : " ", ' ', """ """, ''' '''
food = "Python's favorite food is perl"
say = '"Python is very easy." he says.'
food2 = 'Python\'s favorite food is perl'
say2 = "\"Python is very easy.\" he says."

#여러 줄
multiline = "Life is too short\nYou need python"
multiline2 = '''
Life is too short
You need python
'''
print(multiline2)
multiline3 = """
Life is too short
You need python
"""
print(multiline3)

#문자열 연산
head = "Python"
tail = " is fun!"
print(head + tail) #문자열 더해서 연결하기
a = "python"
print(a * 2) #문자열 곱해서 반복하기

#문자열 곱하기 응용
print("=" * 50)
print("My Program")
print("=" * 50)

#문자열 길이 구하기
example = "Life is too short"
print(len(example))