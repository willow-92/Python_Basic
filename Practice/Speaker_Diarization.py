import json
import os
import pprint
directory1 = "/2020-02-012.상담음성_sample/라벨링데이터/"
directory = "/2020-02-012.상담음성_sample/라벨링데이터/KtelSpeech/D60/J91/S00000001"
files = os.listdir(directory)
print(type(files))
with open ("/2020-02-012.상담음성_sample/라벨링데이터/KtelSpeech/D60/J91/S00000001/S00000001.json", encoding= "UTF-8") as f:
    json_data = json.load(f)
# print(json.dumps(json_data, indent="\t"))
dialogs = json_data['dataSet']['dialogs']


previous_speaker = None
texts = []
dialogs_edited = []
i = 1


for dialog in dialogs:
    speaker = dialog['speaker']
    with open (directory1 + dialog['textPath'], encoding= "UTF-8") as f:
        readlines = f.readlines()
        print("{} {} : {}".format(dialog['textPath'][-6:-4], speaker, readlines))
    
    if previous_speaker == speaker:
        texts += readlines

    else:
       texts = readlines
       dialogs_edited.append({
           "speaker" : speaker,
           "texts" : texts
       })   
    i+=1
    previous_speaker = speaker
pprint.pprint(dialogs_edited)


with open("output.json", "w", encoding='utf-8') as f:
    json.dump(dialogs_edited, f, indent="\t", ensure_ascii=False)
