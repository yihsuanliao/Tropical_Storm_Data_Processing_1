"""

Cheng Chen Yang (ccy3) 657920840
Yi Hsuan Liao (yhliao4) 661311697

We worked together via zoom screen sharing.
Yhliao4 worked on merging the files, categorize the storm, organize the output and comments.
Ccy3 worked on showing stormID, storm name, slicing year date and time, find the maximum of data, and landfall.

"""
# Reading data from file1
with open('hurdat2-1851-2019-052520.txt') as fp:
    data = fp.read()
# Reading data from file2
with open('hurdat2-nepac-1949-2019-042320.txt') as fp:
    data2 = fp.read()
# Merging two files, add the data of the second txt from next line
data += ""
data += data2
# Make an empty dictionary
dic = {}
with open('file3.txt', 'w') as fp:
    fp.write(data)
with open('file3.txt', 'r') as f:  # read the merged file
    howmanydata = 0
    year = 0
    for line in f:
        line = line.replace('\n', '')
        if line[0].isnumeric():
            if int(line[0:4]) != year:
                # slice the year out of the data
                year = int(line[0:4])
                if year in dic:
                    stormcnt = dic[year][0]  # count the storm number of each year
                    Cat1 = dic[year][1]
                    Cat2 = dic[year][2]
                    Cat3 = dic[year][3]
                    Cat4 = dic[year][4]
                    Cat5 = dic[year][5]
                else:
                    stormcnt = 0
                    Cat1 = 0
                    Cat2 = 0
                    Cat3 = 0
                    Cat4 = 0
                    Cat5 = 0
            else:
                if howmanydata == 1:
                    stormcnt = stormcnt + 1
        if line[0].isnumeric() is False and howmanydata == 0:  # distinguish if it is a new storm
            MAXwind = 0  # when detect a new storm, Max return 0
            yes = 0  # if landfall>64, the indicator return 0
            values_on_line = line.split(",")
            howmanydata = int(values_on_line[2])  # find the third column of the new storm to get the numbers of data
            print("Storm ID: {}\nStorm Name: {}".format(values_on_line[0], values_on_line[1].replace(" ", "")))
            continue  # the row of storm name does not need to calculate, so continue
        # minus 1 after read 1 row. variable "howmanydata" is for avoiding writing out results for every line
        howmanydata = howmanydata - 1
        line = line.split(",")
        wind = int(line[6])  # select the wind speed column
        # find the highest wind speed, there's no '=' because we're looking for when it first occurred (date & time)
        if wind > MAXwind:
            MAXdate = line[0]
            MAXtime = line[1]
            MAXwind = wind
        if line[2].replace(" ", "") == "L":
            if wind >= 64:
                yes = 1
        # when howmanydata == 0, means it has gone through the whole year, so print wind speed here
        if howmanydata == 0:
            if MAXwind >= 137:
                Cat5 += 1
            elif MAXwind >= 113:
                Cat4 += 1
            elif MAXwind >= 96:
                Cat3 += 1
            elif MAXwind >= 83:
                Cat2 += 1
            elif MAXwind >= 64:
                Cat1 += 1
            dic[year] = [stormcnt, Cat1, Cat2, Cat3, Cat4, Cat5]

            print("Maximum sustained wind (in knots): {}\nDate: {}\nTime: {}".format(MAXwind, MAXdate, MAXtime))
            if yes:
                print("Landfill: YES\n")  # there's landfall
            else:
                print("Landfill: NO\n")

width = 6  # fixed the width and make it right-justified
str1 = "Year".rjust(width)
str2 = "Storm".rjust(width)
str3 = "Cat1".rjust(width)
str4 = "Cat2".rjust(width)
str5 = "Cat3".rjust(width)
str6 = "Cat4".rjust(width)
str7 = "Cat5".rjust(width)
print("{} {} {} {} {} {} {}".format(str1, str2, str3, str4, str5, str6, str7))
for key in dic:
    print(str(key).rjust(width),
          str(dic[key][0]).rjust(width),
          str(dic[key][1]).rjust(width),
          str(dic[key][2]).rjust(width),
          str(dic[key][3]).rjust(width),
          str(dic[key][4]).rjust(width),
          str(dic[key][5]).rjust(width))

""" testing geograohiclib
from geographiclib.geodesic import Geodesic
geod = Geodesic.WGS84
g = geod.Inverse(0, 0, 10, 0)
print("{:.2f}".format(g['s12']))
"""