print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

tt = 0
tr = 0
tu = 0
te = 0
tl = 0
to = 0
tv = 0

names = name1.lower() + name2.lower() 
# hh next time use .count()
for x in range(0,len(names)) :
   if names[x] == "t" :
     tt += 1
for x in range(0,len(names)) :
   if names[x] == "r" :
     tr += 1
for x in range(0,len(names)) :
   if names[x] == "u" :
     tu += 1
for x in range(0,len(names)) :
   if names[x] == "e" :
     te += 1

numtrue = tt + tr + tu + te 
for x in range(0,len(names)) :
   if names[x] == "l" :
     tl += 1
for x in range(0,len(names)) :
   if names[x] == "o" :
     to += 1
for x in range(0,len(names)) :
   if names[x] == "v" :
     tv += 1

numlove = tl + to + tv + te 
total =  str(numtrue)  + str(numlove)  
if int(total) < 10 or int(total) > 90 :
  print(f"Your score is {total}, you go together like coke and mentos.") 
elif int(total) >=40 and int(total) <=50 :
  print(f"Your score is {total}, you are alright together.")
else :
  print(f"Your score is {total}.")
  
   

  