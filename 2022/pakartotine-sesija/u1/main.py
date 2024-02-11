""" Uzduoties konstantos """
DUOMENU_FAILAS = "U1.txt"
REZULTATU_FAILAS = "U1rez.txt"
PRANESIMAS_NEPAVYKS_NUSIPIRKTI = "Nepavyks nusipirkti"

MAZIAUSIOS_PRODUKTU_KAINOS = "maziausios_produktu_kainos"
MINIMALI_SUMA = "minimali_suma"
PARDUOTUVES_KAINOS = "parduotuves_kainos"
PARDUOTUVES_PIGIAUSIOS_PREKES = "parduotuves_pigiausios_prekes"

parduotuves = {}

""" Funkcija, randanti maziausias prekiu kainas ir ju suma """
def rask_min_prekiu_kainas_ir_ju_suma(parduotuves):
    maziausios_produktu_kainos = [min([kaina for kaina in kainos if kaina > 0]) for kainos in zip(*[value[PARDUOTUVES_KAINOS] for value in parduotuves.values()])]
    
    return {
        MAZIAUSIOS_PRODUKTU_KAINOS: maziausios_produktu_kainos,
        MINIMALI_SUMA: round(sum(maziausios_produktu_kainos), 2)
    }

""" Funkcija, randanti kiekvienoje parduotuveje norimas prekes maziausiomis kainomis """
def rask_parduotuviu_pigiausias_prekes(parduotuves, maziausios_produktu_kainos, megstami_produktai):
    for parduotuves_duomenys in parduotuves.values():
        for i in range(len(megstami_produktai)):
            if parduotuves_duomenys[PARDUOTUVES_KAINOS][i] == maziausios_produktu_kainos[i]:
                parduotuves_pigiausios_prekes = parduotuves_duomenys.get(PARDUOTUVES_PIGIAUSIOS_PREKES, [])
                parduotuves_pigiausios_prekes.append(megstami_produktai[i])
                parduotuves_duomenys[PARDUOTUVES_PIGIAUSIOS_PREKES] = parduotuves_pigiausios_prekes

""" Funkcija irasanti galutinius rezultatus i rezultatu faila, kaip nurodyta salygoje """
def irasyk_rezultatus(parduotuves, biudzetas, minimali_suma):
    with open(REZULTATU_FAILAS, "w", encoding="utf-8") as rez_failas:
        if biudzetas < minimali_suma:
            rez_failas.write(PRANESIMAS_NEPAVYKS_NUSIPIRKTI)
            return
        
        galutiniai_duomenys = f"{minimali_suma:.2f}\n"

        for parduotuves_pavadinimas, parduotuves_duomenys in parduotuves.items():
            galutiniai_duomenys += f"{parduotuves_pavadinimas} {' '.join(parduotuves_duomenys[PARDUOTUVES_PIGIAUSIOS_PREKES])}\n"
        
        rez_failas.write(galutiniai_duomenys.strip())

""" Perskaitomi pradiniai duomenys, visos parduotuves issaugomos i 'parduotuves' zodyno duomenu struktura """
with open(DUOMENU_FAILAS, "r", encoding="utf-8") as duom_failas:
    pirma_eil, megstami_produktai, *parduotuves_text = duom_failas.read().split("\n")
    biudzetas = float(pirma_eil.split(" ")[-1])
    megstami_produktai = megstami_produktai.split(" ")

    for parduotuve_text in parduotuves_text:
        parduotuves_pavadinimas, *parduotuves_kainos = parduotuve_text.split(" ")
        parduotuves_kainos = [float(kaina) for kaina in parduotuves_kainos]

        parduotuves[parduotuves_pavadinimas] = {
           PARDUOTUVES_KAINOS: parduotuves_kainos
            }

""" Randamos maziausios produktu kainos ir ju suma """
maziausios_produktu_kainos, minimali_suma = rask_min_prekiu_kainas_ir_ju_suma(parduotuves).values()

""" Randamos kiekvienoje parduotuveje norimos prekes maziausiomis kainomis """
rask_parduotuviu_pigiausias_prekes(parduotuves, maziausios_produktu_kainos, megstami_produktai)

""" Ismetamos parduotuves, kurios neturi norimu prekiu maziausiomis kainomis """
parduotuves = {parduotuves_pavadinimas: parduotuves_duomenys
               for parduotuves_pavadinimas, parduotuves_duomenys in parduotuves.items()
               if parduotuves_duomenys.get(PARDUOTUVES_PIGIAUSIOS_PREKES)}

""" Partuotuves isrikiuojamos pagal turimu prekiu pigiausiomis kainomis kieki mazejanciai """
parduotuves = dict(sorted(parduotuves.items(), key=lambda item: len(item[1][PARDUOTUVES_PIGIAUSIOS_PREKES]), reverse=True))

""" Irasomi galutiniai rezultatai i rezultatu faila, kaip pateikta salygoje """
irasyk_rezultatus(parduotuves, biudzetas, minimali_suma)