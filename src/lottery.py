import random



  











  
  
def lotto():
  lotto_numbers = []
  is_ok = True
  while is_ok:
    
    value = random.randint(1, 50)
  
    if value in lotto_numbers:
      continue
    lotto_numbers.append(value)
    if len(lotto_numbers) == 6:
      break
  return lotto_numbers

result = lotto()

print(result)
  
  

  


  
  