# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 10:00:08 2019

@author: admin
"""

#Chocolate types

d = "dark"
m = "milk"
w = "white"

print("Spongebob wanted",5,m,"chocolates,",8,w,"chocolates,""and",3,d,"chocolates")
print(d,m,w)

cadburyType1 = "milk chocolate"
cadburyType2 = "dark chocolate"
cadburyType3 = "White chocolate"

cadmilk = 5
caddark = 3
cadwhite = 8

print("there are",cadmilk, cadburyType1, "bars,", caddark, cadburyType2, "bars, and", cadwhite, cadburyType3, "bars")

#annie's code
def chocolate(D,M,W):
    print("there are",D,"dark chocolate bars,",M,"milk chocolate bars, and",W, "white chocolate bars")
    
    chocolate(5,3,8)

#dict data structure
chocolate1 = {"milk":5}
chocolate2 = {"dark":3}    
chocolate3 = {"white":8}

chocolatebox = {"milk":5,"dark":3,"white":8}

print(chocolatebox)

#creating list for students with there names and genders

def Names(S,L,V,K):
    print(S,"is",32,"years old and is male,",L,"is",28,"years old and is a female,",V,"is",45,"years old and a male,and",K,"is",38,"and is a female")
    
    Names("Steve","Lia","Vin","Katie")
    

age = {"steve":32,"Lia":28,"Vin":45,"katie":38}
gender = {"Steve":"M","Lia":"F","Vin":"M","Katie":"F"}

print()

chocolatebox = {"milk":5,"dark":3,"white":8}
print("the number of milk chocolates in chocolate box is",chocolatebox["milk"])

age = {28}
gender = {"Female"}

print("Lia is"age,",and she is",gender)

#practice code

Gender = ("Lia":"female","Steve":"Male")

import pandas
dir(pandas)

#list
chocolatebox = {"milk":5,"dark":8,"white":3}
chocolateinfo = pandas.Series.(chocolatebox)
print(chocolateinfo)

print(chocolate)

#dataframes
chocolatedata = [chocolatebox] #convert dict to list
print(chocolatedata)

chocolatedf = pandas.DataFrame(chocolatedata,  index=["quantity"]) #convet to collum
print(chocolatedf)

#Create a data from 2 dics before
students = [['Steve',32,'male'],['Lia',28,'female'],['Vin',45,'male'],['Katie',38,'female']]
df = pandas.DataFrame(students)
print(df)

df1 = pandas.DataFrame([studentallinfo])
print(df1)

df12 = pandas.DataFrame([studentallinfo], index=["age"])
print(df12)

df2 = pandas.DataFrame(students, columns=["Name","Age","Gender"])
print(df2)

data = [studentage,studentgender]
print(data)

df3 = pandas.DataFrame(data)
print(df3)





