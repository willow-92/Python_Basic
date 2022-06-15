import os
import csv
import re

dir = "directory"

wer = []
cer = []
rtf = []
file_list = []

for file in os.listdir(dir):
    with open (dir + file, "r", encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break

            if "CER" in line:
                print(line[14:])
                cer.append(re.sub('[\\n]','', line[14:]))

            if "WER" in line:
                print(line[19:])
                wer.append(re.sub('[\\n]','', line[19:]))
            
            if "실시간 계수" in line:
                print(line[9:])
                rtf.append(re.sub('[\\n]','', line[9:]))
                file_list.append(file)
            


with open ("C:/Users/kyung.song/Desktop/result.csv", "w", encoding="utf-8") as j:
    for i in range(len(wer)):
        j.write(file_list[i] + "," + cer[i] + "," + wer[i] + "," + rtf[i] + "," + "\n")



# with open("C:/Users/kyung.song/Desktop/check(wer).csv", "w", encoding="utf-8") as j:
#     j.writelines(wer)
        
# cer = []
# with open(dir, "r", encoding="utf-8") as f:
#     while True:
#         line = f.readline()
#         if not line:
#             break

#         if ('cer_result' in line) and (line[0:3] == "cer"):
#             print(line[25:])
#             cer.append(line[25:])


# with open("C:/Users/kyung.song/Desktop/check.csv", "w", encoding="utf-8") as j:
#     j.writelines(cer)

