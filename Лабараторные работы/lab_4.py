users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
stat = {"Общее количество": 0, "Уникальные посещения": 0}
len_users = len(users)
stat["Общее количество"] = len_users
unique_users = set(users)
stat["Уникальные посещения"] = len(unique_users)

print(stat)
