# 숫자 자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*10)
print(3*(3+12))

#문자열 자료형
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)

#boolean자료형 (참 / 거짓)
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not False)
print(not True)
print(not (5 > 10))

#변수
#애완동물을 소개해 주세요~
#변수 사용 전
print("우리집 강아지의 이름은 연탄입니다.")
print("연탄이는 4살이며, 산책을 아주 좋아해요")
print("연탄이는 어른일까요? True")
#변수 사용 후 
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3
print("우리집 " + animal + "의 이름은 " + name + "입니다.")
# print(name + "는 " + str(age) + "살이며, " +  hobby +"을 아주 좋아해요")
print(name , "는 " , age , "살이며, " , hobby ,"을 아주 좋아해요") # ,로 구분시 빈칸이 포함된다. ex) 연탄이 는  4 살이며,  산책 을 아주 좋아해요
print(name + "는 어른일까요? " + str(is_adult))


''' 이렇게 하면
여러 문장이 
주석처리 
됩니다 '''



#연산자
print(1+1) # 2
print(3-2) # 1
print(5*2) # 10
print(10/3) # 3.3333...
print(2**3) # 2^3 = 8
print(5%3) # 나머지 구하기 2
print(10%3) # 1
print(10//3) #10을 3으로 나눴을때의 몫

print(10 > 3) # True
print(4 >= 7) # False
print(5 <= 5) # True
print(3 == 3) # True
print(4 == 2) # False
print(3 + 4 == 7) # True
print(1 != 3) # True
print(not(1 != 3)) # False

print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) # True
print((3 > 0) or (3 > 5)) # True
print((3 > 0) | (3 > 5)) # True
print(5 > 4 > 3) # True 5는 4보다 크고 4는 3보다 크다

#간단한 수식
print(2 + 3 * 4) # 14
print((2+3) * 4) # 20
number = 2 + 3 * 4 # 14
print(number)
number = number + 2 # 16
print(number)
number += 2 # 18
print(number)
number *= 2 # 36
print(number)
number /= 2 # 18
print(number)
number -= 2 # 16
print(number)
number %= 2 #0
print(number)

#숫자처리함수
print(abs(-5)) # -5의 절대값 5
print(pow(4,2)) # 4^2 16
print(max(5,12)) # 최대값 반환 12
print(min(5,12)) # 최소값 반환 5
print(round(3.14)) #반올림 3
print(round(4.99)) #반올림 5

from math import *
print(floor(4.99)) # 내림 4
print(ceil(3.14)) #올림 4
print(sqrt(16)) # 제곱근, 4

#랜덤함수
from random import *
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) #0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) #0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) #1 ~ 10 이하의 임의의 값 생성
print(int(random() * 45) + 1) #1 ~ 45 이하의 임의의 값 생성 
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
print("오프라인 스터디 모임 날짜는 매월",randint(4, 28),"일로 선정되었습니다.")

#문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "나는 소년입니다"
print(sentence2)
sentence3 = """
나는 소년입니다 
하하
"""
print(sentence3)

#슬라이싱
jumin = "950307-1234567"
print("성별 : " + jumin[7])
print("년도 : " + jumin[0:2]) # 0부터 2 직전까지 (0,1)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[0:6])
print("생년월일 : " + jumin[:6]) # 처음부터 6직전까지
print("뒤 7자리 : " + jumin[7:14])
print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) #맨 뒤에서 7번째 부터 끝까지

#문자열처리함수
python = "Python is Amazing"
print(python.lower()) # 모든 문자 소문자
print(python.upper()) # 모든 문자 대문자
print(python[0].isupper()) # 0번째 문자가 대문자인지
print(len(python)) # 문자열 길이
print(python.replace("Python", "Java")) #해당 문자 치환
index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)
print(python.find("n")) #없는 값을 출력하는 경우 find는 -1 index는 에러
print(python.count("n")) #n이 몇개인지

#문자열포맷
print("a" + "b")
print("a","b")

#방법 1
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple 은 %c로 시작해요." % "A")
print("나는 %s색과 %s색을 좋아해요." %("파랑", "빨간"))
print("나는 %d살입니다 %s색을 좋아해요." %(26, "빨간"))

#방법2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

#방법3
print("나는 {age}살이며, {color}색을 좋아해요".format( color="빨간",age=20))

#방법4 (v3.6 이상~)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")

#탈출문자
# \n : 줄바꿈
print("백문이 불여일견 \n백견이 불여일타")
print("저는 \"나도코딩\"입니다.") # 저는 "나도코딩"입니다.
# \\ : 문장 내에서 \
print("path : C:\\study\\study-basic-python") # path : C:\study\study-basic-python

