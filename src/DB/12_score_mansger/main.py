import sqlite3
'''
기능 명세
1. 학생 중간/기말 평균
2. 한 학생의 성적 출력(조회)
0. 생기부 입력
3. 평균 보여주기
4. 액셀 파일로 만들기
5. 액셀에 성적 입력을 하고 -> 우리의 프로그램 입력
6. 메뉴 출력
0. 출석, 지각생, 수업일수 관리
'''


def print_menu():
    # 메뉴 출력
    print("학생성적 관리 프로그램")
    print('1. 학생성적 입력')
    print('2. 전체 학생의 성적 출력')
    print('3. 평균 보여주기')
    print('4. 한 학생의 성적 출력')
    print('5. 메뉴 다시 출력')
    print("종료하려면 exit 입력을 해주세요.")
    print("\n\n")


def input_score(cur, con):
    '''
    성적 입력
    학생이름 국어, 수학, 영어 구분

    '''
    print("======학생성적 입력======")
    print("학생이름, 국어, 수학, 영어, 중간(M)/기말(F) 구분 순서대로 입력 해주세요")
    print("예시 : 홍길동 98 85 95 M")
    input_value = input().split(' ')
    print(input_value)
    
    # 유효성 검사
    if len(input_value) != 5:
        print('다시 입력해주세요')
        return input_score

    if input_value[4] not in ["M", "F"]:
        print('중간 기말 구분 해주세요')
        return

    
    
    cur.execute(
        f"INSERT INTO score VALUES('{input_value[0]}', '{input_value[1]}', '{input_value[2]}', '{input_value[3]}', '{input_value[4]}')"
    )
    con.commit()
    con.close()




def show_score(cur, con):
    #모든 학생성적 조회
    print("모든 학생 성적 조회")
    
    
    result = cur.execute("SELECT name, korean, math, english, kind FROM score")
    score = result.fetchall()
    for data in score:
        print('이름:', data[0], ',', '국어:', data[1], ',', '수학:',
              data[2], ',', '영어:', data[3], ',', 'M/F:', data[4])

def show_one_student_score(cur):
    #한 학생 성적 조회
    print("한 학생의 이름을 입력 해 주세요")
    s_name = input()
    result = cur.execute(f"SELECT name, korean, math, english, kind FROM score WHERE name = '{s_name}'")
    
    score = result.fetchall()
    if len(score) == 0:
        print("입력된 이름을 찾지 못했습니다.")
    for data in score:
        print('이름:', data[0], ',', '국어:', data[1], ',', '수학:',
              data[2], ',', '영어:', data[3], ',', 'M/F:', data[4])





def average_score(cur):  # 평균계산
    MF = input('중간기말 입력(M : 중간 or F : 기말 or 공백 : 전체 조회 ) : ')
    
    con = sqlite3.connect("scoer.db")
    cur = con.cursor()
    
    result = cur.execute(
        f"SELECT name, korean, math, english, kind FROM score WHERE kind = '{MF}' ")
    score = result.fetchall()
    
    for data in score:

        if MF == 'M':
            avg = (int(data[1]) + int(data[2]) + int(data[3]))/3
            print('이름 : ', data[0], '평균 : ', avg)
        elif MF == 'F':
            avg = (int(data[1]) + int(data[2]) + int(data[3]))/3
            print('이름 : ', data[0], '평균 : ', avg)
        


def run():  # 프로그램의 시작점
    print_menu()
    is_working = True
    con = sqlite3.connect("scoer.db")
    cur = con.cursor()
    while (is_working):

        Exit = input('원하시는 메뉴를 선택 해주세요 :')

        if Exit == "exit":
            print("프로그램을 종료 합니다 :D")
            is_working = False
        if Exit == '1':
            print('1. 학생 성적 입력 \n')
            input_score(cur, con)

        if Exit == '2':
            print('2. 전체 학생의 성적 출력 \n')
            # show_one_student_score()
            show_score(cur, con)
        if Exit == '3':
            print('3. 평균 보여주기 \n')
            average_score(cur)

        if Exit == '4':
            print('4. 한 학생의 성적 출력 \n')
            show_one_student_score(cur)
            
        if Exit == '5':    
            print_menu()
            print('\n\n')
            continue
    con.close()    


run()
input_score()
show_score()
