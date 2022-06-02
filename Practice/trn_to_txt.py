out_file = "KsponSpeech_E00001"
f = open('/eval_clean.txt', 'r', encoding='UTF-8')

for i in range(3000):
    line = f.readline()
    out_file_name = "/eval_clean_txt/" + line[28:47] + "txt"
    print(out_file_name)
    out_file = open(out_file_name, 'w')
    out_file.write(line[54:])
    # print(line[28:47] + "txt")
    # print(line[54:])
    out_file.close()
print("DONE!")

