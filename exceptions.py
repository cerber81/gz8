def user_choice():
    choice1 = input('Please enter you choice: ')
    try:
        choice1 = int(choice1)
        if choice1 > 5 and choice1 < 0:
            return print('Error'), user_choice() 
        else:   
            return choice1    
    except ValueError:
        print('Error')
        # error_enter()
        return user_choice()




# def data_search():
#     try:
#         search = input('Please, enter search data: ')
#     except ValueError:
#         print('Error')
#         error_enter()
#     return search




        



