# task constants
DATA_FILE = "U1.txt"
RESULTS_FILE = "U1rez.txt"

def main():
    buckets_count, oil_amount, production_cost, buckets_prices = read_data_file()
    buckets_used_count, oil_amount_left, buckets_unused_count = fill_the_buckets(oil_amount, buckets_count)
    buckets_short_count = get_how_many_buckets_short(oil_amount_left)
    profit = calculate_profit(buckets_used_count, buckets_short_count , buckets_prices, production_cost)
    write_results_to_a_file(buckets_used_count, oil_amount_left, buckets_unused_count, buckets_short_count, profit)

# this function reads the data file and returns buckets count, oil amount, oil production cost and buckets prices
def read_data_file():
    with open(DATA_FILE, "r", encoding="utf-8") as data_file:
        lines = data_file.read().strip().split("\n")
        *buckets_count, oil_amount = [int(d) for d in lines[0].split()]
        production_cost, *buckets_prices = [int(d) for d in lines[1].split()]
    return buckets_count, oil_amount, production_cost, buckets_prices

# this function calculates how many buckets will be used, how many will remain and the amount of oil that will not be filled in a bucket
def fill_the_buckets(oil_amount, buckets_count):
    # there are three buckets: one litre, three litres and five litres in that order
    # the priority is to fill up the biggest bucket
    oil_amount_left = oil_amount
    buckets_unused_count = buckets_count[:]
    buckets_used_count = [0] * 3
    while True:
        if oil_amount_left - 5 >= 0 and buckets_unused_count[2] > 0:
            oil_amount_left -= 5
            buckets_unused_count[2] -= 1
            buckets_used_count[2] += 1
        elif oil_amount_left - 3 >= 0 and buckets_unused_count[1] > 0:
            oil_amount_left -= 3
            buckets_unused_count[1] -= 1
            buckets_used_count[1] += 1
        elif oil_amount_left - 1 >= 0 and buckets_unused_count[0] > 0:
            oil_amount_left -= 1
            buckets_unused_count[0] -= 1
            buckets_used_count[0] += 1
        else:
            break
    return buckets_used_count, oil_amount_left, buckets_unused_count

# This function calculates how many of each bucket would be needed to pour out all of the remaining oil
def get_how_many_buckets_short(oil_amount):
    oil_amount_left = oil_amount
    buckets_used_count = [0] * 3
    while True:
        if oil_amount_left - 5 >= 0:
            oil_amount_left -= 5
            buckets_used_count[2] += 1
        elif oil_amount_left - 3 >= 0:
            oil_amount_left -= 3
            buckets_used_count[1] += 1
        elif oil_amount_left - 1 >= 0:
            oil_amount_left -= 1
            buckets_used_count[0] += 1
        else:
            break
    return buckets_used_count

# This function calculates the possible profit. we sum up all the used buckets with all buckets that we are short of, and then multiply
# each one by their selling price and finally we subtract the production cost
def calculate_profit(buckets_used_count, buckets_short_count, buckets_prices, production_cost):
    buckets_that_would_be_sold = [sum(buckets) for buckets in zip(buckets_used_count, buckets_short_count)]
    profit = sum([item[0] * item[1] for item in zip(buckets_that_would_be_sold, buckets_prices)]) - production_cost
    return profit

# this function writes the results to a file as specified in the task
def write_results_to_a_file(buckets_used_count, oil_amount_left, buckets_unused_count, buckets_short_count, profit):
    final_results = f"{' '.join([str(d) for d in buckets_used_count])} {oil_amount_left}\n"
    final_results += f"{' '.join([str(d) for d in buckets_unused_count])}\n"
    final_results += f"{' '.join([str(d) for d in buckets_short_count])}\n"
    final_results += str(profit)

    with open(RESULTS_FILE, "w", encoding="utf-8") as results_file:
        results_file.write(final_results)

main()