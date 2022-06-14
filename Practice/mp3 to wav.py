import ffmpeg
import os
import pprint
import wave

directory = "input file directroy"
output_directory = "output file directory"
files = os.listdir(directory)
# print(files)

def wav2mp3():
    # print(input)
    # print(output)
    cmd = "ffmpeg -i {} -acodec pcm_s16le -ar 16000 -ac 1 {}".format(input, output)
    os.system(cmd)
    






for file in files:
    input = directory + file
    output = output_directory + file[0:-3] + "wav"
    # print(input)

    if "mp3" not in input:
     continue
    # print(input)
    # print(output)
    wav2mp3()
print("convert finished")