f = open("wordlist.txt","w")

def loop():
	for x1 in a:
		if mn==1:
			f.write(x1+"\n")
		if mn==0:
			break
		for x2 in a:
			if mn==1:
				break
			if mn==2:
				f.write(x1+x2+"\n")
			for x3 in a:
				if mn==2:
					break
				if mn==3:
					f.write(x1+x2+x3+"\n")
				for x4 in a:
					if mn==3:
						break
					if mn==4:
						f.write(x1+x2+x3+x4+"\n")
					for x5 in a:
						if mn==4:
							break
						if mn==5:
							f.write(x1+x2+x3+x4+x5+"n")
						for x6 in a:
							if mn==5:
								break
							if mn==6:
								f.write(x1+x2+x3+x4+x5+x6+"\n")
							for x7 in a:
								if mn==6:
									break
								if mn==7:
									f.write(x1+x2+x3+x4+x5+x6+x7+"\n")
								for x8 in a:
									if mn==7:
										break
									if mn==8:
										f.write(x1+x2+x3+x4+x5+x6+x7+x8+"\n")
									for x9 in a:
										if mn==8:
											break
										if mn==9:
											f.write(x1+x2+x3+x4+x5+x6+x7+x8+x9+"\n")
										for x10 in a:
											if mn==9:	
												break
											if mn==10:
												f.write(x1+x2+x3+x4+x5+x6+x7+x8+x9+x10+"\n")
											for x11 in a:
												if mn==10:
													break
												if mn==11:
													f.write(x1+x2+x3+x4+x5+x6+x7+x8+x9+x10+x11+"\n")
												for x12 in a:
													if mn==11:
														break
													if mn==12:
														f.write(x1+x2+x3+x4+x5+x6+x7+x8+x9+x10++x11+x12+"\n")
													for x13 in a:
														if mn==12:
															break
														if mn==13:
															f.write(x1+x2+x3+x4+x5+x6+x7+x8+x9+x10++x11+x12+x13+"\n")
														for x14 in a:
															if mn==13:
																break
															if mn==14:
																f.write(x1+x2+x3+x4+x5+x6+x7+x8+x9+x10++x11+x12+x13+x14+"\n")
															for x15 in a:
																if mn==14:
																	break
																if mn==15:
																	f.write(x1+x2+x3+x4+x5+x6+x7+x8+x9+x10++x11+x12+x13+x14+x15+"\n")
																for x16 in a:
																	if mn==15:
																		break
																	if mn==16:
																		f.write(x1+x2+x3+x4+x5+x6+x7+x8+x9+x10++x11+x12+x13+x14+x15+x16+"\n")
																	for x17 in a:
																		if mn==16:
																			break
																		if mn==17:
																			f.write(x1+x2+x3+x4+x5+x6+x7+x8+x9+x10++x11+x12+x13+x14+x15+x16+x17+"\n")
																		for x18 in a:	
																			if mn==17:
																				break
																			if mn==18:
																				f.write(x1+x2+x3+x4+x5+x6+x7+x8+x9+x10++x11+x12+x13+x14+x15+x16+x17+x18+"\n")
																			for x19 in a:
																				if mn==18:
																					break
																				if mn==19:
																					f.write(x1+x2+x3+x4+x5+x6+x7+x8+x9+x10++x11+x12+x13+x14+x15+x16+x17+x18+x19+"\n")
																				for x20 in a:
																					if mn==19:
																						break
																					if mn==20:
																						f.write(x1+x2+x3+x4+x5+x6+x7+x8+x9+x10++x11+x12+x13+x14+x15+x16+x17+x18+x19+x20+"\n")

def info():
	print("This tool is created by -- SHUBHAM MAHADWALE\n From India\nYou can use this tool for dictionary attack\nI will update app where you will able to make any password that you want")

print("Created by --")
print("   +***+     /===\     |===\    /===|")
print("  //        / / \ \    |    \__/    |")
print("  ++++++   /=======\   |  |\____/|  |")
print("      ||  | |     | |  |  |      |  |")
print("  ****/   | |     | |  |__|      |__|")
print("Enter minlen : ")
mn=int(input())
print("Enter maxlen : ")
mx=int(input())
if mx<mn:
	print("wrong lengths")
	exit()
print("Select the character option ")
print(" 1)Capital A-Z \n 2)Small a-z \n 3)Numbers 0-9 \n 4)Capital + Small A-Z and a-z\n 5)Capital + Number A-Z and 0-9\n 6)Small + Number a-z and 0-9\n 7)All Capital,Small,Numbers A-Z and a-z and 0-9\n 8)Get information by author\nEnter option number e.g. 1 : ")
opt=int(input())

if opt==1:
		a=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

elif opt==2:
		a=['a','b','c','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

elif opt==3:
		a=['0','1','2','3','4','5','6','7','8','9']

elif opt==4:
		a=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

elif opt==5:
		a=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']

elif opt==6:
		a=['a','b','c','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']

elif opt==7:
		a=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']

elif opt==8:
	info()

else:
	print("WRONG OPTION")

while mn<=mx and opt<=8 and opt>0:
	loop()
	mn+=1
	
print("FILE CREATED AS wordlist.txt")