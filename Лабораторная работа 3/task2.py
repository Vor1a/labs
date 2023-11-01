# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


def find_common_participants(group1, group2, delimiter=","):
    participants1 = group1.split(delimiter)
    participants2 = group2.split(delimiter)

    common_participants = list(set(participants1) & set(participants2))
    common_participants.sort()

    return common_participants

# TODO Провеьте работу функции с разделителем отличным от запятой


common_participants = find_common_participants(participants_first_group, participants_second_group, "|")
print(common_participants)
