Geburtstage = {"Dennis":"19. April", "Mama": "12. Marz"}

while True:
	print("Gebe einen Namen ein:")
	eingabe=input()
	
	if eingabe=="":
		break

	if eingabe=="liste":
		print(Geburtstage)
		continue

	if eingabe in Geburtstage:
		print(eingabe+ " hat am " +Geburtstage[eingabe] + " Geburtstag!")

	else:
		print("Geburtstag nicht gefunden. Wird eingetragen!")
		print("Wann hat die person geburtstag?")
		datum=input()
		Geburtstage[eingabe] = datum
		
			