# \r : 커서를 맨 앞으로 이동(치환)
print("Red Apple\rPine") # PineApple

# \b : 백스페이스(한 글자 삭제)
print("Redd\bApple") # RedApple

# \t : 탭 (4칸이동)
print("Red\tApple") # Red     Apple


#퀴즈 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
'''
예 ) http://naver.com
규칙1 : http:// 부분은 제외 => naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성

예) 생성된 비밀번호 : nav51!

'''
link = "http://naver.com"
replaceLink = link.replace("http://", "") #규칙1
domain = replaceLink[:replaceLink.index(".") ] #규칙2
password = domain[:3] + str(len(domain)) + str(domain.count("e")) + "!" # 규칙 3
print(f"{link}의 생성된 비밀번호는 {password} 입니다.")


#리스트 []

#지하철 칸 별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway) # [10, 20, 30]
subway = ["유재석", "조세호", "박명수"] 
print(subway) # ['유재석', '조세호', '박명수']

#조세호씨가 몇 번쨰 칸에 타고 있는가?
print(subway.index("조세호")) # 1

#하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하") # ['유재석', '조세호', '박명수', '하하']
print(subway)

#정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈")
print(subway) # ['유재석', '정형돈', '조세호', '박명수', '하하']

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop()) # 하하
print(subway.pop()) # 박명수

#같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

#정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list) # [1, 2, 3, 4, 5]
# 역정렬
num_list.reverse()
print(num_list) # [5, 4, 3, 2, 1]

#모두 지우기
num_list.clear()
print(num_list)

#다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]
print(mix_list) # ['조세호', 20, True]

#리스트 확장
subway.extend(mix_list)
print(subway) # ['유재석', '정형돈', '조세호', '유재석', '조세호', 20, True]

#사전
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3]) # 유재석
print(cabinet.get(3)) # 유재석
#없는 값 가져오기
'''
cabinet[5]  keyError 후 시스템 정지 
cabinet.get(5) 문자열 'None' 다음 행 진행
'''
print(cabinet.get(5, "사용 가능")) #사용가능
print(3 in cabinet) # Key3 가 cabinet에 있는가 ? True
print(5 in cabinet) # Key5 가 cabinet에 있는가 ? False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"]) #유재석
print(cabinet["B-100"]) #김태호

#새 손님
print(cabinet)
cabinet["C-20"] = "조세호"
print(cabinet) # {'A-3': '유재석', 'B-100': '김태호', 'C-20': '조세호'}
cabinet["A-3"] = "김종국"
print(cabinet) # {'A-3': '김종국', 'B-100': '김태호', 'C-20': '조세호'}

#간 손님
del cabinet["A-3"]
print(cabinet) # {'B-100': '김태호', 'C-20': '조세호'}

#key들만 출력
print(cabinet.keys()) # dict_keys(['B-100', 'C-20'])

#value들만 출력
print(cabinet.values()) # dict_values(['김태호', '조세호'])

#key, value 쌍으로 출력
print(cabinet.items()) # dict_items([('B-100', '김태호'), ('C-20', '조세호')])

#목욕탕 폐점
cabinet.clear


#튜플 
menu = ("돈까스", "치즈까스")
print(menu[0]) # 돈까스
print(menu[1]) # 치즈까스

#menu.add("생선까스") # AttributeError: 'tuple' object has no attribute 'add'
name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)
(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

#집합(set)
#중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python) # {'유재석'}
print(java.intersection(python)) # {'유재석'}

#합집합 (java도 할수 있거나 python도 할 수 있는 개발자)
print(java | python) # {'김태호', '박명수', '양세형', '유재석'}
print(java.union(python)) # {'김태호', '박명수', '양세형', '유재석'}

#차집합 (java 할 수 있찌만 python은 할줄 모르는 개발자)
print(java - python) # {'양세형', '김태호'}
print(java.difference(python)) # {'양세형', '김태호'}

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
python.add("김태호")
print(python) # {'김태호', '유재석', '박명수'}

# java를 잊었어요
java.remove("김태호")
print(python) # {'김태호', '박명수', '유재석'}

#자료구조의 변경
# 커피숍
menu = {"커피", "우유", "주스"}
print(menu, type(menu)) # {'주스', '커피', '우유'} <class 'set'>

menu = list(menu)
print(menu, type(menu)) # ['커피', '주스', '우유'] <class 'list'>

menu = tuple(menu)
print(menu, type(menu)) # ('커피', '주스', '우유') <class 'tuple'>

'''
퀴즈) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 했습니다.
댓글 작성자들 중에 추첨을 통해 "1명"은 치킨, "3명"은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오.

조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건3 : random 모듈의 shuffle과 sample을 활용

(출력 예제)
--- 당첨자 발표 ---
치킨 당첨자 : 1
커피 당첨자 : [2,3,4]
--- 축하합니다 ---

(활용 예제)
from random import *
lst = [1,2,3,4,5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst,1))
'''
from random import *
lst = list(range(1,21)) # 1부터 20까지 숫자를 생성
shuffle(lst)
winners = sample(lst, 4)
chicken = winners[0]
coffee = winners[1:]

print(f"--- 당첨자 발표 ---\n치킨 당첨자 : {chicken}\n커피 당첨자 : {coffee}\n--- 축하합니다 ---")


#if
weather = input("오늘 날씨는 어때요?")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("날씨가 맑아요")

temp = int(input("기온은 어때요? "))
if temp > 30:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp & temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")

#for
for waiting_number in range(1, 6):
    print("대기번호 : {0}".format(waiting_number))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}님 커피가 준비되었습니다.".format(customer))

