import datetime

nb_sunday_1 = 0
for year in range(1901,2001):
    for month in range(1,13):
        if datetime.datetime(year,month,1).weekday() == 6:
            nb_sunday_1 += 1
nb_sunday_1
