Croissantje = 39
Aantalcroissantjes = int(input('aantal croissantjes'))
Stokbrood = 278
Aantalstokbrooden = int(input('aantal stokbroden'))
Kortingsbon = 50
Aantalbonnen = int(input('aantal bonnen'))

bedrag = ((Aantalcroissantjes*Croissantje)+(Aantalstokbrooden*Stokbrood)-(Aantalbonnen*Kortingsbon)) / 100

uitkomst = 'De feestlunch kost je bij de bakker ' + str( bedrag ) + ' euro voor de croissantjes en de stokbroden als de kortingsbonnen nog geldig zijn!'

print(uitkomst)