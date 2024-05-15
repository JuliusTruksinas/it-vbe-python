# task constants
DATA_FILE = "U2.txt"
RESULTS_FILE = "U2rez.txt"
PASSWORD_LENGTH = 15
STRENGTH_LABEL_LENGTH = 9
PASSWORD = "password"
PARAMETERS = "parameters"
STRENGTH_LABEL = "strength_label"
SIMILARITY_COEFFICIENT = "similarity_coefficient"

def main():
    user_passwords, prewritten_passwords = read_data_file()

    for user_password in user_passwords:
        find_most_similar_password(user_password, prewritten_passwords)

    write_results_to_a_file(user_passwords, prewritten_passwords)

# this function reads the data file and returns the users passwords and the prewritten passwords
def read_data_file():
    user_passwords = []
    prewritten_passwords = []
    with open(DATA_FILE, "r", encoding="utf-8") as data_file:
        n, s = [int(d) for d in data_file.readline().strip().split()]
        for _ in range(n):
            password, *parameters = data_file.readline().strip().split()
            password = password.ljust(PASSWORD_LENGTH)
            parameters = [int(d) for d in parameters]
            user_passwords.append({PASSWORD: password, PARAMETERS: parameters})

        for _ in range(s):
            password, *parameters, strength_label = data_file.readline().strip().split()
            strength_label = strength_label.ljust(STRENGTH_LABEL_LENGTH)
            parameters = [int(d) for d in parameters]
            password = password.ljust(PASSWORD_LENGTH)
            prewritten_passwords.append({PASSWORD: password, PARAMETERS: parameters, STRENGTH_LABEL: strength_label})
    
    return user_passwords, prewritten_passwords

# this function calculates the similarity coefficient of two passwords
def compare_password(password_1, password_2):
    similarity_coefficient = 0
    for i in range(len(password_1[PARAMETERS])):
        similarity_coefficient += abs(password_1[PARAMETERS][i] - password_2[PARAMETERS][i])
    return similarity_coefficient

# this function takes a user password, finds the most similar password out of the prewritten ones
# adds the similarity coefficient and a strength label to the user password, based on the most similar password found
def find_most_similar_password(user_password, prewritten_passwords):
    minimum_similarity_coefficient = compare_password(user_password, prewritten_passwords[0])
    most_similar_password = prewritten_passwords[0]

    for password in prewritten_passwords[1:]:
        similarity_coefficient = compare_password(user_password, password)
        if similarity_coefficient < minimum_similarity_coefficient:
            minimum_similarity_coefficient = similarity_coefficient
            most_similar_password = password
    
    user_password[SIMILARITY_COEFFICIENT] = minimum_similarity_coefficient
    user_password[STRENGTH_LABEL] = most_similar_password[STRENGTH_LABEL]

# this function returns only those prewritten passwords which have the same similarity coefficient, as the password provided
def find_prewritten_similar_password(password, prewritten_passwords):
    similar_passwords = []
    for prewritten_password in prewritten_passwords:
        if compare_password(password, prewritten_password) == password[SIMILARITY_COEFFICIENT]:
            similar_passwords.append(prewritten_password)
    return similar_passwords

# this function writes the results to a file as specified in the task
def write_results_to_a_file(user_passwords, prewritten_passwords):
    final_results = ""

    for user_password in user_passwords:
        prewritten_similar_passwords = find_prewritten_similar_password(user_password, prewritten_passwords)
        sorted_passwords = sorted(prewritten_similar_passwords, key=lambda password: len(password[PASSWORD].strip()), reverse=True)
        final_results += f"{user_password[PASSWORD]} {user_password[STRENGTH_LABEL]} {user_password[SIMILARITY_COEFFICIENT]}\n"
        
        for password in sorted_passwords:
            final_results += f"{password[PASSWORD]}\n"
    
    with open(RESULTS_FILE, "w", encoding="utf-8") as results_file:
        results_file.write(final_results.rstrip("\n"))

main()