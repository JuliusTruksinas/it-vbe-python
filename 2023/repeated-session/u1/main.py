# task constants
DATA_FILE = "U1.txt"
RESULTS_FILE = "U1rez.txt"
QUESTIONS_PER_TEST = 10
PASS_RATE_PERCENTAGE = 50
TEST_NAME_LENGTH = 6
ALL_STUDENTS_COUNT = "all_students_count"
STUDENTS_PASSED_EXAM_COUNT = "students_passed_exam_count"
MAXIMUM_POINTS = "maximum_points"
MAXIMUM_POINTS_PER_TEST = 3

def main():
    tests = read_data_file()
    write_results_to_a_file(tests)

# this function reads the data file and returns all tests in a dict:
# key: test name; value: dict with that tests data
def read_data_file():
    tests = {}

    with open(DATA_FILE, "r", encoding="utf-8") as data_file:
        for line in data_file.read().strip().split("\n")[1:]:
            test_name = line[:TEST_NAME_LENGTH]
            points = [int(d) for d in line[TEST_NAME_LENGTH+1:].split()]
            total_score = sum(points)
            
            found_test = tests.get(test_name, {ALL_STUDENTS_COUNT: 0, STUDENTS_PASSED_EXAM_COUNT: 0, MAXIMUM_POINTS: 0})
            found_test[ALL_STUDENTS_COUNT] += 1

            if total_score >= QUESTIONS_PER_TEST * MAXIMUM_POINTS_PER_TEST * (PASS_RATE_PERCENTAGE / 100):
                found_test[STUDENTS_PASSED_EXAM_COUNT] += 1

            if total_score > found_test[MAXIMUM_POINTS]:
                found_test[MAXIMUM_POINTS] = total_score
            
            tests[test_name] = found_test
    
    return tests

# this function writes the results to a file as specified in the task
def write_results_to_a_file(tests):
    final_results = ""
    for test_name, test_data in tests.items():
        final_results += f"{test_name} {test_data[ALL_STUDENTS_COUNT]} {round(test_data[STUDENTS_PASSED_EXAM_COUNT]/test_data[ALL_STUDENTS_COUNT] * 100)}% {test_data[MAXIMUM_POINTS]}\n"
    
    with open(RESULTS_FILE, "w", encoding="utf-8") as results_file:
        results_file.write(final_results.strip("\n"))

main()