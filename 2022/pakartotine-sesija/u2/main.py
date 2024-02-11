""" Uzduoties konstantos """
DUOMENU_FAILAS = "U2.txt"
REZULTATU_FAILAS = "U2rez.txt"
TASKAI_UZ_TEISINGA_ZODI = 1
TASKU_BAUDA_UZ_NETEISINGA_ZODI = 10
KLAIDU_KIEKIS_IKI_DISKVALIFIKAVIMO = 5
DISKVALIFIKUOTI_TEKSTAS = "Diskvalifikuoti:"

ZODZIU_SK = "zodziu_sk"
KLAIDU_SK = "klaidu_sk"
DISKVALIFIKUOTI_DALYVIAI = "diskvalifikuoti_dalyviai"
DALYVIAI_SURINKE_MAX_TASKUS = "dalyviai_surinke_max_taskus"
MAX_SURINKTI_TASKAI = "max_surinkti_taskai"
MIESTAS = "miestas"

dalyviai = {}

""" Funkcija, sudarnati daugiausia tasku surinkusiu ir diskvalifikuotu dalyviu sarasus """
def sudaryk_max_tasku_surinkusiu_ir_diskvalifikuotu_dalyviu_sarasus(dalyviai):
    gauk_taskus = lambda duomenys: duomenys[ZODZIU_SK] * TASKAI_UZ_TEISINGA_ZODI - TASKU_BAUDA_UZ_NETEISINGA_ZODI * duomenys[KLAIDU_SK]
    diskvalifikuoti_dalyviai = [vardas for vardas, duomenys in dalyviai.items() if duomenys[KLAIDU_SK] > KLAIDU_KIEKIS_IKI_DISKVALIFIKAVIMO]
    nediskvalifikuoti_dalyviai = {vardas: duomenys for vardas, duomenys in dalyviai.items() if vardas not in diskvalifikuoti_dalyviai}
    max_surinkti_taskai = gauk_taskus(max(nediskvalifikuoti_dalyviai.values(), key=gauk_taskus))
    dalyviai_surinke_max_taskus = {vardas: duomenys for vardas, duomenys in nediskvalifikuoti_dalyviai.items() if gauk_taskus(duomenys) == max_surinkti_taskai}

    return {
        DISKVALIFIKUOTI_DALYVIAI: diskvalifikuoti_dalyviai,
        DALYVIAI_SURINKE_MAX_TASKUS: dalyviai_surinke_max_taskus,
        MAX_SURINKTI_TASKAI: max_surinkti_taskai
    }

""" Funkcija, irasanti rezultatus, kaip nurodyta salygoje """
def irasyk_duomenis(dalyviai_surinke_max_taskus, diskvalifikuoti_dalyviai):
    with open(REZULTATU_FAILAS, "w", encoding="utf-8") as rez_failas:
        galutiniai_duomenys = f"{max_surinkti_taskai}\n"

        for vardas, duomenys in dalyviai_surinke_max_taskus.items():
            galutiniai_duomenys += f"{vardas} {duomenys[MIESTAS]}\n"
        if len(diskvalifikuoti_dalyviai):
            galutiniai_duomenys += f"{DISKVALIFIKUOTI_TEKSTAS}\n"
            for diskvalifikuotas_dalyvis in diskvalifikuoti_dalyviai:
                galutiniai_duomenys += f"{diskvalifikuotas_dalyvis}\n"
        rez_failas.write(galutiniai_duomenys.strip())

"""" Perskaitomi pradiniai duomenys, visi dalyviai issaugomi i 'dalyviai' zodyno struktura """
with open(DUOMENU_FAILAS, "r", encoding="utf-8") as duom_failas:
    miestu_kiekis = int(duom_failas.readline().strip())
    for _ in range(miestu_kiekis):
        miestas, dalyviu_kiekis = duom_failas.readline().split(" ")
        dalyviu_kiekis = int(dalyviu_kiekis)
        for _ in range(dalyviu_kiekis):
            vardas, zodziu_sk, klaidu_sk = duom_failas.readline().split(" ")
            zodziu_sk, klaidu_sk = int(zodziu_sk), int(klaidu_sk)

            dalyviai[vardas] = {
                ZODZIU_SK: zodziu_sk,
                KLAIDU_SK: klaidu_sk,
                MIESTAS: miestas
            }

""" Sudaromi diskvalifikuotu ir daugiausia tasku surinkusiu dalyviu sarasai """
diskvalifikuoti_dalyviai, dalyviai_surinke_max_taskus, max_surinkti_taskai = sudaryk_max_tasku_surinkusiu_ir_diskvalifikuotu_dalyviu_sarasus(dalyviai).values()

""" Daugiausia tasku surinkusiu dalyviu sarasas isrikiuojamas, pagal klaidu skaiciu didejanciai """
dalyviai_surinke_max_taskus = dict(sorted(dalyviai_surinke_max_taskus.items(), key=lambda dalyvis: dalyvis[1][KLAIDU_SK]))

""" Rezultatai irasomi i rezultatu faila, kaip nurodyta salygoje """
irasyk_duomenis(dalyviai_surinke_max_taskus, diskvalifikuoti_dalyviai)