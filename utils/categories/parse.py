
file = open('diet.txt ','w',encoding="utf-8")
with open('tmp.txt', 'r',encoding="utf-8") as f:
    for line in f.readlines():
        if line=='\n':continue
        if '...' not in line:
            file.write(line)

file.close()