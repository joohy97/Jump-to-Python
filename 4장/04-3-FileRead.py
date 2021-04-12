f = open("D:/GitRepository/Jump-to-Python/4장/File/새파일.txt", 'r')
line = f.readline()
print(line)
f.close()

f = open("D:/GitRepository/Jump-to-Python/4장/File/새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

f = open("D:/GitRepository/Jump-to-Python/4장/File/새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

f = open("D:/GitRepository/Jump-to-Python/4장/File/새파일.txt", 'r')
data = f.read()
print(data)
f.close()

