#manga introductio
#main menu of manga
#options of your manga
#title of you manga

print("Welcome to Manga Hub :>")
print("Answer a few question before we proceed on type of manga's")
print("What type of genre: ")

genre = int(input('\n1.Action\n2.Romance\n3.Horror\nAnswer:'))

if genre ==  1:
    print("Welcome to the list of Action Manga's ")

elif genre ==  2:
    print("Welcome to the list of Romance Manga's ") 

elif genre ==  3:
    print("Welcome to the list of Horror Manga's ")

else:
    print("Sorry! We dont have that kind of Manga here. Try again!")

print("How long the manga should be? ")

length = input("\n1.short\n2.medium\n3.long\nAnswer:")

if length == "1":
    print("You chose short now lets proceed on decade's")

elif length == "2":
    print("You chose medium now lets proceed on decade's")

elif length == "3":
    print("You chose long now lets proceed on decade's")

else:
    print("Sorry! We dont have that kind of choices here. Try again! ")

print("What decade's it should be? ")

year = input("\n1.2000s\n2.2010s\n3.2020s\nAnswer: ")

if year == "1":
	print("You chose 2000s, Now Enjoy!")

elif year == "2":
	print("You chose 2010s, Now Enjoy!")

elif year == "3":
	print("You chose 2020s, Now Enjoy!")

else:
	print("Sorry! We dont have that kind of choices here. Try again! ")


print("Here's some recommendation for you during 2000s,2010s,2020s: ")
print("\nNaruto (1999–2014) – Masashi Kishimoto \nBleach (2001–2016) – Tite Kubo\nOne Piece (1997–present, huge in the 2000s) – Eiichiro Oda\nFullmetal\nAlchemist (2001–2010) – Hiromu Arakawa\nDeath Note (2003–2006) – Tsugumi Ohba & Takeshi Obata\nGantz (2000–2013) – Hiroya Oku\nD.Gray-man (2004–present) – Katsura Hoshino\nBlack Cat (2000–2004) – Kentaro Yabuki\nBuso Renkin (2003–2005) – Nobuhiro Watsuki\nEyeshield 21 (2002–2009) – Riichiro\nInagaki & Yusuke Murata")



