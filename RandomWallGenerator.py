#!/usr/bin/env python

from PIL import Image # Import knihovny pro PIL
from random import randint # import funkce randint

class NahodnaPlocha():
	###		Zaklady			###
	# Zakladni init programu.
	def __init__(self):

		self.rozmerX = 0 # Sirka
		self.rozmerY = 0 # Vyska
		self.obrazek = "" # Samotna obrazova data
		self.nahodnaBarvaPozadi = (0, 0, 0) # Nahodne pozadi. Teoreticky tento atribut tu byt nemusi, ale uvadim jej zde pro poradek.
		self.jmenoObrazku = "" # Jmeno souboru.
		self.nahodnyStyl = 0 # Urcuje, jaky typ kresby bude funkce kreslit.
		self.paletovaProcedura = 0 # Urcuje, jaka barva z palety bude pouzita.
		self.vynucenyTvar = 0 # Tato promenna vynuti dany tvar. 
		
		###		Zakladni operace
		#self.jednotliveZpracovani() # Volani metody, ktera zpracuje jednu nahodou kresbu.
		self.paletoveZpracovani() # Volani metody, ktera vygeneruje barevnou paletu
		#self.davkoveZpracovani() # Volani davkove metody, ktera opakovane spusti cely proces.
		#self.vycetCinnosti()	# Volani metody, ktera cely proces odstartuje.

	###		Metody - zaklad	###
	def nastavVelikost(self, velX = 1920, velY = 1080): # Implicitni hodnoty, kdyz neni zadan parametr
		self.rozmerX = velX # Dosadi sirku z parametru
		self.rozmerY = velY # Dosadi vysku z parametru
		return
	
	def nahodnePozadi(self): # Metoda na nastaveni nahodne barvy pozadi.
		self.nahodnaBarvaPozadi = self.nahodnaBarva()
		return
	
	def nahodnaBarva(self): # Metoda pro nahodnou barvu.
		if self.nahodnyStyl == 0: # Specialni pripad pro cerny motiv.
			self.sed = randint(0, 200)
			self.barvaKomplet = (self.sed, self.sed, self.sed)
		elif self.nahodnyStyl == 1: # Motiv s nahodnymi barvami pro kazdy objekt zvlast.
			self.barvaKomplet = (randint(0, 255), randint(0, 255), randint(0, 255)) # Nastavi nahodnou barvu.
		elif self.nahodnyStyl == 2: # Cerveny motiv
			self.barvaKomplet = (randint(50, 255), randint(0, 25), randint(0, 25)) # Nastavi odstiny pro cervenou.
		elif self.nahodnyStyl == 3: # Zeleny motiv
			self.barvaKomplet = (randint(0, 25), randint(50, 255), randint(0, 25)) # Nastavi odstiny pro zelenou.
		elif self.nahodnyStyl == 4: # Modry motiv
			self.barvaKomplet = (randint(0, 50), randint(0, 25), randint(50, 255)) # Nastavi odstiny pro modrou.
		elif self.nahodnyStyl == 5: # Zluty motiv
			self.barvaKomplet = (randint(25, 255), randint(50, 255), randint(0, 25)) # Nastavi odstiny pro kombinaci cervene a zelene.
		elif self.nahodnyStyl == 6: # Modrozeleny motiv
			self.barvaKomplet = (randint(0, 25), randint(50, 255), randint(50, 255)) # Nastavi odstiny pro kombinaci zelene a modre.
		elif self.nahodnyStyl == 7: # Purpurovy motiv.
			self.barvaKomplet = (randint(50, 255), randint(0, 25), randint(50, 255)) # Nastavi odstiny pro kombinaci modre a cervene.
		elif self.nahodnyStyl == 8: # Fialovy motiv.
			self.barvaKomplet = (randint(50, 120), randint(0, 25), randint(200, 255)) # Nastavi odstiny pro fialovou.
		elif self.nahodnyStyl == 9: # Tyrkysovy motiv.
			self.barvaKomplet = (0, randint(150, 220), randint(220, 255)) # Nastavi odstiny pro tyrkysovou.
		#### Cerny motiv je naimplementovan zvlast.
			# Zde je uveden zvlastni radek pro zachovani prehlednosti.
		elif self.nahodnyStyl == 11: # Cerny motiv.
			self.cern = randint(0, 35)
			self.barvaKomplet = (self.cern, self.cern, self.cern) # Nastavi odstiny pro cernou.
		return self.barvaKomplet
		
	def nahodnaPruhlednost(self):
		self.nahPruhled = randint(0, 40)
		return self.nahPruhled
		
	def vypocetPruhlednosti(self, barvaSebrana, pruhlednost): # Funkce pro vypocet a pripadnou opravu pruhlednosti.
		self.cer, self.zel, self.mod = barvaSebrana
		self.cer = self.cer + pruhlednost
		self.zel = self.zel + pruhlednost
		self.mod = self.mod + pruhlednost
		self.barva = (self.cer, self.zel, self.mod)
		return self.barva
		
	def vypocetBarevnehoStylu(self): # Funkce pro vytvoreni nahodne barevne palety.
		self.nahodnyStyl = randint(0, 9)
		return
		
	def nakresliZaklad(self): # Metoda pro vykresleni pozadi obrazku.
		self.obrazek = Image.new("RGB", (self.rozmerX, self.rozmerY), self.nahodnaBarvaPozadi) # Vytvori obrazek s drive nastavenou barvou.
		return
		
	def jmenoUloz(self, pocitadlo = "vystup"): # Metoda pro nastaveni jmena obrazku a jeho nasledne ulozeni.
		self.jmenoObrazku = "NahodnyObrazek_%s.jpg" % pocitadlo # Nahodne jmeno.
		self.obrazek.save(self.jmenoObrazku, quality = 100) # Ulozi obrazek.
		return
		
	def vycetCinnosti(self, pocitadlo = "NahodnyObrazek.jpg"): # Metoda, ktera pusti cely proces zpracovani.
		if self.paletovaProcedura == 0: # Podminka pro paletovou proceduru.
			self.vypocetBarevnehoStylu() 
		self.nastavVelikost() # Nastavi velikost.
		if self.nahodnyStyl == 10: # Podminka pro tmave pozadi
			self.nahodnaBarvaPozadi = (0, 0, 0)
			self.vypocetBarevnehoStylu()
		else:
			self.nahodnePozadi() # Kdyz je jinak, bude kreslit nahodnou barvu pozadi.
		self.nakresliZaklad()
		self.nahodnyPocetTvaru()
		self.jmenoUloz(pocitadlo)
		return
		
	def davkoveZpracovani(self): # Tato metoda provede davkove zpracovani.
		for inc in range(15):
			self.vycetCinnosti(inc + 1)
		return
	
	def paletoveZpracovani(self): # Tato metoda postupne vytvori nahodne obrazky dle barev.
		self.paletovaProcedura = 1
		for inc in range(11 + 1):
			self.nahodnyStyl = inc
			self.vycetCinnosti(inc)
		return
		
	def jednotliveZpracovani(self):
		self.nahodnyStyl = randint(0, 11)
		self.vynucenyTvar = 3
		self.vycetCinnosti("vystup")
			
	###		Konec zakladnich metod.		###
	#######################################
	###		Zacatek kreslicich metod.	###
	
	def vykreslovaciFunkce(self, pozX, pozY, barva, pruhlednost): # Tato funkce dela nejvice prace - vykresluje.
		if (pruhlednost > 7) and (pruhlednost < 33):
			self.barvaSebrana = self.obrazek.getpixel((pozX, pozY))
			self.novaBarva = self.vypocetPruhlednosti(self.barvaSebrana, pruhlednost)
			self.obrazek.putpixel((pozX, pozY), self.novaBarva)
		else:
			self.obrazek.putpixel((pozX, pozY), barva)
		return
		
	def nahodnyTypTvaru(self): # Metoda pro vypocet nahodne pravdepodobnosti pro tvar. Vrati cislo do funkce.
		self.nahodnyTvar = randint(1, 3)
		#self.nahodnyTvar = 0
		return self.nahodnyTvar

	def nahodnyPocetTvaru(self): # Metoda na vytvoreni nahodne cetnosti. TODO: Vyres nahodnosti ostatnich typu objektu.
		self.nahodnost = randint(15, 40)
		for inc in range(self.nahodnost):
			self.nakresliTvar() # DEBUG: Pro zapnuti for cyklu odkomentuj for cyklus a posun funkci do tela cyklu.
		return
	
	def nahodnaPoziceObjektu(self): # Metoda pro nahodne umisteni noveho objektu.
		self.startX = 0
		self.startY = 0 # Implicitni nastaveni pozici na 0, aby program nekoncil chybou.
		while self.startX == 0 or self.startX >= self.rozmerX:
			self.startX = randint(0, self.rozmerX)
			#DEBUG print "Start X:", self.startX
		while self.startY == 0 or self.startY >= self.rozmerY:
			self.startY = randint(0, self.rozmerY)
			#DEBUG print "Start Y:", self.startY
		return (self.startX, self.startY)
		
	def nahodnaOrientaceObjektu(self): # Metoda pro nahodnou orientaci objektu. Plati pro asymetricke objekty.
		self.orientace = randint(1, 2)
		return self.orientace
		
	def nahodnaVelikostObjektu(self): # Metoda pro nahodnou velikost daneho objektu.
		self.velikostX = 0
		self.velikostY = 0 # Implicitni nastaveni velikosti na 0, aby program nekoncil chybou.
		while self.velikostX < 30:
			self.velikostX = randint(0, self.rozmerX)
			#DEBUG print "Velikost X:", self.velikostX
		while self.velikostY < 10:
			self.velikostY = randint(0, self.rozmerY)
			#DEBUG print "Velikost Y:", self.velikostY
		return (self.velikostX, self.velikostY)
		
	def nakresliTvar(self): # Zakladni kreslici funkce.
		self.barva = self.nahodnaBarva()
		self.nahPruhled = self.nahodnaPruhlednost()
		self.startX, self.startY = self.nahodnaPoziceObjektu()
		self.velikostX, self.velikostY = self.nahodnaVelikostObjektu()
		if self.vynucenyTvar == 0:
			self.nahodTvar = self.nahodnyTypTvaru()
		else:
			self.nahodTvar = self.vynucenyTvar
		self.orientace = self.nahodnaOrientaceObjektu()
		self.hlavniVykreslivaciFunkce(self.barva, self.nahPruhled, self.startX, self.startY, self.velikostX, self.velikostY, self.nahodTvar, self.orientace)
		return
	
	###		Konec pomocnych metod.		###
	#######################################
	###		Hlavni vykreslovaci funkce	###
	#	Tato funkce sjednocuje veskere vykreslovaci metody do jedne.
	
	def hlavniVykreslivaciFunkce(self, barva, pruhlednost, startX, startY, velikostX, velikostY, tvar, orientace):
		if tvar == 2: # Prepis velikosti pro kruh, jelikoz nelze delat elipsu.
			velikostY = velikostX
			velikostX = velikostX / 2
		if tvar == 3: # Prepis velikosti pro trojuhelnik.
			velikostY = velikostX 
		
		for enc in range(startX, velikostX + startX):
			if enc >= self.rozmerX:
				break
			else:
				for inc in range(startY, velikostY + startY):
					if inc >= self.rozmerY:
						break
					else:
						if tvar == 1: # Podminka pro ctverec.
							self.vykreslovaciFunkce(enc, inc, barva, pruhlednost)
						elif tvar == 2: # Podminka pro kruh.
							if (enc - (velikostX / 2 + startX)) ** 2 + (inc - (velikostX / 2 + startY)) ** 2 <= ((velikostX / 2) ** 2):
								self.vykreslovaciFunkce(enc, inc, barva, pruhlednost)
						elif tvar == 3: # Podminka pro trojuhelnik.
							if orientace == 1:
								if enc + inc <= (velikostX + startX):
									self.vykreslovaciFunkce(enc, inc, barva, pruhlednost) 
							elif orientace == 2:
								if (enc + inc) - startX > (velikostY * 2):
									self.vykreslovaciFunkce(enc, inc, barva, pruhlednost)

		return	# Konec hlavni vykreslovaci funkce.

if __name__ == "__main__":
	nahodna = NahodnaPlocha()
