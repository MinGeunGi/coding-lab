import random

lotto_numbers = []


value = random.randint(1, 50)


lotto_numbers = []
my_num = 1
is_ok = True
while is_ok:
  
  value = random.randint(1, 50)
  
  if value in lotto_numbers:
    continue
  lotto_numbers.append(value)
  if len(lotto_numbers) == 6:
    break
  
  
print(lotto_numbers)
  


  
  