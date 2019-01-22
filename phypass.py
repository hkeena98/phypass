"""
Author: Keye Development (Henry Keena)
Date: 2/02/2018
Release: 1.0
License: MIT
"""

#Imports Random Number Generator
from random import *

#Imports Subprocesses
import subprocess as sub

#Imports OS Path For File Checking
import os.path as path

"""
Function: simp_gen(leng)
Function For Generating Simple Passwords Based On Defined Charset
"""
def simp_gen(leng):
	pasw = []
	charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_-+={}[]:;'<>?/`~|"
	charlen = len(charset)-1
	x = 0
	for x in range(leng):
		rando = randint(0, charlen)
		pasw.append(charset[rando])
	pasd = ''.join(pasw)
	return pasd

"""
Function: phrase_gen(basephrase)
Function For Generating Passwords Based Upon An Input Base Phrase
"""
def phrase_gen(basephrase):
	repA = "aA4"
	repB = "sS5"
	repC = "tT7"
	repD = "iI1"
	repE = "oO0"
	repF = "eE3"
	repG = "[]{}()<>"
	repH = "!@#$%^&*:;?`~'-=+"
	repI = "yYiI"
	charset = []
	pasw = []
	for x in range(len(basephrase)):
		charset.append(basephrase[x])
	for y in range(len(charset)):
		c = charset[y]
		if c == "a" or c == "A" or c == "4":
			a = randint(0, 2)
			pasw.append(repA[a])
		elif c == "s" or c == "S" or c == "5":
			a = randint(0, 2)
			pasw.append(repB[a])
		elif c == "t" or c == "T" or c == "7":
			a = randint(0, 2)
			pasw.append(repC[a])
		elif c == "i" or c == "I" or c == "1":
			a = randint(0, 2)
			pasw.append(repD[a])
		elif c == "o" or c == "O" or c == "0":
			a = randint(0, 2)
			pasw.append(repE[a])
		elif c == "e" or c == "E" or c == "3":
			a = randint(0, 2)
			pasw.append(repF[a])
		elif c == " " or c == "":
			pasw.append("_")
		elif c == "[" or c == "]" or c == "{" or c == "}" or c == "(" or c == ")":
			a = randint(0, 7)
			pasw.append(repG[a])
		elif c == "!" or c == "@" or c == "#" or c == "$" or c == "%" or c == "^" or c == "&" or c == "*" or c == ":" or c == ";" or c == "?" or c == "`" or c == "~" or c == "'" or c == "-" or c == "-" or c == "=" or c == "+":
			a = randint(0, 16)
			pasw.append(repH[a])
		elif c == "y" or c == "Y":
			a = randint(0, 3)
			pasw.append(repI[a])
		else:
			a = randint(0, 1)
			if a == 1:
				pasw.append(c.lower())
			else:
				pasw.append(c.upper())
	pasd = ''.join(pasw)
	return pasd

"""
Function: save_pass(in_passw)
Function That Saves Input Password For Storage / Later Use
"""
def save_pass(in_passw, exists):
	if exists == True:
		file = open("saved.txt", "a")
		file.write("\n\n"+in_passw)
		file.close()
	elif exists == False:
		file = open("saved.txt", "w")
		file.write("\nSAVED GENERATED PASSWORDS:")
		file.write("\n\n"+in_passw)
		file.close()

"""
Function: generation_dialog(opt)
Helper Function For Choosing Style Of Generation
"""
def generation_dialog(opt):
	if opt == "simp":
		while True:
			try:
				leng = int(input("\nEnter Length of Generated Password( 0 to exit )~# "))
			except ValueError:
				print("\n\nNot A Valid Input\n")
				continue
			if leng == 0:
				sub.call('clear',shell=True)
				break
			elif leng != 0:
				passw = simp_gen(leng)
				print("\nGenerated Password: ", passw)
				res = str(input("\nDo You Want To Save This Generation(y/n): "))
				if res == "y" or res == "Y":
					if path.exists("saved.txt") == True:
						save_pass(passw, True)
					elif path.exists("saved.txt") == False:
						save_pass(passw, False)		 
	elif opt == "phrase":
		while True:
			try:
				base = str(input("\nEnter Base Phrase( 0 to exit )~# "))
			except ValueError:
				print("\n\nNot A Valid Input\n")
				continue
			if base == "0":
				sub.call('clear',shell=True)
				break
			elif base != "0":
				passw = phrase_gen(base)
				print("\nGenerated Password: ", passw)
				res = str(input("\nDo You Want To Save This Generation(y/n): "))
				if res == "y" or res == "Y":
					if path.exists("saved.txt") == True:
						save_pass(passw, True)
					elif path.exists("saved.txt") == False:
						save_pass(passw, False)

"""
Function: display_saved()
Function That Displays All Previously Generated And Saved Passwords
"""
def display_saved():
	sub.call('clear',shell=True)
	if path.exists("saved.txt") == True:
		sub.call('cat saved.txt',shell=True)
		try:
    			input("\n\n\nPRESS ENTER TO CONTINUE")
		except SyntaxError:
    			pass
		sub.call('clear',shell=True)
	else:
		print("\n\nPassword Save List Does Not Exist...")
		res = str(input("\nDo You Want To Generate List File(y/n): "))
		if res == "y" or res == "Y":
			file = open("saved.txt", "w")
			file.write("\n\nSAVED GENERATED PASSWORDS:\n")
			file.close()
			print("\nList Generated\n")
		else: 
			print("\nList Not Generated\n")

"""
Function: read_me()
Function That Prints README For User
"""
def read_me():
	sub.call('clear',shell=True)
	sub.call('cat README.md',shell=True)
	try:
    		input("\n\n\nPRESS ENTER TO CONTINUE")
	except SyntaxError:
    		pass
	sub.call('clear',shell=True)

"""
Function: read_lic()
Function That Prints License Information
"""
def read_lic():
	sub.call('clear',shell=True)
	sub.call('cat LICENSE',shell=True)
	try:
    		input("\n\n\nPRESS ENTER TO CONTINUE")
	except SyntaxError:
    		pass
	sub.call('clear',shell=True)

"""
Function: main()
Main Function 
"""
def main():
	sub.call('clear',shell=True)
	print("\n\n!!!Welcome To Phypass!!!\n")
	while True:
		print("\nOptions:\n")
		print("0. Exit (0)\n")
		print("1. Simple Random Password Generation (1)\n")
		print("2. Phrase-Based Password Generation (2)\n")
		print("3. List Saved Generations (3)\n")
		print("4. README (4)\n")
		print("5. LICENSE (5)\n")
		imp = str(input("~# "))
		sub.call('clear',shell=True)
		if imp == "1":
			generation_dialog("simp")
		elif imp == "2":
			generation_dialog("phrase")
		elif imp == "3":
			display_saved()
		elif imp == "4":
			read_me()
		elif imp == "5":
			read_lic()	
		elif imp == "0":
			print("\nThank You For Using Phypass!\n")
			exit()
	
#Calls Main
if __name__ == "__main__":
	main()
