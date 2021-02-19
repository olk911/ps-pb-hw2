cities = ['Москва', 'Париж', 'Лондон']

users = [{'name': 'Иван', 'age': 35},
         {'name': 'Мария', 'age': 22},
         {'name': 'Соня', 'age': 20}]

tourists = [{'user': users[0], 'city': cities[2]},   # Иван - 35 - Лондон
            {'user': users[1], 'city': cities[0]},   # Мария - 22 -Москва
            {'user': users[2], 'city': cities[1]}]   # Соня - 20 - Париж

city = input('Введите город: ')

if tourists[0]['city'].lower() == city.lower():
    user = tourists[0]['user']
    #print(user['name'])
    print(f'Турист {user["name"]}, возраст {user["age"]} - посетил город {tourists[0]["city"]}')
elif tourists[1]['city'].lower() == city.lower():
    user = tourists[1]['user']
    #print(user['name'])
    print(f'Турист {user["name"]}, возраст {user["age"]} - посетил город {tourists[1]["city"]}')
elif tourists[2]['city'].lower() == city.lower():
    user = tourists[2]['user']
    #print(user['name'])
    print(f'Турист {user["name"]}, возраст {user["age"]} - посетил город {tourists[2]["city"]}')
else:
    print(f"В городе {city} наши туристы не были!")