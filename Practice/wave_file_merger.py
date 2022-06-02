import ffmpeg
import os
import pprint
# ud = upper_directory
ud1 ="D62"
ud2 ="J93"
output_dir = "/Speech_Diarization_Model/WAV_files/D62_Tel/"
folder = os.listdir("/Desktop/Validation/{}/{}/".format(ud1,ud2))
# pprint.pprint(folder)


def merge_wav ():
    # wav 파일 합치기 위한 리스트 제작
    input_file = base_dir + "file_list.txt"
    output_file = "{}{}_{}_{}.wav".format(output_dir, ud1, ud2, i)
    
    with open(input_file, "w") as f:
        for name in files:
            if "wav" not in name:
                continue
            f.write("file " + name + "\n")
    print()
    print("file list created")
    print()
    print("start merging wav files")
    print()
    
    # 생성된 리스트 내 파일 병합
    
    cmd = "ffmpeg -f concat -i {} -c copy {}".format(input_file, output_file)
    os.system(cmd)
    print("done!")


for i in folder:
    base_dir = '/Desktop/Validation/{}/{}/{}/'.format(ud1, ud2, i)
    files = os.listdir(base_dir)
    # pprint.pprint(files)
    merge_wav()


      
 




