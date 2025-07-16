import os

fp = open("rwfile.txt", mode='w', encoding="utf-8");
fp.write("hello world\n")
fp.write("next line")
fp.close()

print(os.stat("rwfile.txt").st_size)

with open("rwfile.txt", mode="r", encoding="utf-8") as f:
    print(f.read())

print("------")

with open("rwfile.txt", mode="r", encoding="utf-8") as f:
    for line in f:
        print(line, end='')