#while
customer = "토르"
index = 5
while index >= 1:
    print("{0}님 커피가 준비 되었습니다. {1}번 남았습니다.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기 처분 되었습니다.")


customer = "토르"
person = "Unknown"

while person != customer:
    print("{0}, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")

#continue와 break
absent =  [2, 5] #결석
no_book = [7] #책을 깜빡했음
for student in range(1, 11) : # 1,2,3,4,5,6,7,8,9,10
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))

#한 줄 for
#출석 번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102 ,103, 104
students = [1,2,3,4,5]
print(students) # [1, 2, 3, 4, 5]
students = [i+100 for i in students] 
print(students) # [101, 102, 103, 104, 105]

#학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students] 
print(students) # [8, 4, 10]

#학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students) # ['IRON MAN', 'THOR', 'I AM GROOT']

'''
퀴즈) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

조건1 : 승객별 운행 소요시간은 5 ~ 50분 사이의 난수로 정해집니다.
조건2 : 당신은 소요 시간 5 ~ 15분 사이의 승객만 매칭해야 합니다.

(출력문 예제)
[O] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[O] 3번째 손님 (소요시간 : 5분)
...
[ ] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2명
'''
clients = [randint(5, 50) for i in range(1, 51)]
count = 0
check = ""
index = 1
for client in clients :
    if client >= 5 and 15 >= client:
        count += 1
        check = "O"
    else:
        check = " "
    print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(check, index, client))
    index += 1
print("총 탑승 승객 : {0}명".format(count))


#함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")
open_account()

#전달값과 반환값
def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money: # 잔액이 출금보다 많으면
        print("출금이 완료 되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 실패 했습니다.")
        return balance

def withdraw_night(balance, money): # 저녁에 출금
    commission = 100 #수수료 100원
    return commission, balance - money - commission
balance = 0
balance = deposit(balance, 10000)
balance = withdraw(balance, 2000)
balance = withdraw(balance, 10000)
commission, balance = withdraw_night(balance, 500)

print("수수료는 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))

#기본값
def profile(name, age, main_lang):
    print("이름 : {0} \n나이 : {1} \n주 사용 언어 : {2}".format(name, age, main_lang))

profile("유재석", 20, "자바")
profile("김태호", 25, "파이썬")

#같은 학교 같은 학년 같은 반 같은 수업
def profile_default_value(name, age=17, main_lang="파이썬"):
    print("이름 : {0} \n나이 : {1} \n주 사용 언어 : {2}".format(name, age, main_lang))
profile_default_value("유재석")
profile_default_value("김태호")

#키워드값
def profile_keyword(name, age, main_lang):
    print("이름 : {0} \n나이 : {1} \n주 사용 언어 : {2}".format(name, age, main_lang))

profile_keyword(name="유재석",main_lang="파이썬", age=20)
profile_keyword(age=25,main_lang="파이썬", name="김태호")

#가변인자
def profile_var(name, age, *language):
    print("이름 : {0} \n나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end =" ")
    print()

profile_var("유재석",20, "자바", "파이썬", "C", "C++", "C#")
profile_var("김태호",25, "코틀린", "스위프트")

#지역변수와 전역변수
gun = 10

def checkpoint(soldiers):
    global gun #전역공간에 잇는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
checkpoint(2) #2명이 경계근무 나감
print("남은 총 : {0}".format(gun))

gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))

'''
퀴즈) 표준 체중을 구하는 프로그램을 작성하시오

 * 표준 체중 : 각 개인의 키에 적당한 체중

 (성별에 따른 공식)
 남자 : 키(m) x 키(m) x 22
 여자 : 키(m) x 키(m) x 21

 조건1 : 표준 체중은 별도의 함수 내에서 계산
            * 함수명 : std_weight
            * 전달값 : 키(height), 성별(gender)
조건2 : 표준 체중은 소수점 둘째자리까지 표시

(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg 입니다.
'''

