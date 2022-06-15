import os
import csv
dir = "directory"

cer = []
with open(dir, "r", encoding="utf-8") as f:
    while True:
        line = f.readline()
        if not line:
            break

        if ('cer_result' in line) and (line[0:3] == "cer"):
            print(line[25:])
            cer.append(line[25:])


with open("C:/Users/kyung.song/Desktop/check.csv", "w", encoding="utf-8") as j:
    j.writelines(cer)

