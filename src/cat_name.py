import cat_class
import schedule
import time


my_cat = cat_class.Cat("kiki", 'balck')
print(my_cat.name)
print(f"{my_cat.name} 배고픔 정도 : {my_cat.needed_food_range}")


schedule.every(5).seconds.do(my_cat.changed_sick_status)
schedule.every(10).seconds.do(my_cat.hungry)

while True:
    schedule.run_pending()
    schedule.run_pending()
 
    time.sleep(1)
