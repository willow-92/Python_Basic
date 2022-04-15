# Section12-1
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 생성 및 삽입

# SQLite를 통해 데이터베이스를 생성해보고, 테이블을 생성하고. 테이블에 데이터 베이스를 삽입, 조회, 수정, 삭제 배우기
# SQL structured Quary Language
# SQL문은 비슷비슷. 다른 제품을 사용하기 전에 기초학습
# 데이터베이스를 안 쓴느 곳은 없음. DB가 없으면 전사적인 프로그램이 돌아갈 수가 없음
# 데이터는 일회성이 아니며, 장기적으로 사용 되어야 함.
# 기업에서는 이런 데이터가 기업의 어떤 존폐를 좌우지할 가장 중요한 자산. 
# 보험회사에 있는 데이터베이스가 잘못되었다고 하면 큰 일이 발생함. 
# 데이터를 가지고 이벤트를하고. 기존 고객을 유치하는 등
# 중복을 해결하고, 데이터의 무결성을 제공하고. 이런 것들은 DB를 공부하면서 배우게 되는 내용이고. 
# 핸들링 위주로

import sqlite3
import datetime

# sqlite3
print('sqilite.version :', sqlite3.version)
print('sqilite.sqliteversion :', sqlite3.sqlite_version)

# 삽입 날짜 생성
now = datetime.datetime.now()
print('now: ', now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime :', nowDatetime)

# DB 생성 & Auto Commit
# 데이터에비스에서 Commit 명령어를 실행하지 않으면 데이터의 변경이나 삽입 내용을 데이터베이스에 반영하지 않음
# 커밋이라는 명령어가 실행될 때 까지 어떤 메모리나, 이런 곳에 저장하고 있다가 영구적으로 반영할 때는 커밋을 해야 함
# 오토 커밋은 그때그때 바로 데이터베이스에 쓰겠다는 것.
# Rollback -> 되돌리는 것. 삽입되기 이전으로 포인트를 정해서 되돌릴 수 있음. 
# 커밋과 롤백은 알아두어야 함.

#DB browser for SQL 설치하기
# DB 생성 & Auto Commit(Rollback)
# conn = sqlite3.connect('C:/Users/kyung.song/PycharmProjects/Python_Basic/resource/database/db')
# 이렇게만 만들면 데이터베이스가 생성이 되기는 하지만, Autocommit가 아니다. 

# conn.comit() # 이 명령어를 실행해야 반영이 됨
# 오토 커밋을 하기 위해서는 아래와 같이 해야 함. 
conn = sqlite3.connect('C:/Users/kyung.song/PycharmProjects/Python_Basic/resource/database.db', isolation_level=None)
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

#regdate 이미 위에서 나우 데이트 타임을 변환해 놓았음.
# 근데 그냥 넣으면 문자열 취급을 하기 때문에 에러가 발생됨
# 이떄 처리하기 위해서 ? 처리를 해 놓고, 두 번째 매개변수로 튜플 형태로 입력해줌
# 이 물음표로 처리된 것은 익스큐트가 실행할 떄 매치를 시켜서 물음표로 된 것은 순서대로. 하나밖에 없으니까
# 튜플에 있는 값이 들어가게 됨.

c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)" ,(2, 'park', 'park@daum.net', '010-1111-1111', 'Park.com', nowDatetime))
# 첫 번째 물음표는 첫 번째 튜플, 두 번째 물음표는 두번쨰 튜플. 이 6개의 갯수와 튜플 원소의 갯수가 맞아야 함
# 안 맞으면 에러가 남

# 유니크 컨스트레인트 에러가 나옴. 
# 현재 1번 데이터를 넣었는데, 1번 데이터를 또 넣으려고 하니까 에러가 남
# 그래서 1번 데이터를 주석처리 하고 실행하면 들어감

# Many 삽입
# 파일에서 가져오거나, 튜플, 리스트, 셋, 딕셔너리 형태를 한 번에 인서트 하는 방법을 알아야 함
# 한 번에 대용량을 삽입하는 방법
# 튜플과 리스트 형태를 삽입할 수 있음

userList = (
    (3, 'Lee', 'Lee@naver.com', '010-2222-2222', 'Lee.com', nowDatetime),
    (4, 'cho', 'Cho@daum.net', '010-3333-3333', 'Cho.com', nowDatetime),
    (5, 'Yoo', 'Yoo@google.com','010-4444-4444', 'Yoo.net', nowDatetime)
)

# 위와 같이 파일에서 읽어왔거나, 웹에서 제이슨 형식으로 오면 딕셔너리 형태로 다를 수 있는데, 튜플로 형변환하고
# 튜플 안에 튜플, 튜플 안에 리스트, 리스트 안에 리스트로 데이터셋을 만들어서 한 번에 인서트 하는게 훨씬 빠르다.
# 익스큐트 매니라는 메소드가 있기 때문. 

c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)", userList) 

# 앞으로 파일에서 주로 가져와서 웹에서 크롤링한 데이터를, 웹에서 사용자가 회원가입을 할텐데, 앞으로 배울 플라스크나 디장고. 거기서 웹상에서 입력받은 데이터를
# 장고 같은 경우는 ORM인데, 내부적으로 이런 쿼리가 작동을 해서 데이터베이스에 저장이 되는 것.

# 테이블 데이터 삭제
# conn.execute("DELETE FROM users") 

# 데이터를 지우는 테이블 삭제는 쿼리. 익스큐트 안에 SQL 쿼리를 날려주면 되고
# 보통은 print로 몇 개를 지웠는지 확인할 수 있음

# print("users db deleted :" , conn.execute("DELETE FROM users").rowcount)

# 커밋 : isolation_level = None 일 경우 자동 반영 (오토 커밋)
# conn.commit() <- 위 명령어를 넣지 않았을 경우 실행해야 함

# 롤백
# conn.rollback()

# 리소스를 썼으면 닫아줘야 함
conn.close()