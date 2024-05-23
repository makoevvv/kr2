import random
import csv

goods = {
    'Snickers':['chocolate', 90],
    'Twix':['chocolate', 85],
    'Lays':['snacks', 97],
    'Parlament':['cigarettes', 180],
    'Coca-Cola':['sugary_drinks', 97],
    'Pepsi':['sugary_drinks', 90],
    'Chechil':['dairy_products', 150],
    'Bacon':['meat', 190],
    'Dove_Chocolate':['chocolate', 30],
    'Chicken_Fillet':['meat', 230],
    'Harvest':['cigarettes', 260],
    'Wiskey':['alcohol', 2300],
    'Wine':['alcohol', 1400],
    'Beer':['alcohol', 90],
    'Milk':['dairy_products', 100],
    'Sour_Cream':['dairy_products', 90],
    'Eggs':['meat', 130],
    'Banana':['fruits', 130],
    'Apple':['fruits', 90],
    'Pizza':['ready_made_food', 270],
    'Apple_Juice':['sugary_drinks', 120],
    'Nachos':['snacks', 150],
    'Popcorn':['snacks', 73],
    'Mars':['chocolate', 90],
    'Picnic':['chocolate', 79],
    'Chapman_Green':['cigarettes', 230],
    'Chapman_Rose':['cigarettes', 230],
    'Chapman_Brown':['cigarettes', 230]
}

mas = []


for i in range(1, 1000):
    name = random.choice(list(goods))
    number = random.randint(30, 1000)

    mas.append(f"{i};{random.randint(2015, 2024)}-{random.randint(1, 12)}-{random.randint(1, 28)};{name};{goods[name][0]};{number};{goods[name][1]};{goods[name][1] * number}")


with open('data.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    
    spamwriter.writerow(["|Номер заказа|;|Дата заказа|;|Название товара|;|Категория товара|;|Количество продаж|;|Цена за единицу|;|Общая стоимость|"])
    for i in mas:
        spamwriter.writerow([i])