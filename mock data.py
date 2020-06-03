# Generating mock data in Python by using random.choice function. Data are saved in CSV format and stored. We start
# from a simple example and move towards more realistic data. Thank you 'Keith_Galli' for your tutorials and ideas.
import pandas as pd
import random
import numpy
import datetime
import calendar

products = {
    # Product: [Price, weight]
    'iPhone': [700, 10],
    'Google Phone': [600, 8],
    'Vareebadd Phone': [400, 3],
    '20in Monitor': [109.99, 6],
    '34in Ultrawide Monitor': [379.99, 9],
    '27in 4K Gaming Monitor': [389.99, 9],
    '27in FHD Monitor': [149.99, 11],
    'Flatscreen TV': [300, 7],
    'Macbook Pro Laptop': [1700, 7],
    'ThinkPad Laptop': [999.99, 6],
    'AA Batteries (4-pack)': [3.84, 30],
    'AAA Batteries (4-pack)': [2.99, 30],
    'USB-C Charging Cable': [11.95, 30],
    'Lightning Charging Cable': [14.95, 30],
    'Wired Headphones': [11.99, 26],
    'Bose SoundSport Headphones': [99.99, 19],
    'Apple Airpods Headphones': [150, 22],
    'LG Washing Machine': [600.00, 1],
    'LG Dryer': [600.00, 1]
}

product_list = [product for product in products]
weights = [products[product][1] for product in products]

columns = ['Order ID', 'Product', 'Quantity Ordered', 'Price Each', 'Order Date', 'Purchase Address']

order_id = 143253

for month_value in range(1, 13):
    if month_value <= 10:
        orders_amount = int(numpy.random.normal(loc=12000, scale=4000))

        if month_value == 11:
            orders_amount = int(numpy.random.normal(loc=20000, scale=3000))

        if month_value == 12:
            orders_amount = int(numpy.random.normal(loc=26000, scale=3000))

        df = pd.DataFrame(columns=columns)

        for i in range(orders_amount):

            product = random.choices(product_list, weights=weights)[0]
            price = products[product]
            df.loc[i] = [order_id, product, 1, price, 'NA', 'NA']

            order_id += 1

        month_name = calendar.month_name[month_value]
        print(month_name + 'Finished!!')
        df.to_csv(f'{month_name}_data.csv')
        break
