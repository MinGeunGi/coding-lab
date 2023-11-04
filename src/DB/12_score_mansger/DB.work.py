# 데이터 베이스 생성 스크립트
import sqlite3

con = sqlite3.connect("scoer.db")
cur = con.cursor()
#score테이블 - name(학생이름), korean(국어), math(수학점수), english(영어 점수), kind(M중간 / F기말)
cur.execute("CREATE TABLE score(name, korean, math, english, kind)")

con.close()
