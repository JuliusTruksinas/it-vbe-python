'''Sukuriamos uzduoties konstantos'''
DUOMENU_FAILAS = "U2.txt"
REZULTATU_FAILAS = "U2rez.txt"
POPIERIUS = "P"
ZIRKLES = "Z"
AKMUO = "A"

'''Funkcija, apskaiciuojanti mokinio laimejimu ir pralaimejimu santyki (simtuju tikslumu)'''
def apskaiciuok_santyki(mokinys):
    mokinys['santykis'] = round(mokinys['laimejimu_sk'] / mokinys['pralaimejimu_sk'], 2)
    return mokinys

'''Funkcija, apskaiciuojanti mokynio rezultatus, t.y. laimejimu skaiciu, lygiuju skaiciu, pralaimejimu skaiciu'''
def apskaiciuok_rezultatus(pagrindinis_mokinys, lyginamas_mokinys):
    for index, ejimas in enumerate(pagrindinis_mokinys["ejimai"]):
        if(ejimas == POPIERIUS and lyginamas_mokinys["ejimai"][index] == AKMUO):
            pagrindinis_mokinys["laimejimu_sk"] = pagrindinis_mokinys.get("laimejimu_sk", 0) + 1
        elif(ejimas == ZIRKLES and lyginamas_mokinys["ejimai"][index] == POPIERIUS):
            pagrindinis_mokinys["laimejimu_sk"] = pagrindinis_mokinys.get("laimejimu_sk", 0) + 1
        elif(ejimas == AKMUO and lyginamas_mokinys["ejimai"][index] == ZIRKLES):
            pagrindinis_mokinys["laimejimu_sk"] = pagrindinis_mokinys.get("laimejimu_sk", 0) + 1
        elif(ejimas == lyginamas_mokinys["ejimai"][index]):
            pagrindinis_mokinys["lygiuju_sk"] = pagrindinis_mokinys.get("lygiuju_sk", 0) + 1
        else:
            pagrindinis_mokinys["pralaimejimu_sk"] = pagrindinis_mokinys.get("pralaimejimu_sk", 0) + 1

mokiniai = []

'''Perskaitomas duomenu failas ir duomenys surasomi i sarasa, kuriame kiekvienas elementas yra zodyno duomenu tipo,
reprezentuojantis kiekviena mokini'''
with open(DUOMENU_FAILAS, "r", encoding="utf-8") as duomenu_failas:
    for eilute in duomenu_failas.read().split("\n")[1:]:
        vardas, *ejimai = eilute.split(" ")
        mokiniai.append({
            "vardas": vardas,
            "ejimai": ejimai
        })

'''Palyginamas kiekvienas mokinys su kiekvienu kitu mokiniu ir apskaiciuojami ju rezultatai su "apskaiciuok_rezultatus" funkcija'''
for pagrindinis_mokinys in mokiniai:
    for lyginamas_mokinys in mokiniai:
        if pagrindinis_mokinys["vardas"] != lyginamas_mokinys["vardas"]:
            apskaiciuok_rezultatus(pagrindinis_mokinys, lyginamas_mokinys)

'''Duomenys isrikiuojami pagal pergaliu ir pralaimejimu santyki mazejanciai'''
mokiniai = sorted([apskaiciuok_santyki(mokinys) for mokinys in mokiniai], key=lambda mokinys: mokinys['santykis'], reverse=True)

'''Duomenys suformatuojami kaip nurodyta uzduotyje ir irasomi i rezultatu faila'''
with open(REZULTATU_FAILAS, "w", encoding="utf-8") as rezultatu_failas:
    galutiniai_rezultatai = ""
    for mokinys in mokiniai:
        galutiniai_rezultatai += f"{mokinys['vardas']} {mokinys['santykis']:.2f} {mokinys['lygiuju_sk']}\n"
    rezultatu_failas.write(galutiniai_rezultatai.strip())