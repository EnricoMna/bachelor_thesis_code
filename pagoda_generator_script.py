import bpy
import random
import math

# Definiere die minimalen und maximalen Werte für die zufällige Anordnung

def get_random_breite(min = 15, max = 45):
    return random.uniform(min, max)

def get_random_sockelhoehe(breite, min = 4, max = 30):
    if breite > 30 :
        min = 7
    if breite < 20 :
        max = 7
    return random.uniform(min, max)

def get_random_stockwerke(breite, min = 2, max = 13):
    return random.randint(min, max)

def get_random_verhaeltnis(breite, min = 0.4, max = 0.9):
    return random.uniform(min, max)

def get_random_dachtiefe(breite, min = 3):    
    return random.uniform(min, 8.5 - 0.1 * breite)

def get_random_stufenbreite(breite):
    return random.uniform(breite * 0.4, breite * 0.7)

def get_random_dachschwingung(breite):
    return 6.3 - 0.14 * breite

def get_random_exponent(breite, min = 0, max = 0.6):
    return random.uniform(min, max)

def get_random_dachsparrenanzahl(breite, min = 3, max = 30):
    return random.randint(min, max)

def get_random_erdgeschosshöhe(min = 4.5, max = 10.5, mid = 7):
    return random.choice([min, max, mid])

def get_random_balkon():
    return (bool(random.randint(0,1)))

def get_random_balkonmuster():
    return (bool(random.randint(0,1)))

def get_random_veranda():
    return (bool(random.randint(0,1)))

def get_random_verandamuster():
    return (bool(random.randint(0,1)))

def get_random_stützbalken():
    return (bool(random.randint(0,1)))

def get_random_fenster():
    return (bool(random.randint(0,1)))

def get_random_fenstereg():
    return (bool(random.randint(0,1)))

def get_random_dachsparren():
    return (bool(random.randint(0,1)))


# Wähle das Objekt "Pagode" aus
obj = bpy.data.objects.get("Pagode")

# Prüfe, ob das Objekt existiert
if obj:
    # Debugging-Informationen: Liste alle Modifier auf
    print(f"Alle Modifier für Objekt 'Pagode': {[mod.name for mod in obj.modifiers]}")
    
    # Prüfe, ob der Modifier "GeometryNodesPP" existiert
    modifier = obj.modifiers["GeometryNodesPP"]
    
    if modifier:
        print(f"Modifier 'GeometryNodesPP' gefunden. Typ: {modifier.type}")
        if modifier.type == 'NODES':
            #Erstelle zufällige Werte in festegelegtem Bereich
            breite = get_random_breite()
            sockelhoehe = get_random_sockelhoehe(breite)
            stockwerke = get_random_stockwerke(breite)
            verhaeltnis = get_random_verhaeltnis(breite)
            dachtiefe = get_random_dachtiefe(breite)
            stufenbreite = get_random_stufenbreite(breite)
            dachschwingung = get_random_dachschwingung(breite)
            exponent = get_random_exponent(breite)
            dachsparrenanzahl = get_random_dachsparrenanzahl(breite)
            erdgeschosshöhe = get_random_erdgeschosshöhe()
            balkon = get_random_balkon()
            balkonmuster = get_random_balkonmuster()
            veranda = get_random_veranda()
            verandamuster = get_random_verandamuster()
            stützbalken = get_random_stützbalken()
            fenster = get_random_fenster()
            fenstereg = get_random_fenstereg()
            dachsparren = get_random_dachsparren()
            
            
            
            #Identifier für die Attribute finden und mit diesem die Werte anpassen
            items = modifier.node_group.interface.items_tree
            # breite updaten
            identifier_breite = items["Breite"].identifier
            modifier[identifier_breite] = breite
            # stockwerke updaten            
            identifier_stockwerke = items["Stockwerke"].identifier
            modifier[identifier_stockwerke] = stockwerke            
            # sockelhöhe und stufenanzahl updaten
            identifier_sockelhoehe = items["Sockelhöhe"].identifier
            modifier[identifier_sockelhoehe] = sockelhoehe
            identifier_stufenanzahl = items["Stufenanzahl"].identifier
            modifier[identifier_stufenanzahl] = math.ceil(sockelhoehe)
            # pagodenrelation updaten            
            identifier_verhaeltnis = items["Pagodenrelation"].identifier
            modifier[identifier_verhaeltnis] = verhaeltnis
            # dachbreite updaten            
            identifier_dachtiefe = items["Dachtiefe"].identifier
            modifier[identifier_dachtiefe] = dachtiefe
            # stufenbreite updaten
            identifier_stufenbreite = items["Stufenbreite"].identifier
            modifier[identifier_stufenbreite] = stufenbreite
            # stufenbreite updaten
            identifier_dachschwingung = items["Dachschwingung"].identifier
            modifier[identifier_dachschwingung] = dachschwingung
            # exponent updaten
            identifier_exponent = items["Exponent"].identifier
            modifier[identifier_exponent] = exponent
            # dachsparrenanzahl updaten
            identifier_dachsparrenanzahl = items["Dachsparrenanzahl"].identifier
            modifier[identifier_dachsparrenanzahl] = dachsparrenanzahl
            # erdgeschosshöhe updaten
            identifier_erdgeschosshöhe = items["Erdgeschosshöhe"].identifier
            modifier[identifier_erdgeschosshöhe] = erdgeschosshöhe
            # balkon updaten
            identifier_balkon = items["Balkon"].identifier
            modifier[identifier_balkon] = balkon
            # balkonmuster updaten
            identifier_balkonmuster = items["Balkonmuster"].identifier
            modifier[identifier_balkonmuster] = balkonmuster
            # veranda updaten
            identifier_veranda = items["Veranda"].identifier
            modifier[identifier_veranda] = veranda
            # verandamuster updaten
            identifier_verandamuster = items["Verandamuster"].identifier
            modifier[identifier_verandamuster] = verandamuster
            # stützbalken updaten
            identifier_stützbalken = items["Stützbalken"].identifier
            modifier[identifier_stützbalken] = stützbalken
            # fenster updaten
            identifier_fenster = items["Fenster"].identifier
            modifier[identifier_fenster] = fenster
            # fenstereg updaten
            identifier_fenstereg = items["Fenster EG"].identifier
            modifier[identifier_fenstereg] = fenstereg
            # dachsparren updaten
            identifier_dachsparren = items["Dachsparren"].identifier
            modifier[identifier_dachsparren] = dachsparren
            
            #Aktualisiere die Szene
            context = bpy.context
            modifier.node_group.interface_update(context)
            
            #Informationen / Debug
            print(f"Zufällige Werte gesetzt: Breite={breite}, Sockelhoehe={sockelhoehe}, Stockwerk={stockwerke}")
        else:
            raise ValueError(f"Modifier 'GeometryNodesPP' ist nicht vom Typ 'NODES', sondern {modifier.type}")
    else:
        raise ValueError("Modifier 'GeometryNodesPP' nicht gefunden")
else:
    raise ValueError("Objekt 'Pagode' nicht gefunden")
