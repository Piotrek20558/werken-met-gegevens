Toegangsticket = 745
Personen = int(input('aantal personen'))
Pervijfminuten = 37
Minimaletijd = 5
Aantalmin = int(input('aantal minuten'))

bedrag = ((Toegangsticket*Personen)+(Aantalmin/Minimaletijd*Pervijfminuten*Personen))  / 100

uitkomst = 'Dit geweldige dagje uit met '+ str( Personen ) + ' mensen in de Speelhal met '+ str(Aantalmin) + ' minuten VR kost je maar ' + str( bedrag ) +' euro'

print(uitkomst)