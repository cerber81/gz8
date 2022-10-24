def user_choice():
    try:
        choice1 = int(input('Please enter you choice: '))
    except ValueError:
        print('Error')
        error_enter()
    return choice1

def data_search():
    try:
        search = input('Please, enter search data: ')
    except ValueError:
        print('Error')
        error_enter()
    return search