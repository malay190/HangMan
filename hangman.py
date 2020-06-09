#hangman version1

import random
import string
import time


#output formatting!
print("")
print("")
print("			********************Welcome*********************")
print("			**************Let's Play Hangman****************")
print("")
print("____________")
print("Instruction:")
print("------------")
print("")
print("A game for two in which one player tries to guess the letters of a word,\nthe other player recording failed attempts by drawing a gallows and someone hanging on it,\nline by line")
print("			------------------------------------------------------------")
print("					you got maximum 9 guesses")
print("			============================================================")
print(".-----")
time.sleep(1)
print("|    |")
time.sleep(1)
print("|    O")
time.sleep(1)
print("|    |")
time.sleep(1)
print("|  ~~.~~")
time.sleep(1)
print("|    |")
time.sleep(1)
print("|   / \ ")
time.sleep(1)
print("Let's Start")
time.sleep(2)
print("")

#making lists for word slection!
animal=["panda","tiger","lion","giraffe","cat","hippo","pyhton","leopard","chameleon","camel","Chimpanzee","buffalo","butterfly"]
cricplayer=["virat","kohli","dhoni","pollard","rahul","sachin","yuvraj","sahwag","hardik","rohit","gayle","warner"]
color=["red","pink","white","yellow","black","green","voilet","maroon","purple","navy","teal","beige","orange","coral"]
car=["Nissan","Toyota"," Honda","Chevrolet","Mercedes","Volvo","Cadillac","Lexus","audi"]

#hints!
print("1.Animal")
print("2.cricplayer")
print("3.color")
print("4.car")
print("5.Exit")
choice=int(input("Enter your choice:"))	#take input from user


# function define
def animal_f():
	lista=[]
	animal_v=random.choice(animal).lower()	#select random word from list animal
	n=len(animal_v)	#find length of word
	
	for x in animal_v:	#selected word is append in new list
		lista.append(x)
	
	list=[]
	for x in range(n):
		list.append("_")
	print(" ".join(list))
	
	count=0
	sucess=0
	while count<9 and sucess<n:		
		search=input("enter your guess...")	#take a letter as input from user
		search=search.lower()
		
		if search in lista:	#if letter found in word
			index=lista.index(search)
			lista[index]="*"
			list[index]=search
			print(" ".join(list))
			print("")
			sucess+=1			
		else:
			print(" ".join(list))
			count+=1
			print((9-count),"chances remainig")
			print(" ")
				
	if count<9 and sucess==n:
		print(" ")
		print("Congrats ,you won!")
	else:
		print("")
		print("you loose..try again later")

#function define!		
def cricplayer_f():
	lista=[]
	cric_v=random.choice(cricplayer).lower()	#select random word from list cricplayer
	n=len(cric_v)
	
	for x in cric_v:	#selected word is append in new list
		lista.append(x)
	
	list=[]
	for x in range(n):
		list.append("_")
	print(" ".join(list))
	
	count=0
	sucess=0
	while count<9 and sucess<n:		
		search=input("enter your guess...")	#take a letter as input from user
		search=search.lower()
		
		if search in lista:	#chech entered letter is found in word or not
			index=lista.index(search)
			lista[index]="*"	
			list[index]=search
			print(" ".join(list))
			print("")
			sucess+=1			
		else:
			print(" ".join(list))
			count+=1
			print((9-count),"chances remainig")
			print(" ")
				
	if count<9 and sucess==n:
		print(" ")
		print("Congrats ,you won!")
	else:
		print("")
		print("you loose..try again later")

#function define!		
def color_f():
	lista=[]
	color_v=random.choice(color).lower()	#select random word from list color
	n=len(color_v)
	
	for x in color_v:	#selected word is append in new list
		lista.append(x)
	
	list=[]
	for x in range(n):
		list.append("_")
	print(" ".join(list))
	
	count=0
	sucess=0
	while count<9 and sucess<n:		
		search=input("enter your guess...")	#take a letter as input from user
		search=search.lower()
		
		if search in lista:	#chech entered letter is found in word or not
			index=lista.index(search)
			lista[index]="*"
			list[index]=search
			print(" ".join(list))
			print("")
			sucess+=1			
		else:
			print(" ".join(list))
			count+=1
			print((9-count),"chances remainig")
			print(" ")
				
	if count<9 and sucess==n:
		print(" ")
		print("Congrats ,you won!")
	else:
		print("")
		print("you loose..try again later")

#function define!		
def car_f():
	lista=[]
	car_v=random.choice(car).lower()	#select random word from list car
	n=len(car_v)
	
	for x in car_v:	#selected word is append in new list
		lista.append(x)
	
	list=[]
	for x in range(n):
		list.append("_")
	print(" ".join(list))
	
	count=0
	sucess=0
	while count<9 and sucess<n:		
		search=input("enter your guess...")	#take a letter as input from user
		search=search.lower()
		
		if search in lista:	#chech entered letter is found in word or not
			index=lista.index(search)
			lista[index]="*"
			list[index]=search
			print(" ".join(list))
			print("")
			sucess+=1			
		else:
			print(" ".join(list))
			count+=1
			print((9-count),"chances remainig")
			print(" ")
				
	if count<9 and sucess==n:
		print(" ")
		print("Congrats ,you won!")
	else:
		print("")
		print("you loose..try again later")
			
def exit_f():
	exit()
		
#corresponding function according to choice
if choice==1:	
	animal_f()
elif choice==2:
	cricplayer_f()
elif choice==3:
	color_f()
elif choice==4:
	car_f()
elif choice==5: 
	exit_f()