#first_name = "dep"
#last_name = "trai"
#full_name = first_name +" "+ last_name
#print ("hello "+(full_name))
#print (type(full_name))

#age = 21
#age += 1
#print (age)
#print ("your age is: "+str(age))
#print (type(age))

#height = 190.5
#print ('your height is: '+str(height)+"cm")
#print (type(height))

#human = False
#print("Are you a human: "+str(human))
#print(type(human))

#MULTIPLE ASSIGNMENT:-----------------------------------------
#name = "bro"
#age = 21
#attractive = True

#name, age, attractive = "Bro", 21, True

#print (name)
#print (age)
#print (attractive)

#saitama = garou = boros = 30

#print (saitama)
#print (garou)
#print (boros)

#STRING METHOD
#name = "Bro Code"

#print (len(name))
#print (name.find("o"))  #tim thu tu chu trong dong nhat dinh
#print (name.capitalize())   
#print (name.upper())   #dau in hoa
#print (name.lower())   #dau thuong
#print (name.isdigit())  #check that is the number or not
#print (name.isalpha())  #check if the string is only alpha bet letter
#print (name.count("o"))
#print (name.replace("o","a"))   #replace the lettere you want to another letter
#print (name*3) #x3 print

#TYPE CASTING
#x = 1   #int(binh thuong) int la tinh toan dc
#y = 2.0 #float(co dau .) float se them .0 dang sau (va tinh toan dc)
#z = "3" #str(co dau "")str thi = bnhh ra dung nhu the

#y = int(y)
#z = int(z) # them int  thi co the tinh toan duoc (khong thi sex chi in 3 dau 3)

#print (x)
#print (y)
#print (z*3)

#USER INPUT

#name = input("what is your name?:  ")
#age = int(input("how old are you?:  "))
#height = float(input("how tall are you?:  "))

#print("Hello "+name)
#print("you are "+str(age)+"years old ")
#print("you are "+str(height)+"cm height")

#MATH FUNCTION

#pi = 3.14
#x = 1
#y = 2
#z = 3

#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(abs(pi))
#print(pow(pi,2))
#print(math.sqtr(420))
#print(max(x,y,z))
#print(min(x,y,z))


#indexing
#name = "Bro Code"

#first_name = name[0:3]
#last_name = name[4:]
#funky_name = name[0:8:3]
#reverse_name = name[::-1]
#print(reverse_name)

#cau lenh if
#age = int(input("how old are you?:  "))

#if age >= 18:
#    print ("you are old enough")
#elif age == 100:
#    print ("you are too old")
#else:
#    print ("you are too young")

#temp = int(input("what's the temperature: "))

#if temp >=0 and temp <= 30:
#    print ("the tenperature today is good!")
#    print ("go touch some grass!")
#elif not (temp >=0 and temp <= 30): #if/elif not la nguoc lai
#    print ("the weather is really bad")

#WHILE LOOPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
#a statement that will execute its block of code, as long as its condition remains true

#while 1==1:
#    print("help im stuck in a loop!")

#name = ""

#while len(name) == 0:               #loop bat phai dien ten bang duoc!
#    name = input("enter your name:  ")

#print("hello!" + name)

#for i in range

#for i in range(10):
#    print(i+1)

#for i in range(50,100+1,2):
#    print (i)

#for i in "Bro Code":
#    print (i)


#import time

#for seconds in range(10,0,-1):
#    print (seconds)
#    time.sleep(1)
#print("Happy new year!") 

#NESTED LOOPPPPPPPPPsssssssssssssssssssssssssssssssssss

#rows = int(input("how many rows:  "))
#columns = int(input("how many columns:  "))
#symbol = input("enter a symbol:  ")

#for i in range(rows):
#    for j in range(columns):
#        print (symbol, end="")
#    print(symbol)

#LOOP CONTROL STATEMENT (ko lam theo y muon thi loop tiep)

#break=      used to terminate the loop entirely
#continue=   skip to the next iteration of the loop
#pass=       does nothing, act as a place holder

#while True:
#    name = input("Enter your name: ")
#    if name != "":
#        break

#phone_number = "123-456-7890"

#for i in phone_number:
#    if i == "-":
#        continue
#    print(i, end="")

#for i in range(1,21):

#    if i == 13:
#        pass
#    else:
#        print (i)

#LIST = used to store multiple items in a single variable

#food = ["pizza","hambergur","hotdog","spaghetti","pudding"]

#food[0] = "sushi"
#print (food[3])
#food.append("ice cream")   (add in)
#food.remove("hotdog")      (remove)
#food.pop()                 (remove)
#food.sort()                (sort a->z theo thu tu)
#food.clear()               (xoa het trong food)

#for x in food:
#    print(x)

#2D LIST: A LIST OF LIST

#drinks = ["coffe","soda","tea"]
#dinner = ["pizza","hamburger","hotdog"]
#dessert = ["cake","ice cream"]

#food = [drinks ,dinner ,dessert]

#print(food[0][0])

#TUPLE = COLLECTION WHICH IS ORDERED AND UNCHANGEABLE
#           USED TO GROUP TOGETHER RELATED DATA

#student = ("Bro",21,'male')

#print(student.count("Bro"))
#print(student.index("male"))

#for x in student:
#    print (x)

#if "Bro" in student:
#    print("Bro is here!")

#set = collection which is unordered, unindexed. No duplicate value

#utensils = {"fork","spoon","knife"}
#dishes = {"bowl","plate", "cup","knife"}
#for x in utensils:
#    print (x)

#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear ()
#dishes.update (utensils)
#dinner_table = utensils.union(dishes)

#for x in dishes:
#    print (x)

#print(utensils.difference(dishes))
#print(utensils.intersection(dishes)) 

#DICTIONARY:    A CHANGEABLE, UNORDERED COLLECTION OF UNIQUE KEY: VALUE PAIRS
#                FAST BECAUSE THEY USE HASHING, ALLOW US TO ACCESS A VALUE QUICKLY

capitals = {'USA':'Washington DC',
            'India':'New Dehli',
            'China':'Beijing',
            'Russia':'Moscow'}

capitals.update({'Germany','Berlin'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China')
capitals.clear()
#print(capitals['Russia'])
#print(capitals.get('Germany'))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

for key,value in capitals.items():
    print(key, value)