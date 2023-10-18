import os 

f = open("test.kml", "r")
begin = False

for x in f:
    if begin == False:
        if x == "<coordinates>":
            begin = True
        elif x == "</coordinates>":
            begin = False
        break

    if begin == True:
        x.split(",")
        print(x[2])