import random


class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.needed_food_range = 10
        self.weight = 5
        self.sick = False

    def feed(self):
        self.needed_food_range += 5
        self.weight += 0.5
        print('맛잇다')

    def notice_sick(self):
        if self.sick == True:
            print('병원 가자')

    def changed_sick_status(self):
        sick_value = random.randint(0, 1)
        print(sick_value)
        if sick_value == 0:
            self.sick = True

        else:
            self.sick = False

    def careing(self):
        print(f"아프지마 {self.name}고양이 돌보기")
        self.sick = False 
        
    def hungry(self):
      
      
      self.needed_food_range -= 1
      if self.needed_food_range <= -10:
        print('죽음')

      elif self.needed_food_range <= 4:
        print('밥')
      
  
