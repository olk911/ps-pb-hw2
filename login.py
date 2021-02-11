account1 = {
    "login" : "ivan", 
    "password" : "q1"
    }
account2 = {
     "login" : "petr", 
     "password" : "q2"
    }
account3 = {
    "login" : "olga", 
    "password" : "q3"
    }
account4 = {
    "login" : "anna", 
    "password" : "q4"
    }
user1 = {
    "name" : "Иван",
    "age" : 20, 
    "account" : account1
    }
user2 = {
    "name" : "Петр", 
    "age" : 25, 
    "account" : account2
    }
user3 = {
    "name" : "Ольга", 
    "age" : 18, 
    "account" : account3
    }
user4 = {
    "name" : "Анна", 
    "age" : 27, 
    "account" : account4
    }

account_list = [account1, account2, account3, account4]

user_list = [user1, user2, user3, user4]

print(account_list)
print(user_list)

a = input( 'Введите ключ (name или account): ' )
a1 = a.lower()

try:
    print(f"Значение ключа name для юзера1 = {user1[a1]}")
    print(f"Значение ключа name для юзера2 = {user2[a1]}")
    print(f"Значение ключа name для юзера3 = {user3[a1]}")
    print(f"Значение ключа name для юзера4 = {user4[a1]}")
except KeyError:
    try:
        print(f"Значение ключа account для юзера1 = {user1[a1]}")
        print(f"Значение ключа account для юзера2 = {user2[a1]}")
        print(f"Значение ключа account для юзера3 = {user3[a1]}")
        print(f"Значение ключа account для юзера4 = {user4[a1]}")
    except KeyError:    
        print("Введенный ключ не найден")

b = input("Введите порядковый номер: ")
b1 = int(b)
try:
    user_b = user_list[b1-1]
    print(f"Данные по юзеру № {b1}:")
    print(f"имя: {user_b['name']} \nвозраст: {user_b['age']}")
    print(f"логин: {user_b['account']['login']} \nпароль: {user_b['account']['password']}")
except IndexError:
    print("Введенный порядковый номер не найден")    

c = input("Введите gорядковый номер пользователя, которого нужно переместить в конец: ")
c1 = int(c)
try:
    user_c = user_list[c1-1]
    #print(user_c)
    print('список пользователей до изменения: ')
    print(f"{user_list[0]['name']}")
    print(f"{user_list[1]['name']}")
    print(f"{user_list[2]['name']}")
    print(f"{user_list[3]['name']}")
    user_list.remove(user_c)
    #print(user_list)

    user_list.append(user_c)
    #print(user_list)

    print('список пользователей после изменения: ')
    print(f"{user_list[0]['name']}")
    print(f"{user_list[1]['name']}")
    print(f"{user_list[2]['name']}")
    print(f"{user_list[3]['name']}")
except IndexError:
    print("Введенный порядковый номер пользователя не найден") 

#print(user1['age'])
#print(user_list[0]['age'])

average = (user_list[0]['age'] + user_list[1]['age'] + user_list[2]['age'] + user_list[3]['age'])/len(user_list)
print(average)