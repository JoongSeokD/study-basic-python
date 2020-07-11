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
print(python)