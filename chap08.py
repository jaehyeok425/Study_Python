# def test():
#     print('What a wonderful world')
#     print('Have a good day')
    
#     return 100
# a= test()
# print(a)


#반환 값이 2개 있는 함수
# def func3():
#     result1 = 100
#     result2 = 200
#     return result1, result2

# hap1, hap2 = 0,0

# hap1, hap2 = func3()
# print("func3()에서 돌려준 값 ==>", hap1, hap2)



#투플로 변환 되는거 조심
# def add_mul(x,y):
#     s = x+y
#     m = x*y
#     return s, m
    
# c,d = add_mul(20,3)
# print(c,d)


# def add_mal2(x,y):
#     s = x+y
#     m = x*y

# a = add_mal2(20,3)
# print(type(a))

# def myFunc():
#     pass
# if True:
#     pass
# else:
#     print("거짓말 입니다.")

# 로또
# import random
# def lottoFunc():
#     lottoNum = random.randint(1,45)
#     return lottoNum

# lottoList = []
# num = 0

# print("**로또 추첨을 시작합니다.**\n")

# while True:
#     num = lottoFunc()
#     if num in lottoList:
#         continue
#     else:
#         lottoList.append(num)
        
#         if len(lottoList)==6:
#             break
# print("오늘의 로또 번호 ==>", end='')
# lottoList.sort()
# for i in range(0,6):
#     print(lottoList[i],"", end='')



# def func1():
#     a = 10
#     print("func1()에서 a의 값", a)
    
# def func2():
#     print("func2()에서 a의 값", a)
    
# a= 20
    
# func1()
# func2()


# def func1():
#     global a
#     a= 10
#     print("func1()", a)
    
# def func2():
#     print("func2()", a)
    
# a = 20

# func1()
# func2()



# 100일 후 계산
# from datetime import datetime, timedelta
# def getCurrent():
#     curDate = datetime.now()
#     return curDate

# def getAfterDate(now, day):
#     retDate = now + timedelta(days=day)
#     return retDate

# nowDate, afterDate = None, None
# nowDate = getCurrent()
# print("현재 날짜와 시간:", nowDate)
# afterDate = getAfterDate(nowDate, 100)
# print("100일 후 날짜와 시간:", afterDate)


