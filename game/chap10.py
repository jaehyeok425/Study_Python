#lab 바다거북과 모래거북

# import turtle
# class SeaTurtle(turtle.Turtle):
#     name =''
#     body = None
#     def __init__(self):
#         self.body = turtle.Turtle('triangle')
#         self.body.color("blue")
#         self.name = "바다거북"
#         def swim(self, x, y):
#             self.body.goto(x,y)

#             ## 다음시간에 이어서328p
            

#상속의 구현
class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def eat(self, food):
        print('{}은 {}을 먹습니다.'.format(self.name, food))
        
    def work(self, hour):
        print('{}은{}시간 동안 일합니다.'.format(self.name, hour))
        
class Student(Person):
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        
    def work(self, hour):
        print('{}은{}시간 동안 일합니다.'.format(self.name, hour))

class Employee(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def work(self, hour):
        print('{}은{}시간 동안 일합니다.'.format(self.name, hour))
        
Teddy = Person('Teddy', 17)
Teddy.eat('bread')
Teddy.work(9)

Jenie = Student('Jenie', 18)
Jenie.eat('cake')
Jenie.work(8)

Cathy = Employee('Cathy', 19)
Cathy.eat('ice cream')
Cathy.work(7)
