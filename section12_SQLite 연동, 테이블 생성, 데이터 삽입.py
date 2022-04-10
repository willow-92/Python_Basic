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


