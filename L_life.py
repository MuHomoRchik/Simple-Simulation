# class Student:
#     print("Hände hoh")
#     def __init__(self):
#         self.height = 177
#         print("U menya v jope tarakan")
#
# first_student = Student()
# print(first_student.height)

# class Student:
#     amount_of_students = 0
#     def __init__(self,height = 166):
#         # self.height = height
# german = Student()
# sasha = Student(height = 66)
#
# print(german.height)
# print(sasha.height)
# print(german.amount_of_students)

import random
class Student():
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
    def to_Study(self):
        print("Vchitisya")
        self.progress += 0.12
        self.gladness += 5
    def to_Sleep(self):
        print("Spatky")
        self.gladness -= 1
    def to_poop(self):
        print("Sraty")
        self.gladness -= 4
        self.progress -= 0.1
    def is_alive(self):
        if self.progress < -0.5:
            print("Degroid")
            self.alive = False
        elif self.gladness >= 105:
            print("Zapor")
            self.alive = False
        elif self.progress > 5:
            print("Insult")
            self.alive = False
    def end_day(self):
        print(f"Gavno = {self.gladness}")
        print(f"Rozum = {round(self.progress, 2)}")
    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_Study()
        elif live_cube == 2:
            self.to_Sleep()
        elif live_cube == 3:
            self.to_poop()
            self.end_day()
            self.is_alive()

Nig = Student(name = "Loshara")
for day in range(366):
    if Nig.alive == False:
        break
    Nig.live(day)
