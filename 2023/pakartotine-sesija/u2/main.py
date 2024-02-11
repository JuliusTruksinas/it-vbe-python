''' Uzduoties konstantos '''
DUOMENU_FAILAS = "U2.txt"
REZULTATU_FAILAS = "U2rez.txt"
POPIERIUS = "P"
ZIRKLES = "Z"
AKMUO = "A"

VARDAS = "vardas"
LAIMEJIMU_SK = "laimejimu_sk"
EJIMAI = "ejimai"
PRALAIMEJIMU_SK= "pralaimejimu_sk"
SANTYKIS = "santykis"
LYGIUJIU_SK = "lygiuju_sk"

''' Funkcija, apskaiciuojanti mokinio laimejimu ir pralaimejimu santyki (simtuju tikslumu) '''
def apskaiciuok_santyki(mokinys):
    mokinys[SANTYKIS] = round(mokinys[LAIMEJIMU_SK] / mokinys[PRALAIMEJIMU_SK], 2)
    return mokinys

''' Funkcija, apskaiciuojanti mokynio rezultatus, t.y. laimejimu skaiciu, lygiuju skaiciu, pralaimejimu skaiciu '''
def apskaiciuok_rezultatus(pagrindinis_mokinys, lyginamas_mokinys):
    for index, ejimas in enumerate(pagrindinis_mokinys[EJIMAI]):
        if(ejimas == POPIERIUS and lyginamas_mokinys[EJIMAI][index] == AKMUO):
            pagrindinis_mokinys[LAIMEJIMU_SK] = pagrindinis_mokinys.get(LAIMEJIMU_SK, 0) + 1
        elif(ejimas == ZIRKLES and lyginamas_mokinys[EJIMAI][index] == POPIERIUS):
            pagrindinis_mokinys[LAIMEJIMU_SK] = pagrindinis_mokinys.get(LAIMEJIMU_SK, 0) + 1
        elif(ejimas == AKMUO and lyginamas_mokinys[EJIMAI][index] == ZIRKLES):
            pagrindinis_mokinys[LAIMEJIMU_SK] = pagrindinis_mokinys.get(LAIMEJIMU_SK, 0) + 1
        elif(ejimas == lyginamas_mokinys[EJIMAI][index]):
            pagrindinis_mokinys[LYGIUJIU_SK] = pagrindinis_mokinys.get(LYGIUJIU_SK, 0) + 1
        else:
            pagrindinis_mokinys[PRALAIMEJIMU_SK] = pagrindinis_mokinys.get(PRALAIMEJIMU_SK, 0) + 1

mokiniai = []

''' Perskaitomas duomenu failas ir duomenys surasomi i sarasa, kuriame kiekvienas elementas yra zodyno duomenu tipo,
reprezentuojantis kiekviena mokini '''
with open(DUOMENU_FAILAS, "r", encoding="utf-8") as duomenu_failas:
    for eilute in duomenu_failas.read().split("\n")[1:]:
        vardas, *ejimai = eilute.split(" ")
        mokiniai.append({
            VARDAS: vardas,
            EJIMAI: ejimai
        })

''' Palyginamas kiekvienas mokinys su kiekvienu kitu mokiniu ir apskaiciuojami ju rezultatai su "apskaiciuok_rezultatus" funkcija '''
for pagrindinis_mokinys in mokiniai:
    for lyginamas_mokinys in mokiniai:
        if pagrindinis_mokinys[VARDAS] != lyginamas_mokinys[VARDAS]:
            apskaiciuok_rezultatus(pagrindinis_mokinys, lyginamas_mokinys)

''' Duomenys isrikiuojami pagal pergaliu ir pralaimejimu santyki mazejanciai '''
mokiniai = sorted([apskaiciuok_santyki(mokinys) for mokinys in mokiniai], key=lambda mokinys: mokinys[SANTYKIS], reverse=True)

''' Duomenys suformatuojami kaip nurodyta uzduotyje ir irasomi i rezultatu faila '''
with open(REZULTATU_FAILAS, "w", encoding="utf-8") as rezultatu_failas:
    galutiniai_rezultatai = ""
    for mokinys in mokiniai:
        galutiniai_rezultatai += f"{mokinys[VARDAS]} {mokinys[SANTYKIS]:.2f} {mokinys[LYGIUJIU_SK]}\n"
    rezultatu_failas.write(galutiniai_rezultatai.strip())