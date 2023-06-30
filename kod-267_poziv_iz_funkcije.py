def kub(broj):
    return broj * broj * broj

def ispis_kuba_broja(broj):
    '''Funkcija izracunava kub broja '''
    kubni_broj = kub(broj)
    
    print("Kub broja  " + str(broj) + "  je broj " + str(kubni_broj)) 

ispis_kuba_broja(5)
help(ispis_kuba_broja)