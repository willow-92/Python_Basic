import ffmpeg
import os
import pprint
import wave

directory = "/한국어 음성/평가용_데이터/KsponSpeech_eval/eval_clean/"
output_directory = "/한국어 음성/평가용_데이터/KsponSpeech_eval/eval_clean/"
file_name = "KsponSpeech_E00"
files = os.listdir(directory)
# print(files)

def pcm2wav( pcm_file, wav_file, channels=1, bit_depth=16, sampling_rate=16000 ):

    # Check if the options are valid.
    if bit_depth % 8 != 0:
        raise ValueError("bit_depth "+str(bit_depth)+" must be a multiple of 8.")
        
    # Read the .pcm file as a binary file and store the data to pcm_data
    with open( pcm_file, 'rb') as opened_pcm_file:
        pcm_data = opened_pcm_file.read();
        
        obj2write = wave.open( wav_file, 'wb')
        obj2write.setnchannels( channels )
        obj2write.setsampwidth( bit_depth // 8 )
        obj2write.setframerate( sampling_rate )
        obj2write.writeframes( pcm_data )
        obj2write.close()




for file in files:
    input = directory + file
    output = directory + file[0:-3] + "wav"
    print(input)

    pcm2wav( input, output, 1, 16, 16000 )
print("convert finished")