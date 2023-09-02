#def password(my_words):
my_words = input()
def password(my_word):
  count_upper = 0
  count_isnumeric = 0
  count_isspace = 0
  count_islower = 0
  for word in my_words:
    if word.lower:
      count_islower += 1
      
    if word.isupper:
      count_upper += 1
      
    if word.isspace:
      count_isspace += 1
      
    if word.isnumeric:
      count_isnumeric += 1
 

def password_valid(user_password):
  is_valid = True
  for word in my_words:
    if word.isspace():
      is_valid = False
  
  if len(user_password) < 8:
    is_valid

    
  
  













#print(len(my_words))


  

  
  
 
#print(f"{word}: {word.isupper()}")
  #print(f"{word}: {()}")
