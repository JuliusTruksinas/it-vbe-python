# Task constants
DATA_FILE = "U2.txt"
RESULTS_FILE = "U2rez.txt"
DISH_NAME_SIZE = 15

def main():
    product_prices, dishes = read_data_file()
    write_results_to_a_file(product_prices, dishes)

# This function reads the data file and returns the product prices and all of the dishes
def read_data_file():
    with open(DATA_FILE, "r", encoding="utf-8") as data_file:
        lines = data_file.read().strip().split("\n")
        product_prices = [int(d) for d in lines[1].split()]
        # key: dish name, value: the amount of ingredients needed to make the dish
        dishes = {}
        for line in lines[2:]:
            dish_name = line[:DISH_NAME_SIZE]
            amount_of_products = [int(d) for d in line[DISH_NAME_SIZE:].split()]
            dishes[dish_name] = amount_of_products
        
        return product_prices, dishes

# This function calculates how many cents does one dish cost
def get_one_dish_price(product_prices, product_amounts):
    price = 0
    for i, product_amount in enumerate(product_amounts):
        price += product_amount * product_prices[i]
    return price

# This function calculates how many euros and cents it will cost to buy the lunch package (it includes all dishes)
def get_total_lunch_price(dishes, product_prices):
    price = 0
    for product_amounts in dishes.values():
        price += get_one_dish_price(product_prices, product_amounts)

    euros = price // 100
    cents = price % 100

    return euros, cents

# This function writes the results to a file as specified in the task
def write_results_to_a_file(product_prices, dishes):
    final_results = ""

    for dish_name, product_amounts in dishes.items():
        final_results += f"{dish_name} {get_one_dish_price(product_prices, product_amounts)}\n"
    
    euros, cents = get_total_lunch_price(dishes, product_prices)
    final_results += f"{euros} {cents}"

    with open(RESULTS_FILE, "w", encoding="utf-8") as results_file:
        results_file.write(final_results)
        
main()