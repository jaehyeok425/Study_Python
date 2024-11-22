import random

computer, user = 0, 0
count = 0

while True :
    computer = random.randint(1,10)
    count += 1
    user= int(input("컴퓨터가 생각하는 숫자는? :"))
    
    if computer == user:
        print(count,"번 만에 맞춤")
        break
    else:
        print("응 아니야")
        
print("종료")