users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

visitors = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}

visitors["Общее количество"] = len(users)
visitors["Уникальные посещения"] = len(set(users))
print(visitors)