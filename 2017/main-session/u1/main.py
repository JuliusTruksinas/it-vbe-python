# Task constants
DATA_FILE = "U1.txt"
RESULTS_FILE = "U1rez.txt"
REPRESENTATIONS = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

def main():
    row_count, column_count, rgb_values = read_data_file()
    results_table = generate_results_table(row_count, column_count, rgb_values)
    write_results_to_a_file(results_table)

# This function reads the data file and returns all of the rgb values,the desired row and column count of the results table
def read_data_file():
    with open(DATA_FILE, "r", encoding="utf-8") as data_file:
        rgb_values = []
        lines = data_file.read().strip().split("\n")
        row_count, column_count = [int(d) for d in lines[0].split()]

        for line in lines[1:]:
            rgb_values.append([int(d) for d in line.split()])

        return row_count, column_count, rgb_values

# This function converts a decimal number to hexadecimal
def convert_decimal_to_hexadecimal(decimal_number):
    first_digit = REPRESENTATIONS.get(decimal_number // 16) or decimal_number // 16
    second_digit = REPRESENTATIONS.get(decimal_number % 16) or decimal_number % 16
    return str(first_digit) + str(second_digit)

# This function generates a (string) table of converted decimal numbers to hexadecimal given a column size and row size
def generate_results_table(row_count, column_count, rgb_values):
    i = 0
    table = ""
    for _ in range(row_count):
        for k in range(column_count):
            table += "".join([convert_decimal_to_hexadecimal(rgb_value) for rgb_value in rgb_values[i]])
            if k != column_count - 1:
                table += ";"
            i += 1
        table += "\n"
    return table.strip()

# This function writes the results to a file as specified in the task
def write_results_to_a_file(results_table):
    with open(RESULTS_FILE, "w", encoding="utf-8") as results_file:
        results_file.write(results_table)

main()