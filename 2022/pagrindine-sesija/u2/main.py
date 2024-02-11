""" Uzduoties konstantos """
DUOMENU_FAILAS = "U2.txt"
REZULTATU_FAILAS = "U2rez.txt"
RYTAS = "Rytas"
DIENA = "Diena"
VAKARAS = "Vakaras"
SUGAISTAS_LAIKAS = "sugaistas_laikas"
DIENU_KIEKIS = "dienu_kiekis"

pratimai = {}

""" Funkcija, sudaranti pratimų unikalių (nepasikartojančių) pavadinimų sąrašą. """
def gauk_unikalius_pavadinimus(pavadinimai):
    return list(set(pavadinimai))

""" Perskaitomas duomenu failas """
with open(DUOMENU_FAILAS, "r", encoding="utf-8") as duom_failas:
    dienu_duom = duom_failas.read().split("\n")[1:]
    for dienos_duom_text in dienu_duom:
        """ saugomi visi atlikti pratimai dienoje (iskaitant pasikartojancius) """
        atlikti_pratimai = []
        pratimu_sk, *dienos_duom = dienos_duom_text.split(" ")

        for i in range(0, int(pratimu_sk)*3, 3):
            pavadinimas, dienos_metas, pratimo_min = dienos_duom[i:i+3]
            pratimas = pratimai.get(pavadinimas, {
                RYTAS: 0,
                DIENA: 0,
                VAKARAS: 0,
                SUGAISTAS_LAIKAS: 0,
                DIENU_KIEKIS: 0
            })

            pratimas[dienos_metas] += 1
            pratimas[SUGAISTAS_LAIKAS] += int(pratimo_min)
            pratimai[pavadinimas] = pratimas
            atlikti_pratimai.append(pavadinimas)

        """ Su funkcija 'gauk_unikalius_pavadinimus' gaunamas unikalių (nepasikartojančių) pavadinimų sąrašas """
        atlikti_pratimai = gauk_unikalius_pavadinimus(atlikti_pratimai)
        for atliktas_pratimas in atlikti_pratimai:
            pratimai[atliktas_pratimas][DIENU_KIEKIS] += 1

pratimai = dict(sorted(pratimai.items(), key=lambda pratimas: pratimas[0]))

with open(REZULTATU_FAILAS, "w", encoding="utf-8") as rez_failas:
    galutiniai_rezultatai = ""

    for pavadinimas, duomenys in pratimai.items():
        galutiniai_rezultatai += f"{pavadinimas} {duomenys[DIENU_KIEKIS]} {duomenys[SUGAISTAS_LAIKAS]}\n"

        for duomuo, kiekis in duomenys.items():
            if kiekis > 0 and duomuo not in [SUGAISTAS_LAIKAS, DIENU_KIEKIS]:
                galutiniai_rezultatai += f"{duomuo} {kiekis}\n"

    rez_failas.write(galutiniai_rezultatai.strip())