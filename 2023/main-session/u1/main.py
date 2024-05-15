""" Uzduoties konstantos """
DUOMENU_FAILAS = "U1.txt"
REZULTATU_FAILAS = "U1rez.txt"

ZINGSNIO_ILGIS_CM = "zingsnio_ilgis_cm"
NUEITI_ZINGSNIAI = "nueiti_zingsniai"
MOKINIAI = "mokiniai"
NUEITAS_KLASES_ATSTUMAS_KM = "nueitas_klases_atstumas_km"
AKTYVIU_MOKINIU_SK = "aktyviu_mokinius_sk"

klases = {}

""" Funkcija, kuri apskaičiuoja kiekvienos klasės kategorijos visą nueitą 
atstumą kilometrais ir suskaičiuoja, kiek tos klasės kategorijos mokinių įvedė nueitų žingsnių skaičių 
kiekvieną akcijos savaitės dieną. """
def gauk_klases_nueita_atstuma_ir_aktyviu_mokiniu_sk(klase):
    aktyviu_mokinius_sk = sum([1 for mokinys in klase[MOKINIAI] if all(mokinys[NUEITI_ZINGSNIAI])])
    nueitas_klases_atstumas_km = round(sum(
        [sum(mokinys[NUEITI_ZINGSNIAI]) * mokinys[ZINGSNIO_ILGIS_CM] / 100000
         for mokinys in klase[MOKINIAI] if all(mokinys[NUEITI_ZINGSNIAI])]), 2)
    
    klase[NUEITAS_KLASES_ATSTUMAS_KM] = nueitas_klases_atstumas_km
    klase[AKTYVIU_MOKINIU_SK] = aktyviu_mokinius_sk

""" Funkcija, praeinanti pro kiekviena klase ir apskaiciuojanti klases duomenis su funkcija 'gauk_klases_nueita_atstuma_ir_aktyviu_mokiniu_sk' """
def apskaiciuok_klases_duomenis(klases):
    for klase in klases:
        gauk_klases_nueita_atstuma_ir_aktyviu_mokiniu_sk(klases[klase])

""" Atidaromas duomenu failas, visos klases issaugomos i 'klases' """
with open(DUOMENU_FAILAS, "r", encoding="utf-8") as duom_failas:
    klasiu_duom_text = duom_failas.read().split("\n")[1:]
    for klases_duom_text in klasiu_duom_text:
        klase, zingsnio_ilgis_cm, *nueiti_zingsniai = klases_duom_text.split()
        nueiti_zingsniai = [int(duomuo) for duomuo in nueiti_zingsniai]
        zingsnio_ilgis_cm = int(zingsnio_ilgis_cm)
        mokinys = {
            ZINGSNIO_ILGIS_CM: zingsnio_ilgis_cm,
            NUEITI_ZINGSNIAI: nueiti_zingsniai
        }
        rasta_klase = klases.get(klase, {MOKINIAI: []})
        rasta_klase[MOKINIAI].append(mokinys)
        klases[klase] = rasta_klase

apskaiciuok_klases_duomenis(klases)

""" visu klasiu duomenys surasomos i rezultatu faila, kaip nurodyta salygoje, t.y klasės kategorija; kiek buvo mokinių, kurie 
įvedė nueitų žingsnių skaičių kiekvieną akcijos savaitės dieną; visas tos klasės kategorijos mokinių nueitas atstumas 
kilometrais, suapvalintas iki šimtųjų. """
with open(REZULTATU_FAILAS, "w", encoding="utf-8") as rez_failas:
    galutiniai_rezultatai = ""

    for klase, klases_duom in klases.items():
        if klases_duom[AKTYVIU_MOKINIU_SK] != 0:
            galutiniai_rezultatai += f"{klase} {klases_duom[AKTYVIU_MOKINIU_SK]} {klases_duom[NUEITAS_KLASES_ATSTUMAS_KM]:.2f}\n"
    
    rez_failas.write(galutiniai_rezultatai.strip())