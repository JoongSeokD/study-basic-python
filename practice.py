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