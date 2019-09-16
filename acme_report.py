from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    for _ in range(num_products):
        rand_adj = sample(ADJECTIVES, 1)
        rand_noun = sample(NOUNS, 1)
        rand_adj.append(rand_noun[0])
        # print(rand_adj)
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0.0, 2.5)
        product = Product(rand_adj, price, weight, flammability)
        products.append(product)

    return products


def inventory_report(products):
    num_unique_prod_name = []
    total_price = 0
    total_weight = 0
    total_flammability = 0

    for product in products:
        if product.name not in num_unique_prod_name:
            num_unique_prod_name.append(product.name)
        total_price += product.price
        total_weight += product.weight
        total_flammability += product.flammability

    total = len(num_unique_prod_name)
    avg_price = total_price / total
    avg_weight = total_weight / total
    avg_flammability = total_flammability / total

    print('\nACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'Unique product names: {len(num_unique_prod_name)}')
    print(f'Average Price: {avg_price:.1f}')
    print(f'Average Weight: {avg_weight:.1f}')
    print(f'Average Flammability: {avg_flammability:.1f}')


if __name__ == '__main__':
    inventory_report(generate_products())
