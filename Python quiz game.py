#Python quiz game
print("Welcome to the trivia on Steam Boilers\nAll the best!")
pt=0
#Question 1
print("\nQuestion 1:")
q1=print("According to application, boilers are classified into stationary and ______ boilers")
a1=input("\nPlease type your answer:")
if a1=="Mobile" or a1=="mobile":
    print("\nCorrect answer!")
    pt+=1
else:
    print("\nIncorrect answer :(")
    pt+=0
print("\nYour current score is:",pt)

#Question 2
print("\nQuestion 2:")
q2=print("Babcock and Wilcox boiler gives steam upto a pressure of 75 to __ bar")
a2=input("\nPlease type your answer:")
if a2=="80":
    print("\nCorrect answer!")
    pt+=1
else:
    print("\nIncorrect answer :(")
    pt+=0
print("\nYour current score is:",pt)

#Question 3
print("\nQuestion 3:")
q3=print("According to flow of water and flue gases, Babcock and Wilcox boiler is a _____ tube boiler")
a3=input("\nPlease type your answer:")
if a3=="Water" or a3=="water":
    print("\nCorrect answer!")
    pt+=1
else:
    print("\nIncorrect answer :(")
    pt+=0
print("\nYour current score is:",pt)

#Question 4
print("\nQuestion 4:")
q4=print("In fire tube boiler, there is flow of hot gas in tube and _____ outside tube")
a4=input("\nPlease type your answer:")
if a4=="Water" or a4=="water":
    print("\nCorrect answer!")
    pt+=1
else:
    print("\nIncorrect answer :(")
    pt+=0
print("\nYour current score is:",pt)

#Question 5
print("\nQuestion 5:")
q5=print("Pressure in water tube is upto __ bar")
a5=input("\nPlease type your answer:")
if a5=="75":
    print("\nCorrect answer!")
    pt+=1
else:
    print("\nIncorrect answer :(")
    pt+=0
print("\nYour current score is:",pt)

#Question 6
print("\nQuestion 6:")
q6=print("Rate of steam production in water tube is ____")
a6=input("\nPlease type your answer:")
if a6=="High" or a6=="high":
    print("\nCorrect answer!")
    pt+=1
else:
    print("\nIncorrect answer :(")
    pt+=0
print("\nYour current score is:",pt)

#Question 7
print("\nQuestion 7:")
q7=print("Manhole is _________ in shape")
a7=input("\nPlease type your answer:")
if a7=="Elliptical" or a7=="elliptical":
    print("\nCorrect answer!")
    pt+=1
else:
    print("\nIncorrect answer :(")
    pt+=0
print("\nYour current score is:",pt)

#Question 8
print("\nQuestion 8:")
q8=print("Accesories are not mandatory and not _______ directly on boiler")
a8=input("\nPlease type your answer:")
if a8=="Mounted" or a8=="mounted":
    print("\nCorrect answer!")
    pt+=1
else:
    print("\nIncorrect answer :(")
    pt+=0
print("\nYour current score is:",pt)

#Question 9
print("\nQuestion 9:")
q9=print("Economiser increases ___________ of feed water")
a9=input("\nPlease type your answer:")
if a9=="Temperature" or a9=="temperature":
    print("\nCorrect answer!")
    pt+=1
else:
    print("\nIncorrect answer :(")
    pt+=0
print("\nYour current score is:",pt)

#Question 10
print("\nQuestion 10:")
q10=print("Steam Trap is set up ______ steam separator")
a10=input("\nPlease type your answer:")
if a10=="Before" or a10=="before":
    print("\nCorrect answer!")
    pt+=1
else:
    print("\nIncorrect answer :(")
    pt+=0
print("\nYour current score is:",pt)

#End score
print("Congratulations on completing the quiz!\nYour total score is:",pt)

