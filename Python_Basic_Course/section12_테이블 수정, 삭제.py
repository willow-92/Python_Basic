# Section12-3
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 데이터 수정 및 삭제

import sqlite3

# DB생성(파일)
conn = sqlite3.connect('C:/Users/kyung.song/PycharmProjects/Python_Basic/resource/database.db')

# Cursor 연결
c = conn.cursor()

# 데이터 수정1
c.execute("UPDATE users SET username = ? WHERE id = ?", ('niceman',2))



# 툴이 왜 좋냐? 디비에서 바로 이름을 바꿀 수 있다.
# 수정하고 SQL에서 커밋 명령어를 쳐줘도 바로 데이터가 바뀜

#데이터 수정 2
c.execute("UPDATE users SET username =:name  WHERE id = :id", {"name" : 'goodman', "id" : 5})

# 데이터 수정 3
c.execute("UPDATE users SET username = '%s' Where id = '%s'" % ('badbody', 3))



# 중간 데이터 확인 1

# for user in c.execute("SELECT * FROM users"):
#     print(user)


# Row Delete 1
c.execute("DELETE FROM users WHERE id = ?", (2,))
conn.commit()

# Row Delete 2
c.execute("DELETE FROM users WHERE id = :id", {"id" : 5})

# Row Delete 3
c.execute("DELETE FROM users WHERE id = '%s'" % 4)


# 중간 데이터 확인 2

for user in c.execute("SELECT * FROM users"):
    print(user)

# 테이블 전 데이터 삭제
print("users db deleted : ", conn.execute("Delete FROM users").rowcount, " rows")

#커밋
conn.commit()

#접속 해제
conn.close()

# 데이터베이스는 통합관리를 지원. 여러 사람이 작업해도 통합성. 데이터 중복 방지
# 최신 데이터 유지
# 페북이나 인스타, 공휴일이나 크리스마스 때 막대한 데이터들이 페이스북이나 포탈사이트에 쏟아지는데, 내부적으로 데이터베이스를 구축해 놓은 거 보면 대단함
# 그런 것들이 자산이 됨. 데이터 가치를 발견해서 활용하고. 
# 가벼운 디비엠에서를 사용했지만, 오라클이나 마리아디비, 마이에스큐엘, 키벨류 기반의 카산드라, 몽고디비 등
# 데이터를 표준화 시켜주고. 독립성도 보장시켜 줌
# 어플리케이션이 망가져도 데이터베이스는 망가지지 않음
# 복구도 가능함. 해킹을 당한다고 해서 데이터베이스가 왠만하면 흔들리지 않음. 보안도 되어 있고 실시간 처리도 가능하게 해줌
# 백업과 복원도 배우면 스킬이 좋음. 디비를 잘 하면 주위에서 인정을 받고 물질적인 보상도 그만큼 받는다. 
