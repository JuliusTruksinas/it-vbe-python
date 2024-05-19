# task constants
DATA_FILE = "U1.txt"
RESULTS_FILE = "U1rez.txt"
NAME_LENGTH = 10
PRICES = "prices"
MIN_PRICE_ITEMS = "min_price_items"
TOO_EXPENSIVE_LABEL = "Nepavyks nusipirkti"

def main():
  favourite_fruits, budget, stores = read_data_file()
  min_prices = get_min_prices(stores)
  total_min_price = round(sum(min_prices), 2)
  get_stores_min_price_items(stores, min_prices, favourite_fruits)
  write_results_to_a_file(total_min_price, round(budget, 2), stores)

# this function reads the data file and returns the favourite fruits, budget and all of the stores data
def read_data_file():
  stores = {}
  with open(DATA_FILE, "r", encoding="utf-8") as data_file:
    budget = float(data_file.readline().strip().split()[1])
    favourite_fruits = [
        fruit.ljust(NAME_LENGTH)
        for fruit in data_file.readline().strip().split()
    ]
    for line in data_file.read().strip().split("\n"):
      store_name = line[:NAME_LENGTH]
      prices = [float(d) for d in line[NAME_LENGTH + 1:].split()]
      stores[store_name] = {PRICES: prices}
    return favourite_fruits, budget, stores

# this function gets the min prices of every product and returns them in a list
def get_min_prices(stores):
  stores_prices = [item[PRICES] for item in stores.values()]
  return [
      min([price for price in prices if price > 0])
      for prices in zip(*stores_prices)
  ]

# this function gets all of the products that have the lowest price in that store
def get_stores_min_price_items(stores, min_prices, favourite_fruits):
  for store_data in stores.values():
    store_data[MIN_PRICE_ITEMS] = []
    for i, price in enumerate(store_data[PRICES]):
      if price == min_prices[i]:
        store_data[MIN_PRICE_ITEMS].append(favourite_fruits[i])


# this function writes the results to a file as specified in the task
def write_results_to_a_file(total_min_price, budget, stores):
  if total_min_price > budget:
    with open(RESULTS_FILE, "w", encoding="utf-8") as results_file:
      results_file.write(TOO_EXPENSIVE_LABEL)
      return

  final_results = f"{total_min_price:.2f}\n"
  sorted_stores = sorted(stores.items(), key=lambda item: len(item[1][MIN_PRICE_ITEMS]), reverse=True)
  for store_name, store_data in sorted_stores:
    if len(store_data[MIN_PRICE_ITEMS]) == 0:
      continue
    final_results += f"{store_name} {' '.join(store_data[MIN_PRICE_ITEMS])}\n"
  with open(RESULTS_FILE, "w", encoding="utf-8") as results_file:
    results_file.write(final_results.strip("\n"))
  
main()