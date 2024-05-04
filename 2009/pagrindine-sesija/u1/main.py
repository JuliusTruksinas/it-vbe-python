""" Uzduoties konstantos """
DUOMENU_FAILAS = "U1.txt"
REZULTATU_FAILAS = "U1rez.txt"

""" Funkcija, apskaiciuojanti kiek kiekvieno nominalo monetu gaus studentas uz turimus pinigus """
def apskaiciuok_nominalu_kiekius(pinigai, surikiuoti_mazejanciai_nominalai):
    monetu_kiekiai = {nominalas: 0 for nominalas in surikiuoti_mazejanciai_nominalai}
    for nominalas in surikiuoti_mazejanciai_nominalai:
        while pinigai - nominalas >= 0:
            pinigai -= nominalas
            monetu_kiekiai[nominalas] += 1
    return monetu_kiekiai

""" Funkcija, kuri suraso visus duomenis i rezultatu faila taip, kaip nurodyta salygoje """
def irasyk_rezultatus(gilijos_studento_konvertuoti_kiekiai, eglijos_studento_konvertuoti_kiekiai):
    galutiniai_rezultatai = ""
    for k, v in gilijos_studento_konvertuoti_kiekiai.items():
        galutiniai_rezultatai += f"{k} {v}\n"
    galutiniai_rezultatai += f"{sum(gilijos_studento_konvertuoti_kiekiai.values())}\n"

    for k, v in eglijos_studento_konvertuoti_kiekiai.items():
        galutiniai_rezultatai += f"{k} {v}\n"
    galutiniai_rezultatai += f"{sum(eglijos_studento_konvertuoti_kiekiai.values())}\n"
    
    with open(REZULTATU_FAILAS, "w", encoding="utf-8") as rez_failas:
        rez_failas.write(galutiniai_rezultatai.strip())


with open(DUOMENU_FAILAS, "r", encoding="utf-8") as duom_failas:
    visos_eilutes = duom_failas.read().strip().split("\n")

""" Gauname abieju studentu valstybes nominalus, monetu kiekius, kuriuos turi studentai ir kiek is viso pinigu jie turi """
gilijos_nominalu_sarasas = [int(d) for d in visos_eilutes[1].split()]
gilijos_studento_monetu_kiekiai = [int(d) for d in visos_eilutes[2].split()]
gilijos_studento_visi_pinigai = sum([item[0] * item[1] for item in zip(gilijos_nominalu_sarasas, gilijos_studento_monetu_kiekiai)])

eglijos_nominalu_sarasas = [int(d) for d in visos_eilutes[4].split()]
eglijos_studento_monetu_kiekiai = [int(d) for d in visos_eilutes[5].split()]
eglijos_studento_visi_pinigai = sum([item[0] * item[1] for item in zip(eglijos_nominalu_sarasas, eglijos_studento_monetu_kiekiai)])

""" Apskaiciuojame, kiek ir kokiu nominalu monetu kiekvienas studentas tures, kai konvertuos i kitos valstybes valiuta """

gilijos_studento_konvertuoti_kiekiai = apskaiciuok_nominalu_kiekius(gilijos_studento_visi_pinigai, eglijos_nominalu_sarasas)
eglijos_studento_konvertuoti_kiekiai = apskaiciuok_nominalu_kiekius(eglijos_studento_visi_pinigai, gilijos_nominalu_sarasas)

""" Duomenys irasomi i rezultatu faila """
irasyk_rezultatus(gilijos_studento_konvertuoti_kiekiai, eglijos_studento_konvertuoti_kiekiai)