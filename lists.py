# Boodschappenlijst maken
boodschappen = ["Brood", "Melk", "Kaas", "Eieren", "Appels"]

# Twee producten toevoegen
boodschappen.append("Bananen")
boodschappen.append("Rijst")

# Eén product verwijderen
boodschappen.remove("Kaas")

# Aantal producten tonen
print("Aantal producten:", len(boodschappen))

# Volledige boodschappenlijst tonen
print("Boodschappenlijst:", boodschappen)

# Bonus: controleren of melk in de lijst staat
if "Melk" in boodschappen:
    print("Melk staat in de lijst")
else:
    print("Melk staat niet in de lijst")