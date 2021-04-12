f = open("4장/File/새파일.txt", 'w')
f.close()

f = open("D:/GitRepository/Jump-to-Python/4장/File/새파일.txt", 'w')
f.close()

# r : 읽기모드
# w : 쓰기모드
# a : 추가모드

f = open("D:/GitRepository/Jump-to-Python/4장/File/새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     print(data)