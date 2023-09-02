class User:
  
  def __init__(self, user_name, user_age, user_addrass, user_my_image, user_gole, user_favorit_food):
    self.name = user_name
    self.age = user_age
    self.address = user_addrass
    self.my_image = user_my_image
    self.gole = user_gole
    self.favorit_food = user_favorit_food
  
  def Age_plus(self):
    # 나이 한살 먹는다
    self.age += 1
    
  def change_address(self, change_address):
    # 주소변경 
    self.address = change_address
    
  def Food(self, food):
    self.favorit_food.append(food)
  
  def eat_my_food(self):
    print("goodd my food {Food}")
    


