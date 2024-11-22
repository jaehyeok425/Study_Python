# numList = [0,0,0,0]
# hap = 0

# numList[0] = int(input("숫자:"))
# numList[1] = int(input("숫자:"))
# numList[2] = int(input("숫자:"))
# numList[3] = int(input("숫자:"))

# hap = numList[0] + numList[1] + numList[2] + numList[3]

# print(hap)

# nList = []
# nList.append(0)
# nList.append(10)
# nList.append(8)
# nList.append(1)
# print(nList)

# nList=[]
# for i in range(0, 4):
#     nList.append(0)
# len(nList)

# numList= []
# count = 0
# rep = int(input("뭐 등신아"))
# for i in range(0,rep):
#     numList.append(0)
#     numList[i] = int(input("숫자:"))
#     count += 1
    
# hap = 0
# for i in range(0,len(numList)):
#     hap += numList[i]
    
# print(count,"개의","합:", hap)

# count = 0
# nList = []
# rep = int(input("반복할 횟수"))
# for i in range(0, rep, 1):
#     num = int(input(f"{i+1}번째 숫자 입력:"))
#     nList.append(num)
#     count += 1
    
# hap = 0
# for i in range(0, len(nList)):
#     hap += nList[i]
# print(count,"개의","합계:", hap)


# numlist = [10, 20, 30]
# mylist = [40, 50, 60]

# # sumlist = [0,0,0]
# # for i in range(0, 3):
# #     sumlist[i] = numlist[i] + mylist[i]
# # print(sumlist)

    
# sumlist =[]
# for i in range(0, len(numlist), 1):
#     sum = numlist[i]+mylist[i]
#     sumlist.append(sum)

# for i in range(0, len(sumlist), 1):
#     print(sumlist[i], end=' ')

#리스트 합치기
# a= [1, 2, 3, 4, 5]
# b= [6, 7, 8, 9, 10]

# a.append(b) - 값을 뒤에 추가
# print(a)

# a= [1, 2, 3, 4, 5]
# b= [6, 7, 8, 9, 10]

# a.extend(b) 객체의 요소들을 개별적으로 추가하는 함수
# print(a)

#a +=b        += 연산자를 통해서도 리스트 합병 가능
#print(a)

#리스트 index찾기, 값 존재 알기
#index - 찾고자 하는 값의 인덱스를 알고자 할 때
# a= [2,6,7,9,10]
# print(a.index(7))

# #in 키워드 
# #- 리스트 내에 해당 값이 존재하는지 확인 // value in [list] // boolean 타입으로 변환
# a= [1,2,3,4,5,10]
# b= 10
# c= b in a # c= 10 in [1,2,3,4,5,10]
# print(c)


#리스트 값 변경하기
# numlist = [1,2,3]
# numlist[1] = 200
# print(numlist)

# numlist = [1,2,3,4]
# numlist[1:2] = [200]
# print(numlist)

# numlist =[1,2,3]
# numlist[1] = [200,2001]
# print(numlist)  주의

# numlist = [10,20,30]
# numlist[2:3] = [200,201]
# print(numlist)

#리스트 값 삽입/삭제/개수 세기
#삽입  insert
# numlist = [10,20,30]
# numlist.insert(1,123)
# print(numlist)

#삭제 del - 리스트 이름을 넣으면 리스트가 통째로 삭제
# numlist = [10,20,30]
# del(numlist[1])
# print(numlist)

#삭제 remove 
# numlist = [10,20,30,10]
# numlist.remove(10)
# print(numlist)

#값 추출
# numlist = [10,20,30]
# print(numlist.pop(0))
# print(numlist)

#리스트에서 개수 세기
#count - 찾을 값이 몇 개인지 개수를 세서 알려줌
# numlist = [10,20,30,10,10]
# print(numlist.count(10))


#리스트 정렬/반전/복사
#sort - 값을 정렬하는 함수
# numlist = [20,10,30,50,80,60]
# numlist.sort()
# print(numlist)

# strlist = ["남국","재혁","봉중"]
# strlist.sort()
# print(strlist)

#내림차순 (reverse= True)
# strlist = ['남국','재혁','봉중']
# strlist.sort(reverse = True)
# print(strlist)

# - 인덱스 값에서 정렬x하고 내림차순
# strlist = ['남국','재혁','봉중']
# strlist.reverse()
# print(strlist)

#복사
# numlist = [10,20,30]
# numlist2= numlist.copy()
# print(numlist2)

#문자열의 특징 - 문자열은 대표적인 불변 객체로, 한번 생성되면 변화되지 않음. 변화게 하려면 list로 바꿔주면 됨
# a= 'hellow world'
# # print(a[0])
# # a[0] = 'j'

# b= 'jellow world'
# c= 'j' + a[1:]
# print(b,c)

# d= a.replace('h', 'j') #replace 함수를 써도 a 변수의 값 자체는 변하지 않음

# print(d)
# print(a)

#문자열을 리스트 변환
# a= 'hello world'
# b= list(a)
# print(b)

# c= [1,2,3]
# d= list(c)
# print(d)

#split() - 구분자로 구분되는 리스트를 반환
# a= 'hello,world,nice,weather'
# b=a.split(',')
# print(b)

#2차원 배열
# numlist2 = [[1,2,3,4],
#            [5,6,7,8],
#            [9,10,11,12]]

# for i in range(0,3):
#     for k in range(0,4):
#         print(" ", numlist2[i][k], end='')
#     print("") #줄바꿈

#값 삽입
# numlist2[1][2] = 100 
# print(numlist2)


#tuple - 읽기 전용의 리스트
# numtup = 10,
# print(numtup)

# numtup1 =(10,20,30,40)
# print(numtup1[0])

# print(numtup1[0]+numtup1[1]+numtup1[2])


#투플과 리스트의 상호 변환
# mytup = (10,20,30)
# mylist = list(mytup)
# mylist.append(40)
# mytup = tuple(mylist)
# print(mytup)


#딕셔너리
# myDict = {1:'a',2:'b',3:'c'}
# print(myDict)

# empDict = {'사번':1000,'이름':"홍길동",'부서':'케이팝'}
# # empDict['연락처'] = '010-1231-1312'
# # empDict['부서']='한빛아카데미'
# # len(empDict)
# print(list(empDict.keys()))
# print(list(empDict.values()))
# print(list(empDict.items()))

# #.get():key 값이 없어도 프로그램 다운을 막을 수 있음
# a = {'a':1,'b':2}

# print(a.get('b'))
# print(a.get('a')) #key 값이 없어도 프로그램 다운을 막을 수 있다.

# #for key in 리스트 구문은 리스트에 있는 것을 하나씩 추출해서 key
# #에 넣고 반복문을 실행하므로 같은 결과가 나옴
# for key in ['사번','이름','부서']:
#     print(key, empDict[key])
    
test_keys=['name','age','sex']
test_values=['games','10','man']
test_dict={}
    
for i in range(3):
    test_dict[test_keys[i]]=test_values[i]
    print(test_dict)
    print(len(test_dict))
