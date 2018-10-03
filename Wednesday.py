# Julian Conneely 25/09/18
# updated with correct repo path

import datetime #imported the library

today = datetime.datetime.today()   #created variables and assigned them values
dayofweek =  today.weekday()

print("Lets check if its Wednesday")

if dayofweek == 2:
    print("It's Wednesday!")
elif dayofweek ==1:
    print("Its not Wednesday")
    print("But luckily it will be Wednesday tomoro")
else:
    print("Unfortunately, it's not Wed.")

print("Thanks for checking if its Wednesday")