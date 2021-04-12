f = open("D:/GitRepository/Jump-to-Python/4장/File/새파일.txt", 'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()


# f = open("4장/File/foo.txt", 'w')
# f.write("Life is too short, you need python")
# f.close()

# with 문 이용 시 자동으로 파일 닫힘
with open("4장/File/foo.txt", 'w') as f:
    f.write("Life is too short, you need python")