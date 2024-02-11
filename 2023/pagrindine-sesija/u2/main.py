""" Uzduoties konstantos """
DUOMENU_FAILAS = "U2.txt"
REZULTATU_FAILAS = "U2rez.txt"
SILPNAS = "Silpnas"
VIDUTINIS = "Vidutinis"
STIPRUS = "Stiprus"

ILGIS = "ilgis"
DIDZIUJU_KIEKIS = "didziuju_kiekis"
MAZUJU_KIEKIS = "mazuju_kiekis"
SKAITMENU_KIEKIS = "skaitmenu_kiekis"
SPEC_SIMBOLIU_KIEKIS = "spec_simboliu_kiekis"
IS_ANKSTO_IVESTAS = "is_anksto_ivestas"
ZYMA = "zyma"
PANASUMO_REIKSME = "panasumo_reiksme"

visi_slaptazodziai = {}

""" Funkcija, apskaiciuojanti slaptazodzio panasumo reiksme """
def apskaiciuok_panasumo_reiksme(slaptazodzio_duom, lyginamojo_slaptazodzio_duom):
    return sum([
        abs(slaptazodzio_duom[ILGIS] - lyginamojo_slaptazodzio_duom[ILGIS]),
        abs(slaptazodzio_duom[DIDZIUJU_KIEKIS] - lyginamojo_slaptazodzio_duom[DIDZIUJU_KIEKIS]),
        abs(slaptazodzio_duom[MAZUJU_KIEKIS] - lyginamojo_slaptazodzio_duom[MAZUJU_KIEKIS]),
        abs(slaptazodzio_duom[SKAITMENU_KIEKIS] - lyginamojo_slaptazodzio_duom[SKAITMENU_KIEKIS]),
        abs(slaptazodzio_duom[SPEC_SIMBOLIU_KIEKIS] - lyginamojo_slaptazodzio_duom[SPEC_SIMBOLIU_KIEKIS])
    ])

""" Funkcija, apskaiciuojanti vartotoju slaptazodziu panasumo reiksmes ir zyma """
def apskaiciuok_vartotojo_slaptazodziu_panasumo_reiksmes_ir_zyma(vartotojo_slaptazodziai, is_anksto_ivesti_slaptazodziai):
    for vartotojo_slaptazodzio_duomenys in vartotojo_slaptazodziai.values():
        maziausia_panasumo_reiksme = None
        panasiausio_slaptazodzio_duom = None

        for is_anksto_slaptazodzio_duomenys in is_anksto_ivesti_slaptazodziai.values():
            panasumo_reiksme = apskaiciuok_panasumo_reiksme(vartotojo_slaptazodzio_duomenys, is_anksto_slaptazodzio_duomenys)

            if not maziausia_panasumo_reiksme or panasumo_reiksme < maziausia_panasumo_reiksme:
                maziausia_panasumo_reiksme = panasumo_reiksme
                panasiausio_slaptazodzio_duom = is_anksto_slaptazodzio_duomenys

        vartotojo_slaptazodzio_duomenys[PANASUMO_REIKSME] = maziausia_panasumo_reiksme
        vartotojo_slaptazodzio_duomenys[ZYMA] = panasiausio_slaptazodzio_duom[ZYMA]

""" Funkcija, randanti panasiausia i vartotojo slaptazodi is is anksto ivestu slaptazodziu"""
def rask_panasiausius_slaptazodzius(vartotojo_slaptazodzio_duom, is_anksto_ivesti_slaptazodziai):
    panasiausi_slaptazodziai = []

    for is_anksto_ivestas_slaptazodis, is_anksto_slaptazodzio_duomenys in is_anksto_ivesti_slaptazodziai.items():
        if apskaiciuok_panasumo_reiksme(vartotojo_slaptazodzio_duom, is_anksto_slaptazodzio_duomenys) == vartotojo_slaptazodzio_duom[PANASUMO_REIKSME]:
            panasiausi_slaptazodziai.append(is_anksto_ivestas_slaptazodis)

    panasiausi_slaptazodziai.sort(key=lambda slaptazodis: len(slaptazodis), reverse=True) 

    return panasiausi_slaptazodziai

""" Perskaitomas duomenu failas """        
with open(DUOMENU_FAILAS, "r", encoding="utf-8") as duom_failas:
    slaptazodziai_text = duom_failas.read().split("\n")[1:]

""" Perskaitomi ir issaugomi visi slaptazodziai 'visi_slaptazodziai' zodyno strukturoje"""    
for slaptazodis_text in slaptazodziai_text:
    if len(slaptazodis_text.split(" ")) > 6:
        slaptazodzio_reiksme, *parametrai, zyma = slaptazodis_text.split(" ")
    else:
        slaptazodzio_reiksme, *parametrai = slaptazodis_text.split(" ")
        zyma = None

    ilgis, didziuju_kiekis, mazuju_kiekis, skaitmenu_kiekis, spec_simboliu_kiekis = [int(duomuo) for duomuo in parametrai]
    visi_slaptazodziai[slaptazodzio_reiksme] = {
        ILGIS: ilgis,
        DIDZIUJU_KIEKIS: didziuju_kiekis,
        MAZUJU_KIEKIS: mazuju_kiekis,
        SKAITMENU_KIEKIS: skaitmenu_kiekis,
        SPEC_SIMBOLIU_KIEKIS: spec_simboliu_kiekis,
        ZYMA: zyma
    }

""" Is visu slaptazodziu isrenkami vartotojo slaptazodziai ir is anksto ivesti slaptazodziai """
vartotojo_slaptazodziai = {key: value for key, value in visi_slaptazodziai.items() if not value[ZYMA]}
is_anksto_ivesti_slaptazodziai = {key: value for key, value in visi_slaptazodziai.items() if value[ZYMA]}

""" Apskaiciuojamos vartotoju slaptazodziu panasumo reiksmes """
apskaiciuok_vartotojo_slaptazodziu_panasumo_reiksmes_ir_zyma(vartotojo_slaptazodziai, is_anksto_ivesti_slaptazodziai)

""" I rezultatu faila irasomi rezultatai, taip kaip nurodyta salygoje """
with open(REZULTATU_FAILAS, "w", encoding="utf-8") as rez_failas:
    galutiniai_rezultatai = ""

    for vartotojo_slaptazodis, vartotojo_slaptazodzio_duom in vartotojo_slaptazodziai.items():
        galutiniai_rezultatai += f"{vartotojo_slaptazodis} {vartotojo_slaptazodzio_duom[ZYMA]} {vartotojo_slaptazodzio_duom[PANASUMO_REIKSME]}\n"
        for panasiausias_slaptazodis in rask_panasiausius_slaptazodzius(vartotojo_slaptazodzio_duom, is_anksto_ivesti_slaptazodziai):
            galutiniai_rezultatai += f"{panasiausias_slaptazodis}\n"
    
    rez_failas.write(galutiniai_rezultatai.strip())