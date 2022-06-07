import json
import os
import pprint
from xml.dom.minidom import TypeInfo

ud1 ="D61"
ud2 ="J92"
output_dir = "C:/Users/kyung.song/Desktop/TTA_Dataset/Speech_Diarization_Model/Labeled_texts/D61_Fin_new/"
validation_dir = "C:/Users/kyung.song/Desktop/Validation"
base_dir = "{}/KtelSpeech/{}/{}/".format(validation_dir, ud1,ud2)
folder = os.listdir(base_dir)

def diarize():
    i = 1
    for files in folder:
        # 제이슨 파일 경로 지정 및 열기
        with open(output_dir + files + '.txt', 'w', encoding='UTF-8') as f:
            pass

        try:
            if files == 'S00002095':
                pass
            with open("{}{}/{}.json".format(base_dir, files, files), encoding= "UTF-8") as f:
                json_data = json.load(f)
        except:
            with open("{}{}/{}.json".format(base_dir, files, files), encoding="utf-8-sig") as f:
                json_data = json.load(f)
        
  

        # 필요 변수 세팅
        dialogs = json_data['dataSet']['dialogs']
        speaker_text_info = {}

        for speaker_info in json_data['dataSet']['typeInfo']['speakers']:
            speaker_text_info[speaker_info['id']] = []

        previous_speaker = None
        texts = []


        # 화자 분리해서 읽어오기
        for dialog in dialogs:
            speaker = dialog['speaker']
            text_path = dialog['textPath']

            with open(f'{validation_dir}/{text_path}', encoding="UTF-8") as f:
                readlines = f.readlines()  


            # ================================================================================
            # 같은 화자 발화 묶기 (화자가 2명 이상인 경우)
            # texts = readlines
            # if previous_speaker == speaker:

            #     speaker_text_info[speaker] += texts

            # 다른 화자 감지시 리스트에 담기 (화자가 2명 이상인 경우)
            # else:
            #     speaker_text_info[speaker] += texts
                

            #     if previous_speaker is not None:
            #         with open(output_dir + files + '.txt', 'a', encoding='UTF-8') as f:
            #             total_text = ""
            #             for text in speaker_text_info[previous_speaker]:
            #                 total_text += text
            #             f.write(f"{previous_speaker}: {total_text}\n")
                        

            #         speaker_text_info[previous_speaker] = []
            #     previous_speaker = speaker

            # ===================================================================================================



            # 같은 화자 발화 묶기 (화자가 1명만 있는 경우)
            texts = readlines
  
            with open(output_dir + files + '.txt', 'a', encoding='UTF-8') as f:
                f.write(speaker + " : " + str(texts).strip("['n/ ").strip("']") + "\n")
        
                    

            #         speaker_text_info[previous_speaker] = []
            #     previous_speaker = speaker


    print("done")

                
diarize()































# directory1 = "C:/Users/kyung.song/Desktop/2020-02-012.상담음성_sample/라벨링데이터/"
# directory = "C:/Users/kyung.song/Desktop/2020-02-012.상담음성_sample/라벨링데이터/KtelSpeech/D60/J91/S00000001"
# files = os.listdir(directory)
# print(type(files))
# with open ("C:/Users/kyung.song/Desktop/2020-02-012.상담음성_sample/라벨링데이터/KtelSpeech/D60/J91/S00000001/S00000001.json", encoding= "UTF-8") as f:
#     json_data = json.load(f)
# # print(json.dumps(json_data, indent="\t"))
# dialogs = json_data['dataSet']['dialogs']


# previous_speaker = None
# texts = []
# dialogs_edited = []
# i = 1





# with open("output.json", "w", encoding='utf-8') as f:
#     json.dump(dialogs_edited, f, indent="\t", ensure_ascii=False)



