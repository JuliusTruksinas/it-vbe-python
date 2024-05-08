""" Uzduoties konstantos """
DUOMENU_FAILAS = "U1.txt"
REZULTATU_FAILAS = "U1rez.txt"
SKAICIO_ILGIS = 6
ILIPUSIU_KELEIVIU_SK = "ilipusiu_keleiviu_sk"
ISLIPUSIU_KELEIVIU_SK = "islipusiu_keleiviu_sk"

marsrutai = {}

""" Atidaromas duomenu failas, perskaitomi duomenys ir issaugojami visi marsrutai
key - marsruto nr; value - ilipusiu, islipusiu zmoniu sk(dict) """

with open(DUOMENU_FAILAS, "r", encoding="utf-8") as duom_failas:
    for eilute in duom_failas.read().strip().split("\n")[1:]:
        marsruto_nr, keleiviu_kiekis = [int(d) for d in eilute.split()]
        marsrutas = marsrutai.get(marsruto_nr, {ILIPUSIU_KELEIVIU_SK: 0, ISLIPUSIU_KELEIVIU_SK: 0})

        if keleiviu_kiekis < 0:
            marsrutas[ISLIPUSIU_KELEIVIU_SK] += keleiviu_kiekis
        else:
            marsrutas[ILIPUSIU_KELEIVIU_SK] += keleiviu_kiekis

        marsrutai[marsruto_nr] = marsrutas

marsrutu_items = marsrutai.items()

""" Marsrutai, isrikiuojami pagal marsruto nr didejimo tvarka """
marsrutu_items_pagal_marsruto_nr = sorted(marsrutu_items, key=lambda item: item[0])

""" gaunami visi marsrutu numeriai, kuriais vaziavo bent 1 zmogus, didejimo tvarka(pagal vaziavusiu zmoniu sk.) """
marsrutai_kuriais_vaziavo_bent_1 = sorted([item[0] for item in marsrutu_items if item[1][ILIPUSIU_KELEIVIU_SK]])

""" Gauname, kiek keleiviu buvo vezta ir kiek islipo su kiekvienu marsruto nr. """
kiek_keleiviu_vezta = [item[1][ILIPUSIU_KELEIVIU_SK] for item in marsrutu_items_pagal_marsruto_nr]
kiek_keleiviu_islipo = [item[1][ISLIPUSIU_KELEIVIU_SK] for item in marsrutu_items_pagal_marsruto_nr]

""" Gauname daugiausiai zmoniu vezusio marsruto nr. """
daugiausiai_vezes_marsruto_nr = max(marsrutu_items_pagal_marsruto_nr, key=lambda item: item[1][ILIPUSIU_KELEIVIU_SK])[0]

""" Visi duomenys irasomi i duomenu faila kaip nurodyta salygoje """
with open(REZULTATU_FAILAS, "w", encoding="utf-8") as rez_failas:
    rezultatai = f"{''.join([str(el).rjust(SKAICIO_ILGIS) for el in marsrutai_kuriais_vaziavo_bent_1])}\n"
    rezultatai += f"{''.join([str(el).rjust(SKAICIO_ILGIS) for el in kiek_keleiviu_vezta])}\n"
    rezultatai += f"{''.join([str(el).rjust(SKAICIO_ILGIS) for el in kiek_keleiviu_islipo])}\n"
    rezultatai += f"{str(daugiausiai_vezes_marsruto_nr).rjust(SKAICIO_ILGIS)}"
    rez_failas.write(rezultatai)