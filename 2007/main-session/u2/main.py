# task constants
DATA_FILE = "U2.txt"
RESULTS_FILE = "U2rez.txt"
NAME_LENGTH = 15
MUSHROOM_NUMBER_LENGTH = 5
PORCINI_MUSHROOMS = "baravykai"
OREGANO_MUSHROOMS = "raudonikiai"
STICKY_MUSHROOMS = "lepsiai"

def main():
    peoples_data = read_data_file()
    write_results_to_a_file(peoples_data)

# this function reads the data file and returns data of peoples' data in a dictionary:
# key: person's name; value: the amount of different mushrooms gathered
def read_data_file():
    peoples_data = {}

    with open(DATA_FILE, "r", encoding="utf-8") as data_file:
        people_count = int(data_file.readline().strip())
        for _ in range(people_count):
            person = data_file.readline().strip()
            person_name = person[:NAME_LENGTH]
            day_count = int(person[NAME_LENGTH:])
            for _ in range(day_count):
                mushrooms = [int(d) for d in data_file.readline().strip().split()]
                porcini_mushrooms, oregano_mushrooms, sticky_mushrooms = mushrooms
                found_person = peoples_data.get(person_name, {PORCINI_MUSHROOMS : 0, OREGANO_MUSHROOMS : 0, STICKY_MUSHROOMS : 0,})
                
                found_person[PORCINI_MUSHROOMS] += porcini_mushrooms
                found_person[OREGANO_MUSHROOMS] += oregano_mushrooms
                found_person[STICKY_MUSHROOMS] += sticky_mushrooms

                peoples_data[person_name] = found_person

    return peoples_data

# this function finds and returns the name and total mushroom count of a person that has gathered the most mushrooms
def get_person_with_most_mushrooms(peoples_data):
    person_with_most_mushrooms = max(peoples_data.items(), key=lambda item: sum(item[1].values()))
    return person_with_most_mushrooms[0], sum(person_with_most_mushrooms[1].values())

# this function writes the results to a file as specified in the task
def write_results_to_a_file(peoples_data):
    final_results = ""
    
    for persons_name, persons_data in peoples_data.items():
        final_results += f"{persons_name}{''.join([str(d).rjust(MUSHROOM_NUMBER_LENGTH) for d in persons_data.values()])}\n"
    
    name, total_mushroom_count = get_person_with_most_mushrooms(peoples_data)
    final_results += f"{name}{total_mushroom_count}"

    with open(RESULTS_FILE, "w", encoding="utf-8") as results_file:
        results_file.write(final_results)

main()