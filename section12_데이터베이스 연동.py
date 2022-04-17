# section12-2
# 파이썬 데이터베이스 연동(SQLITE)
# 테이블 조회

import sqlite3
import datetime



# 삽입 날짜 생성
now = datetime.datetime.now()
print('now: ', now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime :', nowDatetime)

path = 'C:/Users/kyung.song/PycharmProjects/Python_Basic/resource/database.db'

conn = sqlite3.connect(path, isolation_level=None)
# DB browser for SQL에서 데이터베이스 불러오기
# 잘 설정이 되었는지 확인해볼 것

# cursor 
# 커서의 획득은 C
c = conn.cursor()
print('Cursor Type: ', type(c))

# 테이블 생성(Data Type : TEXT, NUMERIC, INTEGER, REAL, BLOB)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone txst, website test, regdate test)")

conn.execute("DELETE FROM users")

# 데이터 삽입
c.execute("INSERT INTO users VALUES(1, 'kim', 'kim@naver.com', '010-000-0000', 'kim.com', ?)", (nowDatetime,))

c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)" ,(2, 'park', 'park@daum.net', '010-1111-1111', 'Park.com', nowDatetime))

userList = (
    (3, 'Lee', 'Lee@naver.com', '010-2222-2222', 'Lee.com', nowDatetime),
    (4, 'cho', 'Cho@daum.net', '010-3333-3333', 'Cho.com', nowDatetime),
    (5, 'Yoo', 'Yoo@google.com','010-4444-4444', 'Yoo.net', nowDatetime)
)

c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)", userList) 

# 테이블 데이터 삭제
# conn.execute("DELETE FROM users") 

# 커밋 : isolation_level = None 일 경우 자동 반영 (오토 커밋)
# conn.commit() <- 위 명령어를 넣지 않았을 경우 실행해야 함

# 롤백
# conn.rollback()

# 리소스를 썼으면 닫아줘야 함
conn.close()

#DB파일 조회(없으면 새로 생성)
conn = sqlite3.connect(path) # 본인 DB 경로

# 커서 바인딩
c = conn.cursor()

# 데이터 조회(전체)
c.execute("SELECT * FROM users")

# 커서 위치가 변경
# 1개 로우 선택
# print('One -> \n', c.fetchone())

# 지정 로우 선택
# print("Three -> \n", c.fetchmany(size=3))

# 전체 로우 선택
# print("All -> \n", c.fetchall())

# print("All -> \n", c.fetchall())

# 커서 중요함.
# 파일 읽어올 때 처럼 읽어온 내용의 다음 위치에서 딱 기억하고 있는 것
# 현재 데이터가 5개 밖에 없지만, 만개, 백 만개 이렇게 있을 때 커서가 이동을 하면서 다음 데이터의 위치를 기억하고 있다는 것. 
# DB 개념도 있지만, 외부 파일을 읽어오는 개념에서 커서의 역할이 중요하다고 볼 수 있다. 

# 순회 1
rows = c.fetchall()
for row in rows:
    print('retrieve1 >', row)

for row in c.fetchall():
    print('retrieve2 >', row)
