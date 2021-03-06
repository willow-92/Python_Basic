# section13_타이핑 게임 제작, 기본 완성
# 파일을 읽어오고, 직접 입력을 하고, 소리도 나오게 하고, 전반적인 입출력 기능이 4가지나 들어가 있음
# 업그레이드 타이핑 게임 제작
# 타이핑 게임 제작 및 기본 완성

import random
from telnetlib import AUTHENTICATION
import time

# 사운드 출력 필요 모둘
import winsound
import sqlite3
import datetime
import asyncio

# DB 생성 & Auto Commit
# 본인 DB 경로

async def play_sound(is_answer):
    
    sound_path = './Python_Basic/sound/sound_good.wav' if is_answer else './Python_Basic/sound/sound_bad.wav'

    winsound.PlaySound(sound_path, winsound.SND_FILENAME)

async def make_question():
    random.shuffle(words)
    random.choice(words)

    return random.choice(words)

conn = sqlite3.connect('C:/Users/kyung.song/PycharmProjects/Python_Basic/resource/records.db', isolation_level=None)

# Cursor 연결
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS records(id INTEGER PRIMARY KEY AUTOINCREMENT, cor_cnt INTEGER, record text, regdate test)")

# 전역변수를 스코프에서 선언
words = [] #영어 단어 리스트(1000ro 로드)

n = 1 # 게임 시도 횟수
cor_cnt = 0 # 정답 개수 

with open('./Python_Basic/resource/word.txt','r') as f:
    for c in f:
        words.append(c.strip())
# print(words) # 단어 리스트 확인

# input("Ready? press Enter key!") # Enter Game Start!

start = time.time()
end = time.time() #End Time

q = make_question()
print("*Question # {} : {}".format(n, q)) # 문제 출력
x = input() # 타이핑 입력

while n <= 4:

    print()
    
    if str(q.strip()) == str(x).strip(): # 입력 확인(공백 제거)
        # 정답 소리 재생
        asyncio.run(play_sound(True))
        print("Pass!")
        cor_cnt += 1
    else:
        # 오답 소리 재생
        print("Wrong!")
        asyncio.run(play_sound(False))

    print("\n==================\n")

    n += 1 # 다음 문제 전환

et = end - start
et = format(et, ".3f") # 소수 셋째 자리 출력(시간)

if cor_cnt >= 3:
    print("합격")
else:
    print("불합격")


# 기록 DB 삽입
cursor.execute("INSERT INTO records('cor_cnt', 'record', 'regdate') VALUES (?, ?, ?)", (cor_cnt, et, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))


# 수행 시간 출력
print("게임 시간 : ", et, "초", "정답 개수 : {}".format(cor_cnt))

# 시작 지점
if __name__ == '__main__':
    pass