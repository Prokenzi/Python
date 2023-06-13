# recnici {} - dictionaries
# {kljuc}

# prazan_recnik = {}
# print(prazan_recnik)
# print(type(prazan_recnik))

karakteri_planete = {"Ime":"Milan", "Prezime":"Prokic", "Nadimak":"Proka"}
karakteri_planete["Mesto"] = "Resnik"
karakteri_planete["Mesto"] = "Kragujevac"
#del(karakteri_planete["Mesto"])

# print(karakteri_planete.keys())
# print(karakteri_planete.values())
# print(karakteri_planete.items())

# print(karakteri_planete.get('Ime'))
# print(karakteri_planete.get('Dragi','Nema vrednosti'))

# karakteri_planete.setdefault('Vinograd','Prokupac')
# print(karakteri_planete)
obrisan_karater = karakteri_planete.pop('Nadimak')
print(obrisan_karater)


karakteri_planete2 = {"Rajko":"Rale", "Drakce":"Dragi"}
karakteri_planete.update(karakteri_planete2)
print(karakteri_planete)
print(len(karakteri_planete))