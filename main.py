import log
from person_search2 import person_search

def input_menu_choice():
    log.start_app()
    while True:
        print()
        print('-----------------------')
        print('What do you want to do?')
        print('-----------------------')
        print()
        print('1. Show all')
        print('2. Find info')
        print('3. Add new info')
        print('4. Change info')
        print('5. Delete info')
        print('0. Exit')
        choice_menu = user_choice()
        if choice_menu == 1:

        elif choice_menu == 2:
            print('1. Find by name')
            print('2. Find by position')
            print('0. Exit')
            if choice_menu == 1:
                person_search()
            elif choice_menu == 2:

            elif choice_menu == 0:

            else:
                print('Error')
                input_menu_choice()
        elif choice_menu == 3:
            to_add = adding()
            log.add(to_add)
        elif choice_menu == 4:
            return 4
        elif choice_menu == 5:
            del_key = delete_contact()
            log.del_item(del_key)
        elif choice_menu == 6:
            phonebook = get_data.data_entry()
            writing_scv(phonebook)
            writing_txt(phonebook)
            new_key = max(phonebook)
            with open('last_key.txt', "w", encoding='utf-8') as my_f:
                my_f.write(f"last_key = {new_key}")
            log.new_book()

        elif choice_menu == 0:
            log.end_app()
            return exit()
        else:
            return input_menu_choice()


print(input_menu_choice())