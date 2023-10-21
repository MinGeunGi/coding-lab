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
    print("학생성적 관리 프로그램")
    print('1. 학생성적 입력')
    print('2. 한 학생의 성적 출력')
    print('3. 평균 보여주기')
    print('4. 메뉴 다시 출력')
    print("종료하려면 exit 입력을 해주세요.")


def input_score():
  '''
  학생이름 국어, 수학, 영어 구분
  
  '''
  pass


print_menu()
is_working = True
while (is_working):
  
  Exit = input('원하시는 메뉴를 선택 해주세요 :')
  
  
  if Exit == "exit":
    print("프로그램을 종료 합니다 :D")
    is_working = False
  if Exit == '1':
    print('1. 학생성적 입력 \n')
  if Exit == '2':
    print('2. 한 학생의 성적 출력 \n')
  if Exit == '3':
    print('3. 평균 보여주기 \n')
  if Exit == '4':
    print_menu()
    print('\n\n')

    