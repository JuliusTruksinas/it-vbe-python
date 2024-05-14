# task constants
DATA_FILE = "U2.txt"
RESULTS_FILE = "U2rez.txt"
LOW_AVERAGE_LABEL = "Neatitinka vidurkis"

def main():
    subjects = read_data_file()
    write_results_to_a_file(subjects)

# this function reads the data file and returns a dictionary: key: subject name, value: list of students' names that chose that subject
# a student will be added to the list only if his average is >= 9
def read_data_file():
    subjects = {}
    with open(DATA_FILE, "r", encoding="utf-8") as data_file:
        for line in data_file.read().strip().split("\n")[1:]:
            name, subject, _, *grades = line.split()
            grades = [int(d) for d in grades]
            average = sum(grades) / len(grades)
            if average < 9:
                continue

            found_subject = subjects.get(subject, [])
            found_subject += [name]
            subjects[subject] = found_subject

    return subjects

# this function writes the results to a file as specified in the task
def write_results_to_a_file(subjects):
    final_results = ""

    sorted_subjects = sorted(subjects.items(), key=lambda item: [-len(item[1]), item[0]])
    students_count = sum([len(students) for students in subjects.values()])

    if students_count == 0:
        final_results = LOW_AVERAGE_LABEL
    else:
        for subject, students in sorted_subjects:
            final_results += f"{subject} {len(students)}\n"
            for student in students:
                final_results += f"{student}\n"

    with open(RESULTS_FILE, "w", encoding="utf-8") as results_file:
        results_file.write(final_results.strip())

main()