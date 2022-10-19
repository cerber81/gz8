# добавление строки в базу

def adding():
    to_add = []
    print("Вы добавляете в базу информацию. Если вы не можете заполнить поле, введите None")
    to_add.append(input('Имя: '))
    to_add.append(input('Должность в Хогвардс: '))
    to_add.append(input('Какой предмет преподает: '))
    to_add.append(input('Как зовут его питомца: '))
    to_add.append(input('Дополнительные сведения: '))
    with open('last_key.txt', "r") as my_f:
        last_key = my_f.readline().split()
        new_key = int(last_key[2])
    with open('Hogwarts.csv', "a", encoding='utf-8') as base:
        base.write('{};{};{};{};{};{}\n'.format(new_key + 1, to_add[0], to_add[1], to_add[2], to_add[3], to_add[4]))
    with open('last_key.txt', "w", encoding='utf-8') as my_f:
        my_f.write(f"last_key = {new_key + 1}")

