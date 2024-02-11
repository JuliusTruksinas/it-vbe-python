''' Uzduoties konstantos '''
DUOMENU_FAILAS = "U1.txt"
REZULTATU_FAILAS = "U1rez.txt"
TASKU_MAKSIMUMAS = 30
ISLAIKYMO_PROCENTAS = 50

LAIKIUSIU_ZMONIU_SK= "laikiusiu_zmoniu_sk"
ISLAIKIUSIU_ZMONIU_PROCENTAS = "islaikiusiu_zmoniu_procentas"
DIDZIAUSIAS_TASKU_SK = "didziausias_tasku_sk"

""" Funkcija, apskaiciuojanti kiekvieno testo statistika, t.y laikiusiu zmoniu skaiciu, islaikiusiu zmoniu procenta,
didziausia surinkta tasku skaiciu """
def gauk_testu_statistika(testai):
    rezultatai = {}

    for testo_variantas, zmoniu_rez in testai.items():
        laikiusiu_zmoniu_sk = len(zmoniu_rez)
        islaikiusiu_zmoniu_sk = sum([1 for zmogaus_rez in zmoniu_rez if round(sum(zmogaus_rez) / TASKU_MAKSIMUMAS * 100) >= ISLAIKYMO_PROCENTAS])
        islaikiusiu_zmoniu_procentas = round(islaikiusiu_zmoniu_sk / laikiusiu_zmoniu_sk * 100)
        didziausias_tasku_sk = max([sum(zmogaus_rez) for zmogaus_rez in zmoniu_rez])

        rezultatai[testo_variantas] = {
            LAIKIUSIU_ZMONIU_SK: laikiusiu_zmoniu_sk,
            ISLAIKIUSIU_ZMONIU_PROCENTAS: islaikiusiu_zmoniu_procentas,
            DIDZIAUSIAS_TASKU_SK: didziausias_tasku_sk
        }

    return rezultatai

""" Atidaromas duomenu failas, perskaitomas ir duomenys issaugomi i dictionary tipo duomenu struktura ('testai') """
testai = {}

with open(DUOMENU_FAILAS, 'r', encoding='utf-8') as duomenu_failas:
    for rezultatai in duomenu_failas.read().split('\n')[1:]:
        numeris, var, *taskai = rezultatai.split(" ")
        testo_variantas = f"{numeris} {var}"
        taskai = [int(duomuo) for duomuo in taskai]
        testai[testo_variantas] = testai.get(testo_variantas, []) + [taskai]

""" Atidaromas rezultatu failas ir surasomi rezultatai, kaip pateikta nurodymuose, t.y:
testo variantas, laikiusiu zmoniu skaicius, islaikiusiu zmoniu procentas (suapvalintas iki sveikojo skaiciaus),
didziausias surinktas tasku skaicius """
with open(REZULTATU_FAILAS, 'w', encoding='utf-8') as rezultatu_failas:
    galutiniai_rezultatai = ''

    for testo_variantas, rezultatai in gauk_testu_statistika(testai).items():
        laikiusiu_zmoniu_sk, islaikiusiu_zmoniu_procentas, didziausias_tasku_sk = rezultatai.values()
        galutiniai_rezultatai += f"{testo_variantas} {laikiusiu_zmoniu_sk} {islaikiusiu_zmoniu_procentas}% {didziausias_tasku_sk}\n"

    rezultatu_failas.write(galutiniai_rezultatai.strip())