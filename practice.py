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