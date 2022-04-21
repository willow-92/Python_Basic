# Section12-3
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 데이터 수정 및 삭제

import sqlite3

# DB생성(파일)
conn = sqlite3.connect('C:/Users/kyung.song/PycharmProjects/Python_Basic/resource/database.db')

# Cursor 연결
c = conn.cursor()

# 데이터 수정1
