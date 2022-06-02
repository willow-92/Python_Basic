#-*- coding: utf-8 -*-
import os
num = 0
root = "D60/J91/"
print(root[4:7])
# for i in range(1,11):
#     if i < 10:
#        num = "0"+str(i)
#     else:
#         num = str(i) 
#     print(num)
    
num = 76
file_no = "S000000"+str(num)
print(file_no)
directory = "/2020-02-012.상담음성_sample/라벨링데이터/KtelSpeech/"+ root + file_no +"/"
outfile_name = root[4:7] + "_S" + str(num) + ".txt"


out_file = open(outfile_name, 'w')
files = os.listdir(directory)
for filename in files: 
    if ".txt" not in filename:
        continue
    file = open(directory + filename, "rt", encoding ='UTF-8')
    line = str(file.readlines())
    out_file.write(line)
    out_file.write("\n\n")
    file.close()
out_file.close()

print("merge completed")

#     for line in files:
#         file.read(line)
#         out_file.write(line)
#     out_file.write("\n\n")
#     file.close()
# out_file.close()