def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175
gender = "남자"
weight = round(std_weight(height/100, gender),2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

#표준입출력
print("Python", "Java", sep=",", end="?")
print("무엇이 더 재밌을까요?")

import sys
print("Python", "Java", file=sys.stdout) #표준 출력
print("Python", "Java", file=sys.stderr) #표준 에러

#시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기순번표
# 001, 002, 003, ...
for number in range(1, 21):
    print("대기번호 : " + str(number).zfill(3)) 

answer = input("아무 값이나 입력하세요 : ")
print(type(answer)) #<class 'str'>
print("입력하신 값은 " + answer + "입니다.")

#다양한 출력포맷
#빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
#양수일 떈 +표시 음수일때 - 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
#왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_<+10}".format(500)) # +500______
# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(100000000000)) # 100,000,000,000
# 3자리 마다 콤마를 찍어주기, +-부호 붙이기
print("{0:+,}".format(100000000000))
print("{0:+,}".format(-100000000000))
# 3자리 마다 콤마를 찍어주기, +-부호 붙이기, 자릿수 확보하기
#돈이 많으면 행복하니까 빈자리는 ^로 채워주기
print("{0:^<+30,}".format(-100000000000)) # -100,000,000,000^^^^^^^^^^^^^^
#소수점 출력
print("{0}".format(5/3)) # 1.6666666666666667
print("{0:f}".format(5/3)) # 1.666667
#소수점 특정 자리수 까지만 표시
print("{0:.2f}".format(5/3)) # 1.67

#파일 입출력
#score.txt파일을 쓰기목적으로 열고 utf-8로 인코딩 덮어쓰기 형태
score_file = open("score.txt", "w", encoding="utf-8") 
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

#파일을 이어서 작성하기 append
score_file = open("score.txt", "a", encoding="utf-8")
score_file.write("과학 : 80")
score_file.write("\n코드 : 100")
score_file.close()

#파일의 내용을 읽어오기(전체)
score_file = open("score.txt", "r", encoding="utf-8")
print(score_file.read())
score_file.close()

#한줄씩
score_file = open("score.txt", "r", encoding="utf-8")
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()

#반복 줄읽기
score_file = open("score.txt", "r", encoding="utf-8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()

#리스트로 처리
score_file = open("score.txt", "r", encoding="utf-8")
lines = score_file.readlines()  #list 형태로 저장
for line in lines:
    print(line)
score_file.close()

#pickle (프로그램 상 데이터를 파일 형태로 저장)
import pickle
profile_file = open("profile.pickle", "wb")
profile = {"이름":"박명수","나이":30,"취미":["축구","골프","코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) #file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()

#with
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf-8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf-8") as study_file:
    print(study_file.read())

'''
퀴즈) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

- X 주차 주간보고 -
부서 : 
이름 : 
업무 요약 :

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오

조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.
'''

for i in range(1, 51):
    file_name = str(i) + "주차.txt"
    with open(file_name, "w", encoding="utf-8") as report_file:
        report_file.write("- {0} 주차 주간보고 - ".format(i))
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무 요약 : ")

#클래스
#마린 : 공격 유닛, 군안. 총을 쏠 수 있음
name = "마린"
hp = 40
damage = 5

print("{0} 유닛이 생성되었습니다.".format(name))
print("체력{0}, 공격력 {1}\n".format(hp, damage))

#탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데 일반 모드/ 시즈 모드.
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력{0}, 공격력 {1}\n".format(tank_hp, tank_damage))

tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank2_name))
print("체력{0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력{0}, 공격력 {1}\n".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

#멤버 변수
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

#메소드
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


firebat = AttackUnit("파이어뱃", 50, 16)
firebat.attack("5시")
firebat.damaged(25)
firebat.damaged(25)

#상속
class Unit2:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        

class AttackUnit2(Unit2):
    def __init__(self, name, hp, damage):
        Unit2.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

firebat = AttackUnit2("파이어뱃", 50, 16)
firebat.attack("5시")
firebat.damaged(25)
firebat.damaged(25)

#다중상속
class Unit3:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        

class AttackUnit3(Unit3):
    def __init__(self, name, hp, damage):
        Unit3.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

class Flyable:
    def __init__(self, flying_spped):
        self.flying_spped = Flyable

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]").format(name, location, self.flying_spped)


 class FlyableAttackUnit(AttackUnit3, Flyable):
     def __init__(self, name, hp, damage, flying_spped):
         Unit3.__init__(self, name, hp)
         Flyable.__init__(self, flying_spped)

valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")