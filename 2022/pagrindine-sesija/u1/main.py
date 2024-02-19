""" Uzduoties konstantos """
DUOMENU_FAILAS = "U1.txt"
REZULTATU_FAILAS = "U1rez.txt"

VARDAS = "vardas"
SPRENDIMO_LAIKAI = "sprendimo_laikai"
SURINKTI_TASKAI = "taskai"
SUGAISTAS_LAIKAS = "sugaistas_laikas"
ISSPRESTU_UZD_KIEKIS = "issprestu_uzd_kiekis"

dalyviai = []

""" Funkcija, apsckaiciuojanti dalyvio surinktų taškų skaičių, teisingai 
išspręstų uždavinių skaičių ir šiems uždaviniams spręsti sugaištą laiką minutėmis (NURODYMAI) """
def apskaiciuok_dalyvio_rez(dalyvis, uzd_taskai, uzd_laikai):
    issprestu_uzd_kiekis = sum([1 for laikas in dalyvis[SPRENDIMO_LAIKAI] if laikas > 0])
    sugaistas_laikas = sum(dalyvis[SPRENDIMO_LAIKAI])
    surinkti_taskai = sum(
        [uzd_taskai[index] if laikas <= uzd_laikai[index] else uzd_taskai[index] // 2
         for index, laikas in enumerate(dalyvis[SPRENDIMO_LAIKAI]) if laikas > 0])
    
    dalyvis[SUGAISTAS_LAIKAS] = sugaistas_laikas
    dalyvis[SURINKTI_TASKAI] = surinkti_taskai
    dalyvis[ISSPRESTU_UZD_KIEKIS] = issprestu_uzd_kiekis

    return dalyvis

""" Atidaromas duomenu failas ir perskaitomi duomenys """
with open(DUOMENU_FAILAS, "r", encoding="utf-8") as duom_failas:
    uzd_kiekis, uzd_laikai, uzd_taskai, *dalyviai_text = duom_failas.read().split("\n")

    uzd_kiekis = int(uzd_kiekis)
    uzd_laikai = [int(duomuo) for duomuo in uzd_laikai.split()]
    uzd_taskai = [int(duomuo) for duomuo in uzd_taskai.split()]

""" Praeinama pro kiekvieno dalyvio duomenis, ju rezultatai apskaiciuojami su funkcija 'apskaiciuok_dalyvio_rez'
ir kiekvienas dalyvis (zodyno struktura) yra pridedamas i dalyviu sarasa 'dalyviai' """
for dalyvis_text in dalyviai_text:
    dalyvio_duom = dalyvis_text.split()
    sprendimo_laikai = [int(duomuo) for duomuo in dalyvio_duom[-uzd_kiekis:]]
    vardas = " ".join(dalyvio_duom[:-uzd_kiekis])

    dalyviai.append(
        apskaiciuok_dalyvio_rez({
            VARDAS: vardas,
            SPRENDIMO_LAIKAI: sprendimo_laikai
        }, uzd_taskai, uzd_laikai))

""" Randamas daugiausiai surinktu tasku skaicius """
daugiausiai_tasku = max(dalyviai, key=lambda dalyvis: dalyvis[SURINKTI_TASKAI])[SURINKTI_TASKAI]

""" Atrenkami tik tie dalyviai kurie surinko daugiausiai tasku """
dalyviai = [dalyvis for dalyvis in dalyviai if dalyvis[SURINKTI_TASKAI] == daugiausiai_tasku]

""" Dalyviai isrikiuojami pagal issprestu uzdaviniu kieki mazejanciai, kaip nurodyta salygoje """
dalyviai.sort(key=lambda dalyvis: dalyvis[ISSPRESTU_UZD_KIEKIS], reverse=True)

""" Visi duomenys irasomi i duomenu faila kaip nurodyta salygoje """
with open(REZULTATU_FAILAS, "w", encoding="utf-8") as rez_failas:
    galutiniai_rezultatai = f"{daugiausiai_tasku}\n"
    
    for dalyvis in dalyviai:
        galutiniai_rezultatai += f"{dalyvis[VARDAS]} {dalyvis[ISSPRESTU_UZD_KIEKIS]} {dalyvis[SUGAISTAS_LAIKAS]}\n"

    rez_failas.write(galutiniai_rezultatai.strip())