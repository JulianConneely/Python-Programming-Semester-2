# Julian Conneely 25/09/18

import datetime
today = datetime.datetime.today()
dayofweek =  today.weekday()

if dayofweek == 1:
    print("It's Tuesday!")
else:
    print("Unfortunately, it's not Tuesday.")

