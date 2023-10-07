# 데이터 베이스 생성 스크립트
import sqlite3
con = sqlite3.connect("scoer.db")
cur = con.cursor()
cur.execute("CREATE TABLE score(name, korean, math, english, kind)")

con.close